# test_consensusforge.py
"""
Tests for ConsensusForge module.
"""

import unittest
from consensusforge import ConsensusForge

class TestConsensusForge(unittest.TestCase):
    """Test cases for ConsensusForge class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ConsensusForge()
        self.assertIsInstance(instance, ConsensusForge)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ConsensusForge()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
