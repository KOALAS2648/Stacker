import classStack as cs
import os
from Errors import *
from Var import *

def parseMiniupVars(line, variablesDict:dict):
    var_name = line[0]
    #print(f"The {line} and the type is {type(line)}")
    if var_name not in variablesDict:
        try:
            raise VariableDoesntExist(f"{var_name} doesn't exist")
        except VariableDoesntExist as VDE:
            print(VDE)
    match line[1].upper():
        case "ADD":
            match variablesDict[var_name].type:
                case "INT":
                    if type(line[-1]) is int:
                        variablesDict[var_name].value += line[-1]
                         
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
        case "SUB":
            match variablesDict[var_name].type:
                case "INT":
                    if type(line[-1]) is int:
                        variablesDict[var_name].value -= line[-1]
                        
                    elif type(line[-1]) is str:
                        try:
                            raise TypeError("Can't subtract a string from an int")
                        except TypeError as TE:
                            print(TE)
                    else:
                        print("howss")
                case "STRING":
                    try:
                        raise TypeError("can't subract from a string")
                    except TypeError as TE:
                        print(TE)
                case _:
                    print("how has this line been executed???")
        case _:
            try:
                raise InvalidOperater(f"can't use {line[1].upper()}")
            except InvalidOperater as IO:
                print(IO)

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

def parse(section, times, variablesDict):
    counter = 0
    #print(section)
    for line in section:
        command_word = line[0]
        if command_word == "END":
            break
        counter +=1
    repeatedSection = section[1:counter]
    repeatedSection = [i for i in repeatedSection if i]
    codeLines = []
    for _ in range(times):
        for line in repeatedSection:
            codeLines.append(line.copy())

    for idx, line in enumerate(codeLines):
        if (line[-1] in variablesDict):
            var_name = line[-1]
            codeLines[idx][-1] = variablesDict[var_name].value

        match line[1].upper():
            case "ADD" | "SUB":
                parseMiniupVars(line, variablesDict)
                
            case "PUSH":
                pass

        codeLines[idx] = line
    return codeLines
remove_whitespace = lambda l: [x for x in l if x]
def main(file="main.stack", option=None, clearName="posix"):
    function_list = ["PEEK", "PUSH", "STACK", "POP", "ISEMPTY", "ISFULL", "PRINT" ]
    # removes the whitespace before the code so I can make indented lines
    
    file_data_flag = False
    variableFlag = False
    match option:
        case "-fd" | "--file-data":
            file_data_flag =  True
        case "-c" | "--clear":
            os.system(clearName)
        
        case "-v" | "--variables":
            variableFlag = True
        case None:
            pass
        case _:
            try:
                raise InvalidOption("Invalid operation used")
            except InvalidOption as IO:
                print(IO)
                return 
    stacks = {}
    variables = {}
    file = open(file, "r")
    file_data = file.readlines()
    for idx, line in enumerate(file_data):
        if "\n" in line:
            file_data[idx] = line[:-1].split(" ")
        else:
            file_data[idx] = line.split(" ")
    loop_words_lower = ["loop", "end"]
    loop_words_upper = list(map(lambda x: x.upper(), loop_words_lower))
    var_use_words = ["VAR", "SUB", "ADD"]
    for idx, line in enumerate(file_data):
        if line == [""]:
            continue
        line = remove_whitespace(line)
        #print(line)
        loop_flag = False
        command_word = line[0]
        if command_word in loop_words_lower:
            try:
                raise InvalidCommand(f"{command_word} needs to be capitilized")
            except InvalidCommand as IC:
                print(IC)
                break
        
        elif command_word in stacks and line[1].upper() == "STACK":
            raise StackExist(f"stack '{command_word}' cannot be created as stack '{command_word}' already exists")
        if command_word not in loop_words_upper:
            if command_word not in stacks and line[1].upper() == "STACK":
                stacks[command_word] = cs.Stack(int(line[-1]))
                continue
        if command_word in loop_words_upper or line[1].upper() in var_use_words or command_word in variables:
            pass
        else:
            try:
                stack_name = stacks[command_word]
            except KeyError:
                try:
                    raise StackDoesNotExist(f"stack {command_word} does not exist")
                except StackDoesNotExist as SDNE:
                    print(SDNE)
                    break
        
        if command_word not in loop_words_upper:
            n = line[-1]
            if n in variables:
                        var_name = n
                        line[-1] = variables[var_name].value

            word = line[1]
            match word.upper():
                
                case "PUSH": #done
                    stack_name.push(line[-1])
                case  "ADD"| "SUB":
                    parseMiniupVars(line, variables)
                case "POP": # done
                    stack_name.pop()
                case "PEEK": # done
                    print(stack_name.peek())
                case "SIZE": # done
                    print(stack_name.size())
                case "ISEMPTY":
                    print(stack_name.isEmpty())
                case "PRINT":
                    print(stack_name.data[::-1])
                case "ISFULL":
                    print(stack_name.isFull())
                case "VAR":
                    vname, variable = parse_varible(line, stacks, variables)
                    variables[vname] = variable
                
                case _:
                    raise InvalidCommand(f"Invalid command: {line[1]}")

        elif command_word == "LOOP":
            dataToInsert = parse(file_data[idx:], int(line[1]), variables)
            file_data.pop(idx)
            for i in dataToInsert:
                file_data.insert(idx+1, i)
    if file_data_flag:
        print(file_data)
    if variableFlag:
        print(variables)
        for i in variables:
            print(f"{i} : {variables[i].value}")
            print(f"{i} : {variables[i].type}")


if __name__ == "__main__":
    OS=os.name
    match OS:
        case "posix":
            clearing_use = "clear"
        case "nt":
            clearing_use = "cls"
        case _:
            print("your OS system is not currently supported bt this program")
    os.system(clearing_use)
    exited = False
    while not exited:
        
        ask = input(">>> ")
        match ask.split()[0]:
            case "h" | "help":
                print("r/run - run")
                print("h/help - help")
                print("s/settings - settings")
                print("e/ exit - exit the program")
                print("c/clear - clear the terminal")
                input()
            case "s" | "settings":
                print("there are currently no settings at the moment")
            case "e" | "exit":
                os.system(clearing_use)
                quit()
            case "c" | "clear":
                os.system(clearing_use)
            case "r" | "run":
                
                split_words = ask.split()
                file = split_words[1]
                file_name = file.split(".")
                if file_name[1] != "stack":
                    try:
                        raise WrongFileExtenstion(f"file type is incorrect")
                    except WrongFileExtenstion as WFE:
                        print(WFE)
                        continue
                options = split_words[2:][0] if len(split_words)>2 else None
                try:

                    main(file, options, clearing_use)
                except FileNotFoundError:
                    print(f"{file} doesn't exist please use a file that actually exists!")
            case "os":
                print(os.name)
            case _:
                print("enter a valid command please")

#https://github.com/KOALAS2648/Stacker
