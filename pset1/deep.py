def main():
    x  = input("What is the answer to the Great Question of Life, the Universe, and Everything? ").strip().lower()
    if answer(x):
        print("Yes")
    else:
        print("No")

def answer(x):
    match x:
        case "42" | "forty-two" | "Forty Two":
            return True
        case _:
            return False
main()
