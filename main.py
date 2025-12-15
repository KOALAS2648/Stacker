import classStack as cs


#print(file_data)



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
        file_data[idx] = line[:-1].split(" ")
    loop_words = ["LOOP", "END"]
    for idx, line in enumerate(file_data):
        #print(line)
        loop_flag = False
        if line == [""]:
            continue
        elif line[0] in stacks and line[1].upper() == "STACK":
            raise Exception(f"stack '{line[0]}' cannot be created as stack '{line[0]}' already exists")
        if line[0] not in loop_words:
            if line[0] not in stacks and line[1].upper() == "STACK":
                stacks[line[0]] = cs.Stack(int(line[-1]))
                continue
        if line[0] == "LOOP" or line[0] == "END":
            pass
        else:
            try:
                f = stacks[line[0]]
            except KeyError:
                raise Exception(f"stack {line[0]} does not exist")
        
        if line[0] not in loop_words:
            if line[1].upper() == "PUSH":
                stacks[line[0]].push(line[-1])
                continue
            elif line[1].upper() == "POP":
                stacks[line[0]].pop()
                continue
            elif line[1].upper() == "PEEK":
                print(stacks[line[0]].peek())
                continue
            elif line[1].upper() == "SIZE":
                print(stacks[line[0]].size())
                continue
            elif line[1].upper() == "ISEMPTY":
                print(stacks[line[0]].isEmpty())
                continue
            elif line[1] == "9":
                print("testing line")
            
            else:
                raise Exception(f"Invalid command: {line[1]}")

        elif line[0] == "LOOP":
            dataToInsert = parse(idx, file_data[idx:], int(line[1]))
            file_data.pop(idx)
            for i in dataToInsert:
                file_data.insert(idx, i)
            


if __name__ == "__main__":
    main("code.txt")
