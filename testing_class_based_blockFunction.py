from class_based_blockFunction import ClosestBlock
import unittest


class DemoTesting(unittest.TestCase):
    def test_func_1(self):
        obj1 = ClosestBlock()
        # Arrange
        obj1.add_both(0)
        obj1.add_both(3)

        # Act
        result = obj1.checkClosestBlockForFacilities()

        # Assert
        self.assertEqual(result, 0)
    
    def test_func_2(self):
        obj2 = ClosestBlock()
        # Arrange
        obj2.add_cafe(3)
        obj2.add_cafe(9)
        obj2.add_office(1)
        obj2.add_office(7)

        # Act
        result = obj2.checkClosestBlockForFacilities()

        # Assert
        self.assertEqual(result, 2)
    
    def test_func_3(self):
        obj3 = ClosestBlock()
        # Arrange
        obj3.add_cafe(3)
        obj3.add_office(10)

        # Act
        result = obj3.checkClosestBlockForFacilities()

        # Assert
        self.assertEqual(result, 6)

    def test_func_4(self):
        obj4 = ClosestBlock()
        # Arrange

        # Act
        result = obj4.checkClosestBlockForFacilities()

        # Assert
        self.assertEqual(result, False)


if __name__ == '__main__':
    unittest.main()
