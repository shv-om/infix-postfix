"""
Infix to Postfix conversion

Algorithm 
1. Scan the infix expression from left to right. 
2. If the scanned character is an operand, output it. 
3. Else, 
    1 If the precedence of the scanned operator is greater than the precedence of the operator in the stack(or the stack is empty or the stack contains a ‘(‘ ), push it. 
    2 Else, Pop all the operators from the stack which are greater than or equal to in precedence than that of the scanned operator. After doing that Push the scanned operator to the stack.
      (If you encounter parenthesis while popping then stop there and push the scanned operator in the stack.) 
4. If the scanned character is an ‘(‘, push it to the stack. 
5. If the scanned character is an ‘)’, pop the stack and output it until a ‘(‘ is encountered, and discard both the parenthesis. 
6. Repeat steps 2-6 until infix expression is scanned. 
7. Print the output 
8. Pop and output from the stack until it is not empty.

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

		