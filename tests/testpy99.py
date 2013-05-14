import unittest

from problems import *

class testing99problems(unittest.TestCase):
	
	def test_problem1_expected_list(self):
		self.a = [1,2,3] #last = 3
		self.assertEqual(py1.problem(self.a), 3)

	def test_problem1_empty_list(self):
		self.b = []
		self.assertEqual(py1.problem(self.b), 'The list you provided is empty.', )
		
	def test_problem1_not_a_list(self):
		self.a = 'run'
		self.assertEqual(py1.problem(self.a),'The input you provided is not a list.', )
		
#	def test_problem2_expected_list(self):
#		self.a = [1,2,3] #last but one = 2
#		self.assertEqual(py2.problem(self.a), 2)
	
#	def test_problem2_empty_list(self):
#		self.b = []
#		self.c = py2.problem(self.b)
#		self.assertEqual(self.c, 'The input you provided is not a list.', )
		
		
