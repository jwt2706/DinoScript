import re

TOKENS = {
    "NUMBER": r"\d+",
    "IDENTIFIER": r"[a-zA-Z_][a-zA-Z0-9_]",
    "VAR": r"Varasaurus",
    "EQUALS": r"=",
    "PLUS": r"Triceraplus",
    "MINUS": r"Velociminus",
    "MULTIPLY": r"Stegomult",
    "DIVIDE": r"Tyrannidiv",
    "WHITESPACE": r"\s+",
}

def lexer(code):
    pass

def eval_exp(tokens):
    pass

def interpret(user_input):
    return "Invalid syntax."


print("DinoPy is running.")
while True:
    user_input = input("🦖 >>> ")
    if user_input == "exit":
        break
    try:
        result = interpret(user_input)
        if result is not None:
            print(result)
    except Exception as e:
        print("Error:", e)
