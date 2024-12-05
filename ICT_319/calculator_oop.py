class Calculator:
    def __int__(self):
        self.operand1=None
        self.operand2=None
        self.operator=None







    def ask_user_input(self):
    # Get first operand
        self.operand1 = self.ask_user_float_input("Enter the first operand: ")

    # Get operator
        self.operator = input("Enter an operator (+, -, *, /, **): ")

    # Get second operand
        self.operand2 = self.ask_user_float_input("Enter the second operand: ")


    @staticmethod
    def ask_user_float_input(prompt):
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def calculate(self):
    # Perform the operation based on the operator
        match self.operator:
            case '+':
                return self.operand1 + self.operand2
            case '-':
                return self.operand1 - self.operand2
            case '*':
                return self.operand1 * self.operand2
            case '/':
                if self.operand2 == 0:
                    print("Error: Division by zero is undefined.")
                    return None
                return self.operand1 / self.operand2
            case '**':
                return self.operand1 ** self.operand2
            case _:
                print("Invalid  operator.")
                return None

    def display_result(self,result):
        print(f"{self.operand1} {self.operator} {self.operand2} = {result}")

def main():
    calculator=Calculator()
    calculator.ask_user_input()
    result=calculator.calculate()
    calculator.display_result(result)

# Run the program
main()
