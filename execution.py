from record import Record
from register import Register

class Execution:
    def __init__(self, capacity):
        self.log = Register(capacity)
        self.history = Record()
    
    def execute(self, command):
        command = command.split()

        if command[0] == "park":

            check = self.log.add()

            if check:
                self.history.add(check, command[1],  command[2])
                return "Allocated slot number " + str(check)
            
            else:
                return "Sorry, parking lot is full"
        
        elif command[0] == "leave":
            check = self.log.remove(int(command[1]))
            if check:
                self.history.remove(check)
                return "Slot Number " + str(check) + " is free"
            
            else:
                return "Slot was already empty"
        
        else:
            if command[0] == "status":
                result = list()

                for key in self.history.slot_number.keys():
                    result.append([key, self.history.slot_number[key][0], self.history.slot_number[key][1]])
                
                if result:
                    return result
                
                else:
                    return "Parking lot is empty"
            
            else:
                if command[-1] in self.history.registration_number_to_slot_number:
                    return self.history.registration_number_to_slot_number[command[-1]]

                elif command[-1] in self.history.color_to_slot_number:
                    if len(command[0]) == 33:
                        return self.history.color_to_slot_number[command[-1]]
                    
                    else:
                        return self.history.color_to_registration_number[command[-1]]

                else:
                    return "Not found"