class Functions:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Не може да се дели на нула."
        else:
            return a / b

    def gbye(self):
        return "Довиждане!"