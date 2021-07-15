# triangleareabycoordinates(x1, y1, x2, y2, x3, y3)[5pts]
# Write the function triangleareabycoordinates(x1, y1, x2, y2, x3, y3) that takes 6 int or float
# values that represent the three points (x1,y1), (x2,y2), and (x3,y3), and returns as a float the
# area of the triangle formed by those three points. Hint: you should make constructive use of
# the triangleArea function you just wrote above.

def triangleareabycoordinates(x1, y1, x2, y2, x3, y3):
	# your code goes here
	# a = fun_distance(x1,y1,x2,y2)
	# b = fun_distance(x2,y2,x3,y3)
	# c = fun_distance(x1,y1,x3,y3)

	# s = (a+b+c)//2

	# Area = (s(s-a)(s-b)(s-c))**(1/2)
	# return int(Area)
	Area = abs((0.5)*(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2)))
	return Area
	


# def fun_distance(x1, y1, x2, y2):
# 	# your code goes here
# 	leng = ((x2-x1)**2 + (y2-y1)**2)
# 	dist = (leng)**(1/2)
	
# 	return int(dist)