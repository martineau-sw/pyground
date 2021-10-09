import unittest
import searches

class TestSearches(unittest.TestCase):
    

    def test_sequential(self):
        list = [27,-2,0,135,-2000]

        self.assertEqual(searches.sequential(list,27), 0)       # First in list
        self.assertEqual(searches.sequential(list,0), 2)        # Middle of list
        self.assertEqual(searches.sequential(list,-2000), 4)    # Last in list
        self.assertEqual(searches.sequential(list,5), -1)       # Not in list

    def test_sequential_sentinel(self):
        list = [27,-2,0,135,-2000]

        self.assertEqual(searches.sequential_sentinel(list,27), 0)      # First in list
        self.assertEqual(searches.sequential_sentinel(list,0), 2)       # Middle of list
        self.assertEqual(searches.sequential_sentinel(list,-2000), 4)   # Last in list
        self.assertEqual(searches.sequential_sentinel(list,5), -1)      # Not in list

if(__name__ == '__main__'):
    unittest.main()