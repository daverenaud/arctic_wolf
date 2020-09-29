import sys
import unittest

loader = unittest.TestLoader()
suite = unittest.TestSuite()
suite.addTests(loader.discover('tests', '*.py'))
result = unittest.TextTestRunner(stream=sys.stdout, failfast=True).run(suite)

exit(0 if len(result.errors) == 0 and len(result.failures) == 0 else 1)
