import classStack as cs
from Var import *
from Errors import *
line = ["n", "VAR", "INT", "10"]
stacks = {"i":cs.Stack(10)}
variables = {"j":Variable("int", 10)}


def parse_varible(line,stacks, variables):
    print(line)
    var_name = line[0]
    if var_name in stacks:
        try:
            raise CannotOverWriteStack(f"{var_name} already exists as a stack")
        except CannotOverWriteStack as COWS:
            print(COWS)
    elif var_name in variables:
        try:
            raise VariableAlreadyExists(f"{var_name} already exsits")
        except VariableAlreadyExists as VAE:
            print(VAE)
    
    var_type = line[2]
    var_val = line[3:][0]
    return (var_name, Variable(var_type, var_val))
    
if __name__ == "__main__":
    vname, variable = parse_varible(line, stacks, variables)
    variables[vname] = variable

