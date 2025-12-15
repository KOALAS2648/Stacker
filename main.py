import classStack as cs

def parse(idxInlist, section, times):
    counter = 0
    return_code =[]
    for line in section:
        
        if line[0] == "END":
            break
        counter +=1

    repeatedSection = section[1:counter]
    return [i for i in repeatedSection*times]
def main(file):
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
        command = line[0]
        loop_flag = False
        if line == [""]:
            continue
        elif command in stacks and line[1].upper() == "STACK":
            raise Exception(f"stack '{command}' cannot be created as stack '{command}' already exists")
        if command not in loop_words:
            if command not in stacks and line[1].upper() == "STACK":
                stacks[command] = cs.Stack(int(line[-1]))
                continue
        if command in loop_words:
            continue
        else:
            try:
                stack_name = stacks[command]
            except KeyError:
                raise Exception(f"stack {command} does not exist")
        
        if command not in loop_words:
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
                    raise Exception(f"Invalid command: {line[1]}")

        elif command == "LOOP":
            dataToInsert = parse(idx, file_data[idx:], int(line[1]))
            file_data.pop(idx)
            for i in dataToInsert:
                file_data.insert(idx, i)
            


if __name__ == "__main__":
    main("code.txt")
