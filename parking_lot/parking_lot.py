class Parking():

    def __init__(self):
        self.parking_slots = list()

    def create_parking_lot_slots(self, no_of_slots):

        for i in range(no_of_slots):
            self.parking_slots.append([i + 1])

        print(f"Created a parking lot with {no_of_slots} slots")

    def show(self, Info):

        input_info = list(Info.split())

        if input_info[0] == 'park' and len(input_info) == 3:
            temp = "False"

            for i in range(len(self.parking_slots)):
                if len(self.parking_slots[i]) == 1:
                    self.parking_slots[i].append(input_info[1])
                    self.parking_slots[i].append(input_info[2])
                    print(f"Allocated slot number: {self.parking_slots[i][0]}")
                    temp = "True"
                    break
            if temp == "False":
                print("Sorry, parking lot is full")

        elif input_info[0] == "leave":
            res = (self.parking_slots[int(input_info[1])-1])
            if len(res) > 1:
                while len(res) != 1:
                    res.pop(1)
                print(f"Slot no {input_info[1]} is free")
            else:
                print(f"Slot no {input_info[1]} is already free")

        elif input_info[0] == "status":
            print("Slot No. Registration No Colour ")
            for i in self.parking_slots:
                if len(i) == 3:
                    for j in i:
                        print(j, end=" ")
                    print()

        elif input_info[0] == "registration_numbers_for_cars_with_colour":
            if len(input_info) == 2:
                car_colour = input_info[1]
                arr = list()
                for i in range(len(self.parking_slots)):
                    if car_colour in self.parking_slots[i]:
                        arr.append(self.parking_slots[i][1])

                for j in arr:
                    if j == arr[-1]:
                        print(j)
                    else:
                        print(j, end=(","))

        elif input_info[0] == "slot_numbers_for_cars_with_colour":
            if len(input_info) == 2:

                car_colour = input_info[1]
                arr = []
                for i in range(len(self.parking_slots)):
                    if car_colour in self.parking_slots[i]:
                        arr.append(self.parking_slots[i][0])
                    else:
                        print("Not Found")

                for j in arr:
                    if j == arr[-1]:
                        print(j)
                    else:
                        print(j, end=(","))

        elif input_info[0] == "slot_number_for_registration_number":
            if len(input_info) == 2:
                for i in range(len(self.parking_slots)):
                    if input_info[1] in self.parking_slots[i]:
                        print(self.parking_slots[i][0])
                        break
                else:
                    print("Not Found")
