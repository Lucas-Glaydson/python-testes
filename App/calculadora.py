class Calculator:
    def __init__(self, first_value, second_value):
        self.first_value = first_value
        self.second_value = second_value

    def add(self):
        return self.first_value + self.second_value

    def subtract(self):
        return self.first_value - self.second_value

    def multiply(self):
        return self.first_value * self.second_value

    def dive(self):
        return self.first_value / self.second_value
