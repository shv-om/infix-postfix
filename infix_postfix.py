"""
Infix to Postfix conversion

-by Ulegend

"""

class Convert:
	"""docstring for Conversion"""
	def __init__(self, characters):
		self.characters = characters
		self.stack = []
		self.output = []
		self.precedence = {'+': 1, '-': 2, '*':3, '/':4, '^':5}

	def checkprecedence(self, ch):
		if self.stack == [] or self.stack[-1] == '(':
			return True
		else:
			temp = self.stack[-1]
			if self.precedence[ch] < self.precedence[temp]:
				return False
			else:
				return True

	def infix_postfix(self, expression):
		for i in expression:
			if i.isalnum() == True:
				self.output.append(i)

			elif i == '(':
				self.stack.append(i)

			elif i == ')':
				try:
					pop = self.stack.pop()
					while pop != '(':
						self.output.append(pop)
						#print("pop:",pop)
						pop = self.stack.pop()
				except Exception as e:
					print("Parenthesis Mismatched")
					return

			else:
				if self.checkprecedence(i) == True:
					self.stack.append(i)
				else:
					while self.stack != []:
						temp_pop = self.stack.pop()
						if temp_pop == '(' or temp_pop == ')':
							break
						elif self.precedence[i] <= self.precedence[temp_pop]:
							self.output.append(temp_pop)
						else:
							self.stack.append(temp_pop)
							break
						#print("temp:",temp_pop)

					self.stack.append(i)
			#print(self.stack)

		while self.stack != []:
			self.output.append(self.stack.pop())

		if '(' in self.output:
			print("Parenthesis Mismatched")
			return

		print("".join(self.output))


exp = input("Enter Here: ")
obj = Convert(len(exp))
obj.infix_postfix(exp)

		
