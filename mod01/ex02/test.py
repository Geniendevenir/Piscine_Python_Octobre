from vector import Vector

def main():
	print("I - TEST WRONG CONSTRUCTOR:\n")
	print("A- Wrong Size Constructor")
	Wrong1 = Vector(-1)
	Wrong3 = Vector("test")

	print("\nB- Wrong Range Constructor")
	Wrong6 = Vector((-1))
	Wrong9 = Vector((2, 1))

	print("\nC- Wrong Column Constructor")
	Wrong11 = Vector("test")
	Wrong13 = Vector([[0.0]])
	Wrong14 = Vector([[0.0], ["test"]])
	Wrong18 = Vector([[0.0], [1.0], [2.0, 3.0]])

	print("\nD- Wrong Row Constructor")
	Wrong19 = Vector([["test"]])
	Wrong20 = Vector([[0.0]])
	Wrong21 = Vector([[0.0], ("test")])
	Wrong22 = Vector([[0.0, 1.0]])
	Wrong22 = Vector([[0.0, 1.0]])

	print("\n-------------------------------------\n")

	print("II - TEST VALID CONSTRUCTOR:\n")
	print("A- Valid Size Constructor")
	Valid1 = Vector(3)
	print(Valid1)
	Valid1 = Vector(5)
	print(Valid1)

	print("\nB- Valid Size Range Constructor")
	Valid2 = Vector((2, 5))
	print(Valid2)
	Valid2 = Vector((10, 16))
	print(Valid2)

	print("\nC- Valid Column Constructor")
	Valid3 = Vector([[0.0], [1.0]])
	print(Valid3)
	Valid4 = Vector([[0.0], [1.0], [2.0]])
	print(Valid4)

	print("\nD- Valid Row Constructor")
	Valid5 = Vector([[42.0, 53.0, 2.0]])
	print(Valid5)

	print("\n-------------------------------------\n")

	print("III - TEST DOT PRODUCT:\n")
	Dot1 = Vector([[1.0, 2.0, 3.0]])
	Dot2 = Vector([[3.0, 2.0, 1.0]])
	Dot3 = Vector([[10.0, 1.0, 2.0, 10.0]])
	Dot4 = Vector([[1.0, 1.0, 1.0, 10.0]])

	Dot5 = Vector([[1.0], [2.0], [3.0]])
	Dot6 = Vector([[3.0], [2.0], [1.0]])
	Dot7 = Vector([[10.0], [1.0], [2.0], [10.0]])
	Dot8 = Vector([[1.0], [1.0], [1.0], [10.0]])

	print("A - INVALID DOT PRODUCT:")
	print(Dot1.dot(Dot3))
	print(Dot1.dot(Dot5))

	print("\nB - VALID COLUMN DOT PRODUCT:")
	print(Dot5.dot(Dot6))
	print(Dot7.dot(Dot8))

	print("\nC - VALID ROW DOT PRODUCT:")
	print(Dot1.dot(Dot2))
	print(Dot3.dot(Dot4))

	print("\n-------------------------------------\n")

	print("IV - TEST TRANSFORM VECTOR:\n")
	Col1 = Vector([[1.0], [2.0], [3.0]]) 
	print(Col1.T())

	Row2 = Vector([[1.0, 2.0, 3.0]]) 
	print(Row2.T())

	print("\n-------------------------------------\n")

	print("V - TEST CALCUL VECTOR:\n")
	print("A - TEST __add__ and __radd__:")
	print(Dot1 + Dot2)
	print(Dot1 + 5)
	print(5 + Dot1)
	print(Dot5 + Dot6)
	print(Dot5 + 5)
	print(5 + Dot5)

	print("\nB - TEST __sub__ and __rsub__:")
	print(Dot1 - Dot2)
	print(Dot1 - 5)
	print(5 - Dot1)
	print(Dot5 - Dot6)
	print(Dot5 - 5)
	print(5 - Dot5)

	print("\nC - TEST __truediv__ and __rtruediv__:")
	print(Dot1 / 5)
	#print(5 / Dot1)
	print(Dot5 / 5)
	#print(5 / Dot5)

	print("\nC - TEST __mul__ and __rmul__:")
	print(Dot1 * 5)
	print(5 * Dot1)
	print(Dot5 * 5)
	print(5 * Dot5)


if __name__ == "__main__":
	main()