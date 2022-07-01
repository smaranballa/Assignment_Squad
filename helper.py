def isInteger(s):
    try: 
        int(s)
        return True
    except ValueError:
        print(f"Unable to Convert the given STRING '{s}' to INTEGER :(")
        return False

# Verfifies whether the given Command is Valid or not
def VerifyCommand(commandStr):
    listOfStrs = commandStr.split() 
    cmdStrs = [commStr.lower() for commStr in listOfStrs]           #Making our code to neglect about Lower/Upper Case (Case Insensitive)
    if len(cmdStrs) < 2 or len(cmdStrs) > 4:
        return False
    
    #Check for "Create_parking_lot" command
    if len(cmdStrs) == 2 and cmdStrs[0] == "create_parking_lot":
        isInt = isInteger(cmdStrs[1])
        if isInt:
            return int(cmdStrs[1]) in range(0,1001)
        else:
            return False
    
    #Check for "Park" command
    elif len(cmdStrs) == 4 and cmdStrs[0] == "park" and cmdStrs[2] == "driver_age":
        def verifyVehicleNumber(number):
            vehicleNumber = number.split("-")
            if len(vehicleNumber) != 4:
                return False
            return vehicleNumber[0].isalpha() and vehicleNumber[1].isnumeric() and vehicleNumber[2].isalpha() and vehicleNumber[3].isnumeric()
        isInt = isInteger(cmdStrs[3])
        if isInt:
            return verifyVehicleNumber(cmdStrs[1]) and int(cmdStrs[3]) in range(0,1001)
    
    #Check for "Slot_numbers_for_driver_of_age" command
    elif len(cmdStrs) == 2 and cmdStrs[0] == "slot_numbers_for_driver_of_age" :
        isInt = isInteger(cmdStrs[1])
        if isInt:
            return True and (int(cmdStrs[1]) in range(0,1001))
        else:
            return False
    
    #Check for "Slot_number_for_car_with_number" command
    elif len(cmdStrs) == 2 and cmdStrs[0] == "slot_number_for_car_with_number" :
        def verifyVehicleNumber(number):
            vehicleNumber = number.split("-")
            if len(vehicleNumber) != 4:
                return False
            return vehicleNumber[0].isalpha() and vehicleNumber[1].isnumeric() and vehicleNumber[2].isalpha() and vehicleNumber[3].isnumeric()
        return verifyVehicleNumber(cmdStrs[1])

    #Check for "Leave" command
    elif len(cmdStrs) == 2 and cmdStrs[0] == "leave":
        isInt = isInteger(cmdStrs[1])
        if isInt:
            return True and (int(cmdStrs[1]) in range(0,1001))

    #Check for "Vehicle_registration_number_for_driver_of_age" command
    elif len(cmdStrs) == 2 and cmdStrs[0] == "vehicle_registration_number_for_driver_of_age":
        isInt = isInteger(cmdStrs[1])
        if isInt:
            return True and (int(cmdStrs[1]) in range(1,1001))
        else:
            return False

    #Return False, if any of the above conditions are not met
    else:
        return False