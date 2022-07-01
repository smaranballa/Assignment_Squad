import os
import helper as hp
import collections

class ParkingLot:
    def __init__(self, numOfCars: int):
        self.numberOfCars = numOfCars
        self.slots = [0 for i in range(numOfCars)]
        self.carsWithAge = collections.defaultdict(set)             #Used Dictionary for Sets, because of O(1) lookup
        self.slotWithCar = {}
        self.slotsWithAge = collections.defaultdict(set)
        print(f"Created parking of {numOfCars} slots")
    
    #Checks if there are any available slots
    def CheckAvailableSlots(self):
        for i in range(self.numberOfCars):
            if self.slots[i] == 0:
                slotNum = i
                self.slots[i] = 1
                return True, slotNum
        return False, -1

    def ParkTheVehicle(self, cmdStrs):
        isAvailable, slotNum = self.CheckAvailableSlots()
        if isAvailable:
            vehicleNumber = cmdStrs[1]
            ageOfDriver = cmdStrs[3]
            
            # car = CarDetails(cmdStrs[1], cmdStrs[3], self.slotNumer)
            self.carsWithAge[ageOfDriver].add(vehicleNumber)
            self.slotsWithAge[ageOfDriver].add(slotNum)
            self.slotWithCar[vehicleNumber] = slotNum
            print(f"Car with vehicle registration number \"{vehicleNumber}\" has been parked at slot number {slotNum+1}")
            
        else:
            print("Sorry, Slots not available for your Car to park :(")
    
    def GetAlltheSlotNumbers(self, cmdStrs):
        ageOfDriver = cmdStrs[1]
        if ageOfDriver not in self.slotsWithAge:
            print(f"No Cars were parked with Drivers of Age {ageOfDriver}")
        else:
            slots = [str(slot+1) for slot in self.slotsWithAge[ageOfDriver]]
            print(", ".join(slots))
    
    def GetSlotNumberforCar(self, cmdStrs):
        vehicleNumber = cmdStrs[1]
        if vehicleNumber not in self.slotWithCar:
            print(f"The Car with Number {vehicleNumber} is never Parked...")
        else:
            print(self.slotWithCar[vehicleNumber])
    
    def GetTheVehicleNumbers(self, cmdStrs):
        driverAge = cmdStrs[1]
        if driverAge in self.carsWithAge:
            print(", ".join(self.carsWithAge[driverAge]))
        else:
            print()
    
    def VacateSlot(self, cmdStrs):
        slotNum = int(cmdStrs[1])
        if slotNum > self.numberOfCars or slotNum < 1:
            print("No such Slot in the Parking lot...")
        
        elif self.slots[slotNum-1] == 0:
            print("Slot already vacant...")
        
        else:
            self.slots[slotNum-1] = 0                   #Set the Slot Number as 0, such that next car can be parked here
            for carNumber in self.slotWithCar:
                if slotNum-1 == self.slotWithCar[carNumber]:
                    break
            vacatedCarNumber = carNumber
            del self.slotWithCar[vacatedCarNumber]      #Remove the Slot from the "slotWithCar" Dictionary

            driverAge = 0
            for age in self.slotsWithAge:               #Remove the SlotNumber from the "slotsWithAge" Dictionary
                if slotNum-1 in self.slotsWithAge[age]:
                    self.slotsWithAge[age].remove(slotNum-1)
                    driverAge = age
                    break
            
            for age in self.carsWithAge:                #Remove the CarNumber from the "carsWithAge" Dictioinary
                if vacatedCarNumber in self.carsWithAge[age]:
                    self.carsWithAge[age].remove(vacatedCarNumber)
                    break
            
            print(f"Slot number {slotNum} vacated, the car with vehicle registration number \"{vacatedCarNumber}\" left the space, the driver of the car was of age {driverAge}")


def ExecuteCommand(cmd: str, parkingLot: ParkingLot):
    cmdStrs = cmd.split()

    if cmdStrs[0] == "Park":
        parkingLot.ParkTheVehicle(cmdStrs)
    
    elif cmdStrs[0] == "Slot_numbers_for_driver_of_age":
        parkingLot.GetAlltheSlotNumbers(cmdStrs)
    
    elif cmdStrs[0] == "Slot_number_for_car_with_number":
        parkingLot.GetSlotNumberforCar(cmdStrs)
    
    elif cmdStrs[0] == "Leave":
        parkingLot.VacateSlot(cmdStrs)
    
    elif cmdStrs[0] == "Vehicle_registration_number_for_driver_of_age":
        parkingLot.GetTheVehicleNumbers(cmdStrs)

    else:
        print("INVALID Statement from the Input file ... :(")

def main():
    #Proceed only when the Input file exists
    if os.path.isfile("input.txt"):
        inputFile = open("input.txt", "r")
        input_statements = inputFile.readlines()
        lineNumber = 1
        parkingLot = None
        for command in input_statements:
            verified = hp.VerifyCommand(command)
            if verified:
                split = command.split()
                if lineNumber == 1 and command[0:6].lower() == "create":
                    parkingLot = ParkingLot(int(split[-1]))               #Creates a Parking Lot with given N
                    lineNumber += 1
                    continue
                ExecuteCommand(command, parkingLot)
            else:
                print(f"Unable to Verify Line Number {lineNumber} from the Input file...So, SKIPPING this line")
            lineNumber += 1
    else:
        print("Unable to locate the input file... :(")

if __name__ == "__main__":
    main()
  
