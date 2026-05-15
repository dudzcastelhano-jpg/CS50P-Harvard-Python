def main():
    expression = input("Expression ").strip()
    x, y, z = expression.split(" ")
    
    n1 = float(x)
    n2 = float(z)
    
    print(f"{calculate(n1, y, n2):.1f}")

def calculate(n1, operator, n2):
    match operator:
        case "+":
            return n1 + n2
        case "-":
            return n1 - n2
        case "*":
            return n1 * n2
        case "/":
            if n2 == 0:
                return "Error"
            return n1 / n2
        case _:
            return "Invalid operator"

main()