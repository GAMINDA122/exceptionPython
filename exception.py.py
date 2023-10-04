try:
    num1 = int(input("Enter your 1st number : "))
    num2 = int(input("Enter your 2nd number : "))
    print("Answer is ",num1/num2)

except Exception as e:
    print("Something went wrong in your enter values --> ",e)

print("Bye! Thank you for your using ?")