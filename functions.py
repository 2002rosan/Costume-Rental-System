
def welcome():
    print("\n")
    print("**********************************************")
    print("\tWELCOME TO COSTUME RENTAL SHOP")
    print("**********************************************")

def option_select_message():
    print("\n")
    print("Select one option from the given list.")
    print("1. Enter 1 to rent a costume")
    print("2. Enter 2 to return a costume")
    print("3. Enter 3 to exit.\n")

def thank_you_message():
    print("\n")
    print("Thank You for using our costume rental shop application!")

def invalid_message():
    print("\n")
    print("Invalid input.")
    print("Please select the value as per the provided options.")


def rent_costume():
    print("\n")
    print("You can rent any costumes from the following options.")
    

def return_costume():
    print("\n")
    print("You can return from here.")

    
def costume_available():
    print("\n")
    print("--------------------------")
    print("Costume is available")
    print("--------------------------")

def costume_unavailable():
    print("\n")
    print("--------------------------")
    print("Costume is not in stock.")
    print("--------------------------")
    print("\n")



def display_costumes():
    print("\n")
    file = open("costumes.txt","r")
    print("-----------------------------------------------------------------")
    print("ID     Costume Name       Costume Brand    Price         Stock")
    print("-----------------------------------------------------------------")
    counterID = 0
    for line in file:
        counterID = counterID + 1
        print("",counterID,"   ",line.replace(",","\t   "))
    file.close()
    print("-----------------------------------------------------------------")


def dictionary_rent():
    file = open("costumes.txt", "r")
    counterID = 0
    dictionary_costume = {}
    for line in file: 
        counterID = counterID + 1
        line = line.replace("\n","")
        line = line.split(',')

        dictionary_costume[counterID] = line
    return dictionary_costume
    file.close()

def valid_costume_ID_rent():

    invalidInputLoop = True

    while invalidInputLoop == True:
        try:
            print("\n")
            validCostumeID = int(input("Enter the ID of costume you want to rent: "))
            
            while validCostumeID <= 0 or validCostumeID > len(dictionary_rent()):
                print("\n")
                print("Please provide valid id from above options!")
                
                display_customes()
                
                validCostumeID = int(input("Enter the ID of costume you want to rent:"))

            invalidInputLoop = False
            
        except:
            invalid_message()
            
    return validCostumeID


def valid_costume_ID_return():

    invalidInputLoop = True

    while invalidInputLoop == True:
        try:
            print("\n")
            validCostumeID = int(input("Enter the ID of costume you want to return: "))
            
            while validCostumeID <= 0 or validCostumeID > len(dictionary_rent()):
                print("\n")
                print("Please provide valid id from above options!")
                
                display_customes()
                
                validCostumeID = int(input("Enter the ID of costume you want to return:"))

            invalidInputLoop = False
            
        except:
            invalid_message()
            
    return validCostumeID
        


def quantity_validation(stockQuantity):

    invalidInputLoop = True

    while invalidInputLoop == True:
        try:
            quantityOfCostume = int(input("\nEnter the number of costume you want to rent: "))
            
            while quantityOfCostume <=0 or quantityOfCostume > stockQuantity:
                if quantityOfCostume <= 0:
                    print("\n-----------------------------------------")
                    print("Please provide the number of costumes more than 0.")
                    print("-----------------------------------------\n")
                else:
                    print("\n-----------------------------------------")
                    print("Provided number of costume is more than our stock")
                    print("-----------------------------------------\n")

                quantityOfCostume = int(input("Enter the quantity: "))
            invalidInputLoop = False

        except:
            invalid_message()
            
    return quantityOfCostume


def stock_costume_infile(dictionary):
    file = open("costumes.txt","w")
    for i in dictionary.values():
        line = str(i[0] + "," + str(i[1]) + "," + str(i[2]) + "," + str(i[3])) 
        file.write(line)
        file.write("\n")
    file.close()



def total_price(dictionary, quantityDetails, costumeID):
    price = float(dictionary[costumeID][2].replace("$",""))
    print("\n")
    print("The price of costume: $" + str(price))
    print("\n")
    pricePerItem = price * quantityDetails
    return pricePerItem



def rent_bill_generation(bill,customerName,currentDate,finalPrice,rentCustomedict):


    file = open(bill,"w")
    file.write("Name of the customer is: " + customerName)
    file.write("\n")
    file.write("Date of rent of custome is: " + str(currentDate))
    file.write("\n")
    file.write("Total Price of custome is: $" + str(finalPrice))
    file.write("\n")
    file.write("Customes rented are: ")
    file.write("\n")
    
    Id = 1
    for brand,custome in rentCustomedict.items():
            
        file.write("\t" + str(Id) + ". " + custome + " --- " + brand)
        file.write("\n")
        Id += 1

    file.close()

    
def quantity_return():

    invalidInputLoop = True

    while invalidInputLoop == True:
        try: 
            print("\n")
            returnQuantity = int(input("How many costume you want to return: "))
                    
            while returnQuantity <= 0:

                print("\n")
                print("** Enter the valid quantity. **")
                print("\n")
                returnQuantity = int(input("How many costume you want to return: "))

            invalidInputLoop = False

        except:
             invalid_message()
                
    return returnQuantity



def amount_of_fine(quantity):

    invalidInputLoop = True

    while invalidInputLoop == True:

        try:
            print("\n")
            rented_days = int(input("Enter the days taken to return: "))

            while rented_days <= 0:
                
                print("\n")
                print("** Enter the valid days. **")
                print("\n")
                
                rented_days = int(input("Enter the days taken to return: "))
                
            if rented_days > 5:
                finedDays = rented_days - 5

            else:
                finedDays = 0
            
            finePer = finedDays * 2
            
            print("\n")
            print("Fine for the delay: $" + str(finePer * quantity))
            print("\n")
            
            totalFine = finePer * quantity

            invalidInputLoop = False

        except:
            invalid_message()
            
    return totalFine



def return_bill_generation(bill,customerName,currentDate,totalFine,renturnCustomedict):

    
    file = open(bill,"w")
    file.write("Name of the customer is: " + customerName)
    file.write("\n")
    file.write("Date of return of custome is: " + str(currentDate))
    file.write("\n")
    file.write("Total fine is: $" + str(totalFine))
    file.write("\n")
    file.write("Customes rented are: ")
    file.write("\n")
    
    Id = 1
    for brand,custome in renturnCustomedict.items():
            
        file.write("\t" + str(Id) + ". " + custome + " --- " + brand)
        file.write("\n")
        Id += 1

    file.close()
