#Vector
def vector():
  decide = input("Choose 'Vector projection', 'determinant' 'Vector degrees' or 'Dot product': ").lower()

  if decide == "vector projection":
   proj()

  elif decide == "dot product":
    dot()
  
  elif decide == "vector degrees":
    vec_deg()
  
  elif decide == "determinant":
    det()
    
# Derteminant
def det():
  a1, a2 = input("Enter a1 and a2: ").split()
  b1, b2 = input("Enter b1 and b2: ").split()
  a1 = int(a1)
  a2 = int(a2)
  b1 = int(b1)
  b2 = int(b2)
  
  determinant = (a1 * b2) - (a2 * b1)
  print("The areal area of the parallellogram is %s." % (determinant))
  lop = input("Do you want to calculate the are of the triangle -->").lower()
  
  if lop == "yes":
    result = determinant * 0.5
    print("The are area of the triangle is %s." % (result))

#Dot product
def dot():
  a1, a2 = input("Enter a1 and a2: ").split()
  b1, b2 = input("Enter b1 and b2: ").split()
  a1 = int(a1)
  a2 = int(a2)
  b1 = int(b1)
  b2 = int(b2)
  
  result = (a1 * b1) + (a2 * b2)
  print("The dot product is %s." % (result))

# Vector degrees
def vec_deg():
  from math import sqrt
  a1, a2 = input("Enter a1 and a2: ").split()
  b1, b2 = input("Enter b1 and b2: ").split()
  a1 = int(a1)
  a2 = int(a2)
  b1 = int(b1)
  b2 = int(b2)
  
  dot = (a1 * b1) + (a2 * b2)
  length = (sqrt(a1) + sqrt(a2)) * (sqrt(b1) + sqrt(b2))
  degs = dot / length
  print("The result is %s." % (degs))

#Vector proj
def proj():
  def prik_produkt():
    return (a1 * b1) + (a2 * b2)
  
  def vec_length():
    from math import sqrt
    return (sqrt(b1**2) + sqrt(b2**2))**2

  a1, a2 = input("Enter a1 and a2: ").split()
  b1, b2 = input("Enter b1 and b2: ").split()
  a1 = int(a1)
  a2 = int(a2)
  b1 = int(b1)
  b2 = int(b2)

  def res():
    one = (prik_produkt() / vec_length()) * b1
    two = (prik_produkt() / vec_length()) * b2
    print("The result is (%s, %s)." % (one, two))

  res()