# Calculator by Mazaher
print(
  "Following Operations can be solved:\n\n1.Addition\n\n2.Subtraction\n\n3.Multiplication\n\n4.Division"
)
a = int(input("\nEnter value of a\n"))
b = int(input("\nEnter value of b\n"))
ans = input("Which operation do you want to perform?\n")
if (ans == "1"):
    print("Addition =",a + b)
elif (ans == "2"):
    print("Subtraction =",a - b)
elif (ans == "3"):
    print("Multiplication =",a * b)
elif (ans == "4"):
    print("Division =",a / b)
