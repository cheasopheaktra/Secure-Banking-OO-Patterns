"""
Unit Testing Module
Utilizes mocking to isolate OO architecture from non-deterministic AI outputs.
"""
import unittest
from unittest.mock import MagicMock
from src.banking_system import SecureBankingSystem
from src.ai_fraud_engine import AIServiceFactory

class TestFraudDetectionIntegration(unittest.TestCase):
    
    def setUp(self):
        # Mock the AI Factory to isolate testing environment
        self.mock_factory = MagicMock(spec=AIServiceFactory)
        self.mock_ai_engine = MagicMock()
        self.mock_factory.instantiate_fraud_engine.return_value = self.mock_ai_engine
        
        # Initialize Banking System with the Mock Factory
        self.system = SecureBankingSystem(self.mock_factory)
        self.system.create_account("ACC_01", 20000)
        self.system.create_account("ACC_02", 5000)

    def test_transaction_blocked_on_high_ai_risk(self):
        # Arrange: Simulate AI returning a 98% fraud probability
        self.mock_ai_engine.evaluate_risk_score.return_value = 0.98 
        
        # Act
        transfer_status = self.system.process_transfer("ACC_01", "ACC_02", 15000)
        
        # Assert: Transaction must fail due to high risk, preserving balances
        self.assertFalse(transfer_status, "Transaction should be blocked.")
        self.assertEqual(self.system.accounts["ACC_01"].get_balance(), 20000)
        self.mock_ai_engine.evaluate_risk_score.assert_called_once_with(15000)

    def test_transaction_success_on_low_ai_risk(self):
        # Arrange: Simulate AI returning a safe 10% risk probability
        self.mock_ai_engine.evaluate_risk_score.return_value = 0.10 
        
        # Act
        transfer_status = self.system.process_transfer("ACC_01", "ACC_02", 2000)
        
        # Assert: Transaction must succeed
        self.assertTrue(transfer_status, "Transaction should succeed.")
        self.assertEqual(self.system.accounts["ACC_01"].get_balance(), 18000)
        self.assertEqual(self.system.accounts["ACC_02"].get_balance(), 7000)

if __name__ == '__main__':
    unittest.main()
