import classStack as cs
from Var import *
from Errors import *
line = ["n", "VAR", "INT", "10"]
stacks = {"i":cs.Stack(10)}
variables = {"j":Variable("int", 10)}


def parse_varible(line,stacks, variablesDict):
    
    var_name = line[0]
    if var_name in stacks:
        try:
            raise CannotOverWriteStack(f"{var_name} already exists as a stack")
        except CannotOverWriteStack as COWS:
            print(COWS)
    elif var_name in variablesDict:
        try:
            raise VariableAlreadyExists(f"{var_name} already exsits")
        except VariableAlreadyExists as VAE:
            print(VAE)
    
    var_type = line[2]
    var_val = line[3:][0]
    return (var_name, Variable(var_type, var_val))
    

def parseMiniupVars(line, stacks, variablesDict):
    var_name = line[0]
    if var_name not in variablesDict:
        try:
            raise VariableDoesntExist(f"{var_name} doesn't exist")
        except VariableDoesntExist as VDE:
            print(VDE)
    match (n:=line[1].upper()):
        case "ADD":
            match variablesDict[var_name].type:
                case "INT":
                    if type(line[-1]) is int:
                        variablesDict[var_name].value += line[-1]
                        print(variablesDict[var_name].value) 
                    elif type(line[-1]) is str:
                        try:
                            raise TypeError(f"can't add an int to a string")
                        except TypeError as TE:
                            print(TE)
                case "STRING":
                    if type(line[-1]) is int:
                        try:
                            raise TypeError(f"can't add an int to a string")
                        except TypeError as TE:
                            print(TE)
                    elif type(line[-1]) is str:
                        variablesDict[var_name].value += line[-1]
                        print(variablesDict[var_name].value)
        case "SUB":
            match variablesDict[var_name].type:
                case "INT":
                    if type(line[-1]) is int:
                        variablesDict[var_name].value -= line[-1]
                        print(variablesDict[var_name].value)
                    elif type(line[-1]) is str:
                        try:
                            raise TypeError("Can't subtract a string from an int")
                        except TypeError as TE:
                            print(TE)
                case "STRING":
                    try:
                        raise TypeError("can't subract from a string")
                    except TypeError as TE:
                        print(TE)
        case _:
            try:
                raise InvalidOperater(f"can't use {line[1].upper()}")
            except InvalidOperater as IO:
                print(IO)
def parse(idxInlist, section, times,variablesDict):
    counter = 0
    return_code =[]
    
    for line in section:
        command_word = line[0]
        if command_word == "END":
            break
        counter +=1
    for i in repeatedSection:
        print(i)
    repeatedSection = section[1:counter]
    return [i for i in repeatedSection*times]
if __name__ == "__main__":
    vname, variable = parse_varible(line, stacks, variables)
    variables[vname] = variable
    line = ["a", "VAR", "INT", "10"]
    vname, variable = parse_varible(line, stacks, variables)
    variables[vname] = variable

    line = ["b", "VAR", "STRING", "10"]
    vname, variable = parse_varible(line, stacks, variables)
    variables[vname] = variable


    line = ["a", "ADD", 10]
    parseMiniupVars(line, stacks, variables)
    