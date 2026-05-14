from func import Functions
func = Functions()
print("Какво ще правим днес?")
print("[1] Събиране\n[2] Изваждане\n[3] Умножение\n[4] Деление\n[5] Изход")

add = ["add", "plus", "sum", "addition", "and", "+", "1"]
substract = ["substract", "minus", "difference", "subtraction", "from", "-", "2"]
multiply = ["multiply", "times", "product", "multiplication", "*", "3"]
divide = ["divide", "over", "quotient", "division", "/", "4"]
bye = ["bye", "goodbye", "exit", "quit", "5"]

res = input().lower()

if res in bye:
    print(func.gbye())
    quit()

a = float(input("Въведете първото число: "))
b = float(input("Въведете второто число: "))

if res in add:
    print(f"Резултатът е: {func.add(a, b)}")

elif res in substract:
    print(f"Резултатът е: {func.subtract(a, b)}")

elif res in multiply:
    print(f"Резултатът е: {func.multiply(a, b)}")

elif res in divide:
    print(f"Резултатът е: {func.divide(a, b)}")