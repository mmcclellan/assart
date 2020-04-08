import unittest

class TestMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('assart'.upper(), 'ASSART')

    def test_isupper(self):
        self.assertTrue('ASSART'.isupper())
        self.assertFalse('Assart'.isupper())

    def test_split(self):
        s = 'A simple s3 analytic reporting tool'
        self.assertEqual(s.split(), ['A', 'simple', 's3', 'analytic', 'reporting', 'tool'])
        with self.assertRaises(TypeError):
            s.split(6)

if __name__ == '__main__':
    unittest.main()
