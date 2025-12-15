All the funnctions that a stack uses are supported: - these functions aren't case sensitive
PUSH <p></p>
POP <p></p>
PEEK<p></p>
isEmpty/isFull - True / False<p></p>
SIZE - size of the satck<p></p>

<p></p>
<p></p>
Extra functions:- these functions are case sensitive and must be in all caps<p></p>
STACK - creates a stack object to use <b>MUST BE USED BEFORE USING PUSH / POP</B><p></p>
LOOP/END - used when you want to do a line of code multipule times <p></p>

<b>Example program</b>
<p></p>
first_stack STACK 7<p></p>
first_stack PUSH 10<p></p>
first_stack PUSH 20<p></p>
first_stack PUSH 30<p></p>
first_stack PUSH 40<p></p>
<p></p>
<p></p>
first_stack PUSH 50<p></p>
first_stack PUSH 60<p></p>
LOOP 4<p></p>
first_stack pop<p></p>
END<p></p>
<p></p>
first_stack PUSH 70<p></p>
first_stack PUSH 80<p></p>
first_stack PEEK<p></p>
