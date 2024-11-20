def main(): #main definition
    
    a = float(input("Enter a number"))
    b = float(input("Enter another number"))

def add(a,b) : #add definition
    output1 = a + b
    return output1

def subtract(a,b) : #subtract definition
    output2 = a - b
    return output2

def multiply(a,b) : #multiply definition
    output3 = a * b
    return output3

def divide(a,b) : #divide definition
    output4 = a / b
    return output4

if __name__ == "__main__" : #determines whether currect script is being run as main program or if it's being imported as a module into another script
    main()
