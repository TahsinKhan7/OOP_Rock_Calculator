class Calculator:
    def __init__(self):
        self.numbers = True
        self.operators = True
        self.calculator_ready = True

    def user_input(self, input_num_1, input_num_2, operation):
        self.input_num_1 = input_num_1
        self.input_num_2 = input_num_2
        self.operation = operation


    def Addition(self, add):
        self.add = add
    def Subtraction(self, subtract):
        self.subtract = subtract
    def Multiplication(self, multiply):
        self.multiply = multiply
    def Division(self, divide):
        self.divide = divide

calculate = Calculator()
calculate.user_input()

