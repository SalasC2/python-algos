import flatten_list
import unittest

class TestFlattenList(unittest.TestCase):
    """
    Test the Flatten function from the Flatten list File
    """
 
    def test_empty_flatten_list(self):
        """
        Return empty array when array is empty
        """
        result = flatten_list.flatten3([])
        print(result)
        self.assertEqual(result, [])
 
    def test_simple_nested_flatten_list(self):
        """
        Test flattening of simple nested array
        """
        result = flatten_list.flatten3([[2], 3, [], 4, [[6], 7]])
        print(result)
        self.assertEqual(result, [2, 3, 4, 6, 7])

 
    def test_complicated_nested_flatten_list(self):
        """
        Test flattenting of multiple stacked nested array using recursion function
        """
        result = flatten_list.flatten([[1], 2, [[3, 4], 5], [[[]]], [[[6]]], 7, 8, []])
        print(result)
        self.assertEqual(result, [1, 2, 3, 4, 5, 6, 7, 8])
        

 
 
if __name__ == '__main__':
    unittest.main()
