import unittest
from dow_calculator import dow_datetime_method, dow_doomsday_computer, dow_doomsday_human

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.dates = ['0001-01-03','1599-02-28','1904-02-29','2022-01-31','9999-12-31']

    def test_dow_datetime_method(self):
        actual = [dow_datetime_method(i) for i in self.dates]
        expected = [
            'Wednesday', 
            'Sunday', 
            'Monday', 
            'Monday', 
            'Friday'
        ]

        self.assertEqual(expected, actual, 'dow_datetime_method has unexpected outputs')
    
    def test_dow_doomsday_computer(self):
        actual = [dow_doomsday_computer(i) for i in self.dates]
        expected = [
            'Wednesday', 
            'Sunday', 
            'Monday', 
            'Monday', 
            'Friday'
        ]

        self.assertEqual(expected, actual, 'dow_doomsday_computer has unexpected outputs')

    def test_dow_doomsday_human(self):
        actual = [dow_doomsday_human(i) for i in self.dates]
        expected = [
            'Wednesday', 
            'Sunday', 
            'Monday', 
            'Monday', 
            'Friday'
        ]

        self.assertEqual(expected, actual, 'dow_doomsday_human has unexpected outputs')

if __name__ == '__main__':
    unittest.main()