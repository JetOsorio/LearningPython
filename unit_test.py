import  unittest

from test_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    #Tests for the test_function
    def test_first_last_name(self):
        formatted_name = get_formatted_name('bob', 'ross')
        self.assertEqual(formatted_name, 'Bob Ross')

unittest.main()