from record import Record
from register import Register
from execution import Execution

command = input()
command = int(command.split()[-1] )
user = Execution(command)
output = []

while command != "exit":
    command = input()

    if command != "exit":
        enter = user.execute(command)
        
        output.append(enter)

print(output)