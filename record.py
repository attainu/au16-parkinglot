class Record:
    def __init__(self):
        self.slot_number = {}
        
        self.color_to_registration_number = {}

        self.color_to_slot_number = {}

        self.registration_number_to_slot_number = {}

        
    
    def add(self, slot, registration_number, color):
        if color not in self.color_to_registration_number:
            
            self.slot_number[slot] = [registration_number, color ]
            
            self.color_to_registration_number[color] = [registration_number]
            
            self.color_to_slot_number[color] = [slot]

            self.registration_number_to_slot_number[registration_number] = slot

        else:
            self.slot_number[slot] = [registration_number, color ]
            
            self.color_to_registration_number[color].append(registration_number)
            
            self.color_to_slot_number[color].append(slot)

            self.registration_number_to_slot_number[registration_number] = slot
            
    
    def remove(self, slot):
        self.color_to_registration_number[ self.slot_number[slot][1]   ].remove( self.slot_number[slot][0]   )
        
        self.color_to_slot_number[ self.slot_number[slot][1] ].remove(slot)

        self.registration_number_to_slot_number.pop( self.slot_number[slot][0]  )

        self.slot_number.pop(slot)


       
       