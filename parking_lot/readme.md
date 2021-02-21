Parking Lot

Setup

Requirements:
1. Python should be installed in system

2. VS Code Software should be installed

	To Design a parking lot using Python in VS Code

3. GIT should be installed
	
	To push the project code into github repo

4. Flake 8 should be installed in VS Code

	It will help you with linting, modular extensible code with oops principles & clean readable code


The project file called parking_lot.py has the following functions:

1. create_parking_lot_slots N - This function creates a parking lot with N no of slots
2. show - This function handles all the functions of a parking lot 

Like:

-> park the car into slot - it allocates the arrived car into nearest available parking slot
& ask for car details as in the following format
park reg_no colour - Parks a vehicle with given registration number and color in the empty slot . 
			If there are no more empty slots available, it display a message "Parking lot is full".

-> status - Prints the slot number, registration number and color of the parked vehicles.

-> leave N - Vacate the car from slot N

-> registration_numbers_for_cars_with_colour Colour - Prints the Registration numbers of all cars of a particular colour.

-> slot_numbers_for_cars_with_colour Colour - Prints the Slot numbers of all slots where a car of a particular colour is parked.

-> slot_number_for_registration_number reg_no - Prints the Slot number in which a car with a given registration number is parked


Running the app

-> Go To VS Code, Open parking_lot Project folder and open the main.py file and run that file.


Instructions and commands used by the program are as follows:

To run the program in Terminal or any command prompt follow below instructions:

->Please note that all inputs are case sensitive

Choose any one of the following:\n1.MANUAL\n2.FILE
1.MANUAL - you have to provide information manually what u need to do i.e. create, park, leave and see status of parking lot etc.
2.FILE - you should select the file you need to run:          

File path: E:\AttainU\Project\parking_lot\Run_test_cases.txt

-> To create a parking lot, "CreateParkingLot" eg : CreateParkingLot 6 [where 6 is number of slots]

-> To park a vehicle, "park" eg : park KA-01-HH-1234 White [where KA-01-HH-1234 is the registration no and White is the color of car]

-> To see status of car, "status" - Prints the slot number, registration number and color of the parked vehicles.

-> To vacate the car from parking lot, "leave" eg: leave 4 [where 4 is the slot number]

-> To print the Registration numbers of all cars of a particular colour, "registration_numbers_for_cars_with_colour" eg: registration_numbers_for_cars_with_colour White [Where White is the color of car]

-> To print the Slot numbers of all slots where a car of a particular colour is parked, "slot_numbers_for_cars_with_colour" eg: slot_numbers_for_cars_with_colour White [Where White is the color of car]

-> To print the Slot number in which a car with a given registration number is parked, "slot_number_for_registration_number" eg: slot_number_for_registration_number KA-01-HH-1234 [Where KA-01-HH-1234 is the Car Registration number]



FLAKE8 - I have used flake8 to check mistakes in all my project files and it shows NONE. (only for file name it shows)



INPUT: -

CreateParkingLot 6
park KA-01-HH-1234 White
park KA-01-HH-9999 White
park KA-01-BB-0001 Black
park KA-01-HH-7777 Red
park KA-01-HH-2701 Blue
park KA-01-HH-3141 Black
leave 4
status
park KA-01-P-333 White
park DL-12-AA-9999 White
registration_numbers_for_cars_with_colour White
slot_numbers_for_cars_with_colour White
slot_number_for_registration_number KA-01-HH-3141
slot_number_for_registration_number MH-04-AY-1111



OUTPUT:-

Created a parking lot with 6 slots
Allocated slot number: 1
Allocated slot number: 2
Allocated slot number: 3
Allocated slot number: 4
Allocated slot number: 5
Allocated slot number: 6
Slot no 4 is free
Slot No. Registration No Colour
1 KA-01-HH-1234 White 
2 KA-01-HH-9999 White
3 KA-01-BB-0001 Black
5 KA-01-HH-2701 Blue
6 KA-01-HH-3141 Black
Allocated slot number: 4
Parking lot is full, Sorry For Inconvinience
KA-01-HH-1234,KA-01-HH-9999,KA-01-P-333
not found
not found
not found
1,2,4
6
Not Found


