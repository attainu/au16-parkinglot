from parking_lot import Parking


class ManualInput:

    def __init__(self):
        self.manual = Parking()

    def create_parking_lot_slots(self):
        User_Input = list(input("$").split())
        size = int(User_Input[1])
        self.manual.create_parking_lot_slots(size)

    def show(self):

        temp = "True"

        while temp == "True":
            User_Input = input("$")
            if User_Input == "exit":
                temp = "False"
                break
            else:
                self.manual.show(User_Input)
