import classStack as cs
import os
from Errors import *
def parse(idxInlist, section, times):
    counter = 0
    return_code =[]
    for line in section:
        command_word = line[0]
        if command_word == "END":
            break
        counter +=1

    repeatedSection = section[1:counter]
    return [i for i in repeatedSection*times]


def main(file, option, clearName):
    file_data_flag = False
    match option:
        case "-fd" | "--file-data":
            file_data_flag =  True
        case "-c" | "--clear":
            os.system(clearName)
        case None:
            pass
        case _:
            try:
                raise InvalidOption("Invalid operation used")
            except InvalidOption as IO:
                print(IO)
                return 
    stacks = {}
    file = open(file, "r")
    file_data = file.readlines()
    for idx, line in enumerate(file_data):
        if "\n" in line:
            file_data[idx] = line[:-1].split(" ")
        else:
            file_data[idx] = line.split(" ")
    loop_words = ["LOOP", "END"]
    for idx, line in enumerate(file_data):
        #print(line)
        loop_flag = False
        command_word = line[0]
        if line == [""]:
            continue
        elif command_word in stacks and line[1].upper() == "STACK":
            raise StackExist(f"stack '{command_word}' cannot be created as stack '{command_word}' already exists")
        if command_word not in loop_words:
            if command_word not in stacks and line[1].upper() == "STACK":
                stacks[command_word] = cs.Stack(int(line[-1]))
                continue
        if command_word in loop_words:
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
        
        if command_word not in loop_words:
            n = line[1]
            match n.upper():
                case "PUSH":
                    stack_name.push(line[-1])
                case "POP":
                    stack_name.pop()
                case "PEEK":
                    print(stack_name.peek())
                case "SIZE":
                    print(stack_name.size())
                case "ISEMPTY":
                    print(stack_name.isEmpty())
                case "PRINT":
                    print(stack_name.data)
                case "ISFULL":
                    print(stack_name.isFull())
                case _:
                    raise InvalidCommand(f"Invalid command: {line[1]}")

        elif command_word == "LOOP":
            dataToInsert = parse(idx, file_data[idx:], int(line[1]))
            file_data.pop(idx)
            for i in dataToInsert:
                file_data.insert(idx, i)
    if file_data_flag:
        print(file_data)


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
