# Calculator.
def cal():
  print("This is a calculator.")
  print("You choose a number, then a sign and then the last number. The signs can be plus, minus, times, **, division and modulos.")
  
  num1 = int(input("Number 1 --> "))
  sign = input("Sign --> ")
  num2 = int(input("Last number --> "))
  
  if sign == "+" or sign == "-" or sign == "*" or sign == "/" or sign == "%":
    print("You want to calculate %s %s %s." % (num1, sign, num2))
  
  if sign == "+":
      print(add(num1,num2))
      
  elif sign == "-":
        print(sub(num1,num2))
        
  elif sign == "*":
    print(mul(num1,num2))
	
  elif sign == "/":
	  print(div(num1,num2))

  elif sign == "%":
	  print(mod(num1, num2))
    
  else:
	  print("Something went wrong.")

def add(x,y):
    """Add function"""
    return x + y

def sub(x,y):
    """Subtract function"""
    return x - y

def div(x,y):
    if y == 0:
        raise ValueError('Cannot divide by zero')
    #Divide function
    return x / y

def mul(x,y):
    #"""Multiply function"""
    return x * y

def mod(x,y):
    #"""Modulus function"""
    return x % y
