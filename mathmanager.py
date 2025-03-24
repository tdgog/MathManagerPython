from sympy.strategies.core import switch


class MathManager:

	def add(self, a, b):
			return a+b

	def subtract(self, a, b):
			return a-b

	def multiply(self, a, b):
			return a*b

	def calculate_monthly_interest(self, money: float, years: int):
		pass

	def calculate_tax_paid(self, income: float) -> float:
		taxable = income - 12570

		# No taxable income, therefore no taxes paid
		if taxable <= 0:
			return 0

		# If they make less than the threshold for 40%, tax the full income at 20%
		if taxable <= 50270:
			return taxable * 0.2

		# If they make less than the threshold for 45%, tax the first 50270 at 20% and the rest at 40%
		if taxable <= 125140:
			return 50270 * 0.2 + (taxable - 50270) * 0.4

		# If they make more than the threshold for 45%, tax the first 50270 at 20%, the next 74870 at 40%,
		# and the rest at 45%
		return 50270 * 0.2 + (125140 - 50270) * 0.4 + (taxable - 50270 - 125140) * 0.45

	def calculate_degree_classification(self, marks: list[int]) -> str:
		marks.remove(min(marks))
		average_mark = sum(marks) / len(marks)

		if average_mark < 40:
			return "fail"
		elif average_mark < 50:
			return "3rd"
		elif average_mark < 60:
			return "2:2"
		elif average_mark < 70:
			return "2:1"
		return "1st"
