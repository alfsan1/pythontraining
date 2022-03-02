## create a zero division error
## 20 febrero 2022

## we are going to divide a 0, example

# print(5/0)

## we cannot divide by zero

## how can we try this, an except block, to try to see if it work

try:
    print(5/0)
except ZeroDivisionError:
    print("you can't divide by zero")

print("Select another number")

## exception with else 
## this is in order to handle errors in blocks, and that the program doesn't stop if there is an error. 

## we're creating a division machine where you put two numbers. and the system will divide the two numers, all while in a loo
## user will use Q to quit and get out of the program

print("please enter two numbers to be divided")
print("use Q to quite program")

while True:
    number1 = input("Select First number ")
    if number1 == "q":
        break
    number2 = input("Select Second number ")
    if number2 == "q":
        break
#line 36 is the one that produces the error when divided by 0, so that has to have the exception code for error handling
    try:
        division = int(number1)/int(number2)
    except ZeroDivisionError:
        print("ERROR, Can't divide by zero")
    except ValueError:
        print("ERROR, you have to use numbers")
    else:
        print("the result is " + str(division) )

