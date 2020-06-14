
# Square root function.
def sqr():
  from math import sqrt
  answer = input("Enter a number you want to find the square root of: ")
  def cals():
    result = sqrt(int(answer))
    print("The result is %s." % (result))

  print("We will now find the square root of you number.")

  if len(answer) > 0 and answer.isnumeric:
    cals()
  
  elif answer.isalpha:
    print("You can only use numbers.")

  elif len(answer) == 0:
    print("You must write something.")
  
  else:
    print("Something went wrong.")