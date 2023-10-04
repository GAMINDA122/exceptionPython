try:
    num1 = int(input("Enter your 1st number : "))
    num2 = int(input("Enter your 2nd number : "))
    print("Answer is ",num1/num2)

except ZeroDivisionError as e:
    print("Can't divide by zero --> ",e)

except ValueError as a:
    print("Use only integer valuse --> ",a)

except Exception as e:
    print("Something went wrong in your enter values --> ",e)

print("Bye! Thank you for your using ?")