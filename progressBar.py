# coding=utf-8

class progressBar():
	def __init__(self,deno):	#nume=分子 deno=分母
		self.deno = deno

	def barCalc(self,nume):
		self.nume = nume

		percentage = int(self.nume * 100 / self.deno)
		bar = "#" * int(percentage/10) + " " * (10-int(percentage/10))
		print("\r{0}% [{1}]".format(percentage, bar), end="")

		if self.nume == self.deno:
			print("\n")