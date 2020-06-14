import vectorlength
import lineslope
import degrees
import vector
import calculator
import squareroot

# if function.
def t_if():
  if choice == "calculator":
    calculator.cal()

  elif choice == "square root":
    squareroot.sqr()

  elif choice == "vector length":
    vectorlength.length_vector()

  elif choice == "line slope":
    lineslope.calc()
  
  elif choice == "degrees":
    degrees.deg()
  
  elif choice == "vector":
    vector.vector()

  else:
    print("Something went wrong. Make sure you spelled correctly.")


print("Enter what type of calculations you want.")
print("You can choose 'Square root', 'Vector length', 'Calculator', 'Vector', 'Degrees' and 'Line slope'.")

choice = input("Enter here: ").lower()

if len(choice) > 0:
  t_if()

else:
  print("Something went wrong. Make sure you spelled it correct.")