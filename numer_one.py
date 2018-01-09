def divide(num):
    print(500/num)

user = int(input("Enter the number you want to divide 500 with:"))

try:
    divide(user)

except:
    print("Zero is not allowed.")
else:
    print("The division is successful")

finally:
    divide(500)