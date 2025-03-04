import re

TOKEN_TYPES = {
    "NUMBER": r"\d+",
    "VAR": r"varasaurus",
    "EQUALS": r"=",
    "PLUS": r"triceraplus",
    "MINUS": r"velociminus",
    "MULTIPLY": r"stegomult",
    "DIVIDE": r"tyrannidiv",
    "IDENTIFIER": r"[a-zA-Z_][a-zA-Z0-9_]*",
    "WHITESPACE": r"\s+",
}

variables = {}

def lexer(code):
    tokens = []

    while code:
        match = None
        for token_type, pattern in TOKEN_TYPES.items():
            regex = re.compile(pattern)
            match = regex.match(code)
            if match:
                if token_type != "WHITESPACE":
                    tokens.append((token_type, match.group(0)))
                code = code[match.end():]
                break
        if not match:
            raise Exception(f"Unknown character: {code[0]}")
    return tokens

def eval_exp(tokens):
    if not tokens:
        return None
    
    # return the number, if all we have is a number
    if len(tokens) == 1 and tokens[0][0] == "NUMBER":
        return int(tokens[0][1])
    
    expression = ""
    for token_type, value in tokens:
        if token_type == "NUMBER":
            expression += value
        elif token_type == "IDENTIFIER":
            if value in variables:
                expression += str(variables[value])
            else:
                raise Exception(f"Undefined variable: {value}")
        elif token_type == "PLUS":
            expression += "+"
        elif token_type == "MINUS":
            expression += "-"
        elif token_type == "MULTIPLY":
            expression += "*"
        elif token_type == "DIVIDE":
            expression += "/"
    
    # compute the expression and return
    return eval(expression)


def interpret(code):
    tokens = lexer(code)

    # variable assignement
    if len(tokens) >= 3 and tokens[0][0] == "VAR" and tokens[1][0] == "IDENTIFIER" and tokens[2][0] == "EQUALS":
        var_name = tokens[1][1]
        value = eval_exp(tokens[3:])
        variables[var_name] = value
        return f"{var_name} = {value}"

    return eval_exp(tokens)

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
