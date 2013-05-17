import unittest

from problems import *

class testing99problems(unittest.TestCase):
	
	def test_problem1_expected_list(self):
		self.a = [1,2,3]
		self.assertEqual(py1.problem(self.a), 3)
	
	def test_problem1_one_item_list(self):
		self.a = [1]
		self.assertEqual(py1.problem(self.a), 1)

	def test_problem1_empty_list(self):
		self.b = []
		self.assertEqual(py1.problem(self.b), 'The list you provided is empty.')
		
	def test_problem1_not_a_list(self):
		self.a = 'run'
		self.assertEqual(py1.problem(self.a),'The input you provided is not a list.')

# Problem 2
		
	def test_problem2_expected_list(self):
		self.a = [1,2,3] #last but one = 2
		self.assertEqual(py2.problem(self.a), 2)
	
	def test_problem2_empty_list(self):
		self.b = []
		self.assertEqual(py2.problem(self.b), 'The list you provided is empty.')
		
	def test_problem2_one_item_list(self):
		self.a = [1]
		self.assertEqual(py2.problem(self.a), 'The list you provided contains only one element.')
	
	def test_problem2_not_a_list(self):
		self.a = 'run'
		self.assertEqual(py2.problem(self.a),'The input you provided is not a list.')

# Problem 3

	def test_problem3_expected_list(self):
		self.a = 2
		self.b = [1,2,3] #self.a = 3
		self.assertEqual(py3.problem(self.a,self.b), 3)
	
	def test_problem3_non_int(self):
		self.a = [1] #not an int
		self.b = [1,2,3]
		self.assertEqual(py3.problem(self.a,self.b), 'You did not provide an int.')
		
	def test_problem3_empty_list(self):
		self.a = 3
		self.b = [] #empty list
		self.assertEqual(py3.problem(self.a,self.b), 'The list you provided contains less than ' + str(self.a) + ' elements.')
	
	def test_problem3_not_a_list(self):
		self.a = 3
		self.b = 'run'
		self.assertEqual(py3.problem(self.a,self.b),'The input you provided is not a list.')
	
	def test_problem3_one_item_list(self):
		self.a = 0
		self.b = [1]
		self.assertEqual(py3.problem(self.a,self.b),1)

# Problem 4

	def test_problem4_expected_list(self):
		self.a = [1,2,3]
		self.assertEqual(py4.problem(self.a), 3)
	
	def test_problem4_one_item_list(self):
		self.a = [1]
		self.assertEqual(py4.problem(self.a), 1)

	def test_problem4_empty_list(self):
		self.b = []
		self.assertEqual(py4.problem(self.b), 0)
		
	def test_problem4_not_a_list(self):
		self.a = 4
		self.assertEqual(py1.problem(self.a),'The input you provided is not a list.')

# Problem 5 - Reversing a list

	def test_problem5_expected_list(self):
		self.a = [1,2,3]
		self.assertEqual(py5.problem(self.a), [3,2,1])
		
	def test_problem5_not_a_list(self):
		self.a = 'run'
		self.assertEqual(py5.problem(self.a),'The input you provided is not a list.')
	
	def test_problem5_empty_list(self):
		self.b = []
		self.assertEqual(py5.problem(self.b), [])
	
	def test_problem5_one_item_list(self):
		self.a = [1]
		self.assertEqual(py5.problem(self.a),[1])

# Problem 6

	def test_problem6_is_a_palindrome(self):
		self.a = ['m','o','m']
		self.assertEqual(py6.problem(self.a), 'This list is a palindrome.')
	
	def test_problem6_not_a_palindrome(self):
		self.a = ['m','o','n']
		self.assertEqual(py6.problem(self.a), 'This list is not a palindrome.')

