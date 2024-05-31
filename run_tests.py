import unittest
from src.tests import search

if __name__ == "__main__":
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(search)
    runner = unittest.TextTestRunner()
    runner.run(suite)
