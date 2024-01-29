class flight():
    def __init__(self,capacity):
        self.capacity=capacity
        self.passengers = []
    def add_passenger(self, name):
        if not self.open_seats(): # or if self.open_seats==0:
          return(Falsealse)
        else:
            return(True)
        self.passengers.append(name) # calling add passengers would add a name to the list

    def open_seats(self):
        return self.capacity-len(self.passengers)
    

Flight=flight(3) # provide a capacity
                 #auto gets the empty list of passengers

people=["haary" , "ron","ronaldo","ney"]

for person in people:
    success=flight.add_passenger(person)
    if success:
        print(f"Added {person} to flight successfully")
else:
     print("seats not available for {person}")