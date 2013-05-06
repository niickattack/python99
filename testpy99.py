import py1
import py2
import unittest

class testing99problems(unittest.TestCase):
	
	def test_expected_list(self):
		self.a = [1,2,3]
		self.assertEqual(py1.problem(self.a), 3)

	#def test_empty_list(self):
	#	self.b = []
	#	self.c = py1.problem(self.b)
	#	self.assertEqual(self.c, 'There is a problem with the list provided, it may be empty.')
		
if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(testing99problems)
	unittest.TextTestRunner(verbosity=2).run(suite)