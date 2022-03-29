class Calculator:

    def __init__ (self,input1,input2):
        self.input1= input1
        self.input2= input2

    def adder(self):
        return self.input1+self.input2
    
    def subtractor(self):
        return self.input1-self.input2

    def multiplier(self):
        return self.input1*self.input2
    
    def divider(self):
        return self.input1/self.input2
    
    def clear(self):
        self.input1= int(input("\nEnter First Number: "))
        self.input2= int(input("Enter Second Number: "))
        return ""

def main():
#get user input for two 2 numbers
    input1= int(input("Enter First Number: "))
    input2= int(input("Enter Second Number: "))

#Create an object for calculator class
    calculate = Calculator(input1, input2)

    option = 1

    while option!=7:
        print("\n1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. All Operations")
        print("6. Reset")
        print("7. Shutdown")
        
        option=int(input("Enter choice: "))

        if option==1:
            print("Result: ",calculate.adder())
        elif option==2:
            print("Result: ",calculate.subtractor())
        elif option==3:
            print("Result: ",calculate.multiplier())
        elif option==4:
            print("Result: ",calculate.divider())
        elif option==5:
            print("ADD Result: ",calculate.adder())
            print("SUBTRACT Result: ",calculate.subtractor())
            print("MULTIPLY Result: ",calculate.multiplier())
            print("DIVIDE Result: ",calculate.divider())
        elif option==6:
            print(calculate.clear())
        elif option==7:
            print("Shutting Down!")
        else:
            print("Invalid Option")

    print()

if __name__ == "__main__":
    main()