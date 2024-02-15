"""
    Author: AaronTook (https://AaronTook.github.io)
    File Last Modified: 2/14/2024
    File Name: app.py
    Project Name: f_x
"""

def f_x(f, x): # Evaluate f(x).
    split_chars = ['+', '-', '*', '/']
    terms = []
    operators = []
    current_term = ""
    term_start = 0
    if f.startswith("-"):
        f = "0" + f
    for i in range(len(f)):
        if f[i] in split_chars:
            terms.append(f[term_start : i].strip())
            term_start = i
            operators.append("+")#(f[i])
    terms.append(f[i : ].strip())
    for term in terms:
        evaluate_x_term(term, x)
    string_f = ""
    operators.append("")
    
    
    for i in range(len(terms)):
        string_f += (evaluate_x_term(terms[i], x) + operators[i])
    return eval(string_f)

def evaluate_x_term(term, x): # Evaluate an individual term.
    if "^" in term:
        for i in range(len(term)):
            split_chars = ['+', '-', '*', '/']
            if term[i] == "^":
                if term[0] in split_chars:
                    new_term = term[1:i] + 'x' * (int(term[i+1:])-1)
                else:
                    new_term = term[:i] + 'x' * (int(term[i+1:])-1)
                break
        term = new_term
    if term[0] == "x":
        term = "1" + term
    return str(eval(term.replace("x", f"*{x}")))

if __name__== "__main__":
    user_f_x = input("f(x) = ")
    user_x = input("x = ")
    try:
        print(f"f({user_x}) = {f_x(user_f_x, user_x)}")
    except:
        print("Invalid f(x) or unexpected crash.")
        