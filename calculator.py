"""
- input value 1 
- select operator (+,-,/,//,%,*)
- input value 2
- calculate
- print out the value/ solution

"""

print("============================================")
valueOne = input("Enter the first operand: ")
valueTwo = input("Enter the second operand: ")

operatorChoice = input(
"""
Kindly input the number of the operation you want: \n
 1. addition(+)
 2. subtraction(-)
 3. multiplication(*)
 4. division(/)
 5. power(**)
 6. floor division(divsion without decimals //)
 
""")

output =""
operatorChoice = int(operatorChoice)
valueOne = int(valueOne)
valueTwo = int(valueTwo)

#match case calculator
match operatorChoice:
    case 1:
        output = valueOne + valueTwo
    case 2:
        output = valueOne - valueTwo
    case 3:
        output = valueOne * valueTwo
    case 4:
        output = valueOne / valueTwo
    case 5:
        output = valueOne ** valueTwo
    case 6:
        output = valueOne // valueTwo
    case _:
        print("Syntax error!")

print("****************************************")
print(output) #standard output
print("============================================")
