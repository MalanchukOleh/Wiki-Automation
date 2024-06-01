import unittest
from src.tests import search_test

if __name__ == "__main__":
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(search_test)
    runner = unittest.TextTestRunner()
    runner.run(suite)
