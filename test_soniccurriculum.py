# test_soniccurriculum.py
"""
Tests for SonicCurriculum module.
"""

import unittest
from soniccurriculum import SonicCurriculum

class TestSonicCurriculum(unittest.TestCase):
    """Test cases for SonicCurriculum class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SonicCurriculum()
        self.assertIsInstance(instance, SonicCurriculum)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SonicCurriculum()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
