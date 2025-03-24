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
		pass

	def calculate_degree_classification(self, marks: list[int]) -> str:
		if min(marks) < 0 or max(marks) > 100 or len(marks) != 5:
			raise InvalidMarkException()

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

class InvalidMarkException(Exception):
	...