from parking_lot import Parking


class FileInput:

    def __init__(self):

        self.file = Parking()

    def create_parking_lot_slots(self, capacity):
        user_input = list(capacity.split())
        size = int(user_input[1])
        self.file.create_parking_lot_slots(size)

    def show(self, capacity):

        User_Input = capacity

        self.file.show(User_Input)
