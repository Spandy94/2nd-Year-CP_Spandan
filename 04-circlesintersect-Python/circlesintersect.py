# Write the function circlesIntersect(x1, y1, r1, x2, y2, r2) 
# that takes 6 numbers (ints) -- x1, y1, r1, x2, y2, r2 -- 
# that describe the circle centered at (x1,y1) with radius r1, 
# and the circle centered at (x2,y2) with radius r2, and returns True 
# if the two circles intersect and False otherwise.

def fun_circlesintersect(x1, y1, r1, x2, y2, r2):
	# your code goes here
	return (fun_distance(x1,y1,x2,y2) <= (r1+r2)) 

def fun_distance(x1, y1, x2, y2):
	# your code goes here
	leng = ((x2-x1)**2 + (y2-y1)**2)
	dist = (leng)**(1/2)
	
	return int(dist)
