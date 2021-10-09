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

    def test_binary(self):
        list = [0,1,2,3,5,8,13,21,34,55]

        self.assertEqual(searches.binary(list,1), 1)                    # First in list
        self.assertEqual(searches.binary(list,5), 4)                    # Middle of list
        self.assertEqual(searches.binary(list,55), 9)                   # Last in list
        self.assertEqual(searches.binary(list,89), -1)                  # Not in list

if(__name__ == '__main__'):
    unittest.main()