#Custom Calculator
#Here I define the function 
def division(x, y):
    #Perform calculation (division)
    answer = int(x) / int(y)
    #Print out the answer for the user
    print(answer)

#In lines 8 and 9 I ask for an input from the user
x = input("Enter the first number:")
y = input("Enter the second number:")
#In line 11 I call the function and pass x and y as parameters 
division(x, y)