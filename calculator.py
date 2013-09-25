import arithmetic

def main():
    #import arithmetic.py
    #loop while first user input is not q
    #get user input -did
    #split user input into tokens
    #check first token to find out operation
    #if else statements to determine next steps
    #execute operation and (return) and print

    while True:
        inp = raw_input("> ")
        tokens = inp.split(" ")
        if len(tokens) > 1:
            x = int(tokens[1])
        if len(tokens) > 2:
            y = int(tokens[2])

        if tokens[0] == "+":
            answer = arithmetic.add(x, y)
        elif tokens[0] == "-":
            answer = arithmetic.subtract(x, y)
        elif tokens[0] == "*":
            answer = arithmetic.multiply(x, y)
        elif tokens[0] == "/":
            answer = arithmetic.divide(x, y)
        elif tokens[0] == "square":
            answer = arithmetic.square(x)
        elif tokens[0] == "cube":
            answer = arithmetic.cube(x)
        elif tokens[0] == "pow":
            answer = arithmetic.power(x, y)
        elif tokens[0] == "mod":
            answer = arithmetic.mod(x, y)
        elif tokens[0] == "q":
            break
        else:
            print "This is an invalid expression."
        
        if len(tokens) > 1:
            print answer
