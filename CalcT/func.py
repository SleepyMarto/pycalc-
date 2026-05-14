# glavni funkcii
class Functions:
    def __init__(self, equation_label):
        self.equation_text = ""
        self.equation_label = equation_label

    def button_press(self, num):
        self.equation_text += str(num)
        self.equation_label.set(self.equation_text)

    def equals(self):
        try:
            total = str(eval(self.equation_text))
            self.equation_label.set(total)
            self.equation_text = total

        except ZeroDivisionError:
            self.equation_label.set("can't divide by 0")
            self.equation_text = ""

    def clear(self):
        self.equation_text = ""
        self.equation_label.set("")