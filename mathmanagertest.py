import unittest
from mathmanager import MathManager

class mathmanagertest(unittest.TestCase):
	def testAdd(self):
		math = MathManager()
		self.assertEqual(math.add(0, 3), 3)

	def testSubtract(self):
		math = MathManager()
		self.assertEqual(math.subtract(0, 3), -3)

	def testMultiply(self):
		math = MathManager();
		self.assertEqual(math.multiply(0, 3), 0)

	def test_calculate_degree_classification(self):
		math = MathManager()
		self.assertEqual(math.calculate_degree_classification([40, 40, 40, 10, 10]), "fail")
		self.assertEqual(math.calculate_degree_classification([40, 40, 40, 40, 10]), "3rd")
		self.assertEqual(math.calculate_degree_classification([100, 35, 60, 45, 62]), "2:1")
		self.assertEqual(math.calculate_degree_classification([80, 35, 50, 45, 62]), "2:2")
		self.assertEqual(math.calculate_degree_classification([0, 70, 70, 70, 70]), "1st")
