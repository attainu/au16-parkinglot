from manual_input import ManualInput
from file_input import FileInput

if __name__ == "__main__":

    print("Please note that all inputs are case sensitive")
    print("Choose any one of the following:\n1.MANUAL\n2.FILE")
    interaction_with_user = input("Type MANUAL or FILE here:")
    print()
    manual = ManualInput()
    auto = FileInput()

    if interaction_with_user == "MANUAL":
        cnt = 0
        while cnt < 2:
            if cnt == 0:
                manual.create_parking_lot_slots()
                cnt += 1
            else:
                manual.show()
                cnt += 1

    elif interaction_with_user == "FILE":
        print("File path: E:\AttainU\Project\parking_lot\Run_test_cases.txt")
        file_address = input("Please enter the file location here :\n$ ")
        f = open(file_address, "r")
        cnt = 0
        for row in f:
            if cnt == 0:
                auto.create_parking_lot_slots(row)
                cnt += 1
            else:
                auto.show(row)
