
command_words = ["pop", "push", "isEmpty", "size"]
stack = []
MAX_SIZE = 10
def minipulateStack(command, inp=None):
    match command.lower():
        case "pop":
            if len(stack) == 0:
                raise Exception("stack underflow error")
            stack.pop()
        case "push":
            if len(stack) == MAX_SIZE:
                raise Exception( "stack overflow Error")
            stack.append(inp)
        case "isempty":
            return  len(stack)==0
        case "size":
            return len(stack)
        case "peek":
            return stack[-1]

        case other:
            raise Exception("can't use that command")

for i in range(0, 10): minipulateStack("push", 100)