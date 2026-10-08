"""
Secure Concurrent Banking System
Implements thread-safe Bank Accounts using RLock and canonical lock ordering.
Integrates AI Factory for dynamic fraud detection.
"""
import threading
from src.ai_fraud_engine import AIServiceFactory
from src.security_audit import security_audit_logger

class BankAccount:
    def __init__(self, account_id: str, initial_balance: float):
        self.account_id = account_id
        self._balance = initial_balance
        self.lock = threading.RLock() # Reentrant lock for thread safety

    def withdraw(self, amount: float) -> bool:
        with self.lock:
            if amount > 0 and self._balance >= amount:
                self._balance -= amount
                return True
            return False

    def deposit(self, amount: float):
        with self.lock:
            if amount > 0:
                self._balance += amount

    def get_balance(self) -> float:
        with self.lock:
            return self._balance


class SecureBankingSystem:
    def __init__(self, ai_factory: AIServiceFactory):
        self.accounts = {}
        # Instantiate the AI Engine via the injected Factory
        self.ai_engine = ai_factory.instantiate_fraud_engine()

    def create_account(self, account_id: str, initial_balance: float):
        self.accounts[account_id] = BankAccount(account_id, initial_balance)

    @security_audit_logger
    def process_transfer(self, from_id: str, to_id: str, amount: float) -> bool:
        """Executes a thread-safe transfer with AI fraud evaluation."""
        if from_id not in self.accounts or to_id not in self.accounts:
            return False

        # 1. AI Risk Evaluation (Strategy Pattern execution)
        risk_score = self.ai_engine.evaluate_risk_score(amount)
        if risk_score > 0.80: # Threshold for high risk
            print(f"FRAUD ALERT: Transfer of {amount} blocked. Risk Score: {risk_score}")
            return False

        account1 = self.accounts[from_id]
        account2 = self.accounts[to_id]

        # 2. Canonical Lock Ordering to prevent Deadlocks (Coffman conditions)
        first_lock, second_lock = (account1.lock, account2.lock) if from_id < to_id else (account2.lock, account1.lock)

        # 3. Critical Section Execution
        with first_lock:
            with second_lock:
                if account1.withdraw(amount):
                    account2.deposit(amount)
                    return True
                return False
