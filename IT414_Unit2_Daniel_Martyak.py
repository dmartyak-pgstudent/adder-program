##IT414 Unit 2 Assignment Daniel Martyak

##This is the function to add two separate numebrs together
def adder():
    num_1 = input("Enter the first numeric value: ")
    num_2 = input("Enter the second numeric value: ")
    sum = int(num_1) + int(num_2)
    print("The Sum is: ", sum)

##This is the unit test that, when run, will automatically test the method
##created with the first function
    if input("Do you want to test the variables? Y or N:") == 'Y':
        def unit_test():
            if num_1.isnumeric():
                print("Number 1 is numeric")
            else:
                print("The first entry is not numeric")

            if num_2.isnumeric():
                print("Number 2 is numeric")
            else:
                print("The second entry is not numeric")

        unit_test()
    pass

##This is the main function to call the addition function
def main():
    adder()

#This code runs the main function to accept inputs from the user
main()


