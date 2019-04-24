class Calculator:
    print('Welcome to my simple calculator!')
    def __init__(self):
        self.numbers = True
        self.operators = True

    def addition(self):
        result = self.input_num_1 + self.input_num_2
        return 'Your result is: ' + str(result)

    def subtract(self):
        result = self.input_num_1 - self.input_num_2
        return 'Your result is: ' + str(result)

    def multiply(self):
        result = self.input_num_1 * self.input_num_2
        return 'Your result is: ' + str(result)

    def divide(self):
        result = self.input_num_1 / self.input_num_2
        return 'Your result is: ' + str(result)

    def user_input_calculator(self):
        # self.input_num_1 = input_num_1
        # self.input_num_2 = input_num_2
        # self.operation = operation

        while True:
            self.input_num_1 = int(input('Enter your first number: '))
            self.input_num_2 = int(input('Enter your second number: '))
            self.operation = input('What would you like to do to the numbers? (Add, Subtract, Multiply or Divide only): ')

            #Add
            if self.operation.strip().capitalize() == 'Add':
                print(self.addition())

            #Subtract
            elif self.operation.strip().capitalize() == 'Subtract':
                self.subtract()

            #Multiply
            elif self.operation.strip().capitalize() == 'Multiply':
                self.multiply()

            #Divide
            elif self.operation.strip().capitalize() == 'Divide':
                self.divide()
            else:
                print('Please state one of the specified options (Add, Subtract, Multiply or Divide)')


calculate = Calculator()
calculate.user_input_calculator()