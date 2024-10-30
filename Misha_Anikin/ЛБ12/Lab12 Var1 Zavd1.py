import turtle

t = turtle.Turtle()

def execute_commands(commands):
    for command in commands:
        if command == 'F':
            t.forward(50)
        elif command == 'L':
            t.right(90)
        elif command == 'R':
            t.left(90)
        elif command == 'U':
            t.penup()
        elif command == 'D':
            t.pendown()
            
commands = "DFFRRRFFLFFFFURRFFFFFLLD"
execute_commands(commands)
turtle.done()