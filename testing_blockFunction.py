import unittest
import blockFunction as bf


class TestClosestBlockForFacilities(unittest.TestCase):
    def setUp(self):
        self.array1 = [
            { 
                'office': True,
                'cafe': True
            },
            {
                'office': False,
                'cafe': False
            },
            {
                'office': False,
                'cafe': False
            },
        ]
        self.array2 = [
            { 
                'office': True,
                'cafe': False
            },
            {
                'office': False,
                'cafe': False
            },
            {
                'office': False,
                'cafe': False
            },
        ]

    def test_func_1(self):
        result = bf.checkClosestBlockForFacilities(self.array1)
        self.assertEqual(result, 0)    #checking boolean statement - matching with result and expected value


    def test_func_2(self):
        result = bf.checkClosestBlockForFacilities(self.array2)
        self.assertEqual(result, False)

    def test_func_3(self):
        # Arrange
        array = [
            { 
                'office': True,
                'cafe': False
            },
            {
                'office': False,
                'cafe': False
            },
            {
                'office': False,
                'cafe': True
            },
        ]

        # Act
        result = bf.checkClosestBlockForFacilities(array)

        # Assert
        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main()
