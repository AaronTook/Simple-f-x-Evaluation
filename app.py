"""
    Author: AaronTook (https://AaronTook.github.io)
    File Last Modified: 2/18/2024
    File Name: app.py
    Project Name: f_x
"""

def f_x(f, x):
    split_chars = ['+', '-', '*', '/']
    
    # Format based on first term and remove whitespace.
    if not f.strip().startswith("-"):
        f = "+" + f
    f = "0" + f.strip()
    f = f.replace(" ", "")
    
    # Split into terms based on split_chars.
    terms = []
    operators = []
    start_of_term = 0
    for i in range(len(f)):
        char = f[i]
        if char in split_chars:
            terms.append(f[start_of_term : i])
            start_of_term = i+1
            operators.append(char)
    
    terms.append(f[start_of_term  : ])
    
    # Evaluate the equation terms and calculate the final answer.
    number_of_terms = len(terms)
    string_to_eval = ""
    for i in range(number_of_terms): # Iterate through each term and operator.
        string_to_eval += evaluate_x_term(terms[i], x)
        if i !=  number_of_terms-1:
            string_to_eval += operators[i]
        else:
            return eval(string_to_eval)

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
    # Run a simple input for the program demo.
    user_f_x = input("f(x) = ")
    user_x = input("x = ")
    try:
        print(f"f({user_x}) = {f_x(user_f_x, user_x)}")
    except:
        print("Invalid f(x) or unexpected crash.")
        
    