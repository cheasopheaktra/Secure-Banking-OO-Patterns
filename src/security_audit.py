"""
Security Auditing Module
Implements the Decorator pattern to ensure strict SOC/GRC compliance logging.
"""
import logging
from functools import wraps

# Configure standard logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def security_audit_logger(func):
    """
    Decorator isolating security logging from core business logic.
    Maintains Single Responsibility Principle (SRP).
    """
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        logging.info(f"AUDIT INIT: Initiating transaction via {func.__name__}")
        try:
            result = func(self, *args, **kwargs)
            if result:
                logging.info(f"AUDIT SUCCESS: Transaction authorized and completed.")
            else:
                logging.warning(f"AUDIT BLOCKED: Transaction denied by validation or AI constraints.")
            return result
        except Exception as e:
            logging.error(f"AUDIT EXCEPTION: System fault during {func.__name__} - {str(e)}")
            raise
    return wrapper
