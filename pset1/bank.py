def main():
    g = input("Greeting: ").strip().lower()
    if greeting(g) == "hello":
        print("$0")
    elif greeting(g) == "h":
        print("$20")
    else:
        print("$100")

def greeting(n):
    if n.startswith("hello"):
        return "hello"
    elif n.startswith("h"):
        return "h"
    else:
        return "other"
    
main()
