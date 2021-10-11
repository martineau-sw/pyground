import unittest
import searches

class TestSearches(unittest.TestCase):
    
    def test_sequential(self):
        list = [x for x in range(0,9)]


        self.assertEqual(searches.sequential(list,0), 0)       # First in list
        self.assertEqual(searches.sequential(list,4), 4)        # Middle of list
        self.assertEqual(searches.sequential(list,8), 8)    # Last in list
        self.assertEqual(searches.sequential(list,10), -1)       # Not in list

    def test_sequential_sentinel(self):
        list = [27,-2,0,135,-2000]

        self.assertEqual(searches.sequential_sentinel(list,27), 0)      # First in list
        self.assertEqual(searches.sequential_sentinel(list,0), 2)       # Middle of list
        self.assertEqual(searches.sequential_sentinel(list,-2000), 4)   # Last in list
        self.assertEqual(searches.sequential_sentinel(list,5), -1)      # Not in list

    def test_binary(self):
        list = [0,1,1,2,3,5,8,13,21,34,55]

        self.assertEqual(searches.binary(list,0), 0)                    # First in list
        self.assertEqual(searches.binary(list,5), 5)                    # Middle of list
        self.assertEqual(searches.binary(list,55), 10)                   # Last in list
        self.assertEqual(searches.binary(list,89), -1)                  # Not in list

    def test_jump(self):
        list = [0,1,1,2,3,5,8,13,21,34,55]

        self.assertEqual(searches.jump(list,0), 0)             # First in list
        self.assertEqual(searches.jump(list,5), 5)                    # Middle of list
        self.assertEqual(searches.jump(list,55), 10)                   # Last in list
        self.assertEqual(searches.jump(list,89), -1) 

    def test_interpolation(self):
        list = [1.5 * x for x in range(50,100)]

        self.assertEqual(searches.interpolation(list, list[0]), 0)
        self.assertEqual(searches.interpolation(list, list[len(list)//2]), len(list)//2)
        self.assertEqual(searches.interpolation(list, list[len(list)-1]), len(list)-1)
        self.assertEqual(searches.interpolation(list, list[len(list)-1]+1), -1)

    def test_exponential(self):
        list = [x for x in range(0,1000)]

        self.assertEqual(searches.exponential(list, list[0]), 0)
        self.assertEqual(searches.exponential(list, list[len(list)//2]), len(list)//2)
        self.assertEqual(searches.exponential(list, list[len(list)-1]), len(list)-1)
        self.assertEqual(searches.exponential(list, list[len(list)-1]+1), -1)

if(__name__ == '__main__'):
    unittest.main()