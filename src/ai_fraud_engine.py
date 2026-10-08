"""
AI Fraud Engine Module
Implements Strategy and Abstract Factory patterns for scalable AI integration.
"""
from abc import ABC, abstractmethod

# --- Strategy Pattern for Interchangeable Algorithms ---
class FraudDetectionStrategy(ABC):
    @abstractmethod
    def evaluate_risk_score(self, amount: float) -> float:
        """Evaluates transaction risk. Returns a probability between 0.0 and 1.0"""
        pass

class MLHeuristicStrategy(FraudDetectionStrategy):
    def evaluate_risk_score(self, amount: float) -> float:
        # Simulated local Machine Learning heuristic evaluation
        if amount >= 10000:
            return 0.85 # High Risk
        elif amount > 5000:
            return 0.40 # Medium Risk
        return 0.05 # Low Risk

class CloudAIStrategy(FraudDetectionStrategy):
    def evaluate_risk_score(self, amount: float) -> float:
        # Simulated external API call to Cloud AI
        return 0.90 if amount > 8000 else 0.10

# --- Abstract Factory Pattern for Vendor Neutrality ---
class AIServiceFactory(ABC):
    @abstractmethod
    def instantiate_fraud_engine(self) -> FraudDetectionStrategy:
        pass

class OnPremiseAIFactory(AIServiceFactory):
    """Instantiates highly secure, local edge-AI models."""
    def instantiate_fraud_engine(self) -> FraudDetectionStrategy:
        return MLHeuristicStrategy()

class CloudAIFactory(AIServiceFactory):
    """Instantiates cloud-based AI models."""
    def instantiate_fraud_engine(self) -> FraudDetectionStrategy:
        return CloudAIStrategy()
