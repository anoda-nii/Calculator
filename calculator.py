# Calculator.
def cal():
  print("This is a calculator.")
  print("You choose a number, then a sign and then the last number. The signs can be plus, minus, times, **, division and modulos.")
  
  num1 = int(input("Number 1 --> "))
  sign = input("Sign --> ")
  num2 = int(input("Last number --> "))
  
  if sign == "+" or sign == "-" or sign == "*" or sign == "/":
    print("You want to calculate %s%s%s." % (num1, sign, num2))
  
  if sign == "+":
      result = int(num1) + int(num2)
      print("The result is %s." % (result))
      return result
      
  elif sign == "-":
        result = int(num1) - int(num2)
        print("The result is %s." % (result))
        
  elif sign == "*":
    result = num1 * num2
    print("The result is %s." % (result))
	
  elif sign == "/":
	  result = num1 / num2
	  print("The result is %s." % (result))
	
  elif sign == "**":
	  result = num1**num2
	  print("The result is %s." % (result))

  elif sign == "%":
	  result = num1 % num2
	  print("The result is %s." % (result))
    
  else:
	  print("Something went wrong.")