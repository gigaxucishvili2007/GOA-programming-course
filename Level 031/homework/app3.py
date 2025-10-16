'''3) მომხარებელს შემოატანინეთ ორი რიცხვი და შექმენი ფუნქცია რომელიც შეადარებს რომელია უფრო დიდი'''

num1 = int(input("Enter the first number :"))
num2 = int(input("Enter the second number :"))
if num1 > num2:
  print(f"first number is bigger than second number {num1}")
elif num1 < num2:
  print(f"second number is bigger than first number {num2}")
else:
  print("numbers are equal")