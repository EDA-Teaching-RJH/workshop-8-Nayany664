def main(): #main definition
    add()
    subtract()
    multiply()
    divide()

def add(a,b) : #add definition
    output = a + b
    return output

def subtract(a,b) : #subtract definition
    output = a - b
    return output

def multiply(a,b) : #multiply definition
    output = a * b
    return output

def divide(a,b) : #divide definition
    output = a / b
    return output

if __name__ == "__main__" : #determines whether currect script is being run as main program or if it's being imported as a module into another script
    main()
