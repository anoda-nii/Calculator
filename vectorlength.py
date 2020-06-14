# Vector length.
def length_vector():
  print("Enter the length of the x coordinate and the length of the y coodinate.")
  x, y = input("x and y coordinate: ").split()
  print("Your vector is (%s, %s)" % (x, y))
  
  from math import sqrt
  length = sqrt(int(x)**2) + sqrt(int(y)**2)
  print("The length of the vector is %s." % (length))