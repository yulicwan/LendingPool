# test_lendingpool.py
"""
Tests for LendingPool module.
"""

import unittest
from lendingpool import LendingPool

class TestLendingPool(unittest.TestCase):
    """Test cases for LendingPool class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = LendingPool()
        self.assertIsInstance(instance, LendingPool)
        
    def test_run_method(self):
        """Test the run method."""
        instance = LendingPool()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
