import datetime

import functions

functions.welcome()

invalidInput = True

while invalidInput == True:
    
    try:
        
        continueLoop = True
                
        while continueLoop == True:

            functions.option_select_message()

            option = int(input("Please enter one id from the given options: "))

    # -->Action if the customer input is 1<-- # 
            if option == 1:
                                
                functions.rent_costume()
                                
                functions.display_costumes()

                dictionarycostume = functions.dictionary_rent()

                rent_costume_Array = {}
 
                total_price_Array = []
                                
                moreRentLoop = True

                while moreRentLoop == True:

                    rentCostumeID = functions.valid_costume_ID_rent()
                                    
                    if int(dictionarycostume[rentCostumeID][3]) > 0:
                                        
                        functions.costume_available()

                        NoOfCostume = functions.quantity_validation(int(dictionarycostume[rentCostumeID][3]))
                                        
                        dictionarycostume[rentCostumeID][3] = int(dictionarycostume[rentCostumeID][3]) - NoOfCostume

                        rent_costume_Array[dictionarycostume[rentCostumeID][1]] = dictionarycostume[rentCostumeID][0]

                        functions.stock_costume_infile(dictionarycostume)

                        totalPrice = functions.total_price(dictionarycostume,NoOfCostume,rentCostumeID)
                                        
                        total_price_Array.append(totalPrice)

                    else:
                        functions.costume_unavailable()
                                    
                                    
                    print("Have you rented any costume previously?")
                    continueRent = input("Please enter 'n' if you have not rented any costume previously: ").lower()

                    if continueRent == "n":
                        moreRentLoop = False

                    else:
                        functions.display_customes()


                print("\n")
                nameOfCustomer = input("Enter your name: ")
                                    
                todayDate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                unique_rent_BillName = "Rent_" + nameOfCustomer + "_" + str(datetime.datetime.now().second) + str(datetime.datetime.now().microsecond) + str(datetime.datetime.now().hour) + ".txt"
                                
                totalPrice = 0
                                    
                for i in total_price_Array:
                    totalPrice = totalPrice + i

    # ->To generating invoice/file for the details of the customer for renting<- #
                print("\n")
                print("------------------------------------------")
                print("\t \t Bill Details")
                print("------------------------------------------")
                print("Customer name:", nameOfCustomer)
                print("Renting Date and Time:", todayDate)
                print("Total price is: $" + str(totalPrice))

                print("Rented customes are: ")
                Id = 1
                for brand,custome in rent_costume_Array.items():
                                    
                    print("\t" + str(Id) + ". " + brand + " --- " + custome)
                    Id += 1
                    
                print("------------------------------------------")

                                
                functions.rent_bill_generation(unique_rent_BillName,nameOfCustomer,todayDate,totalPrice,rent_costume_Array)
                                
                                
    # -->Action if the customer input is 2<-- #                   
            elif option == 2:
                              
                functions.return_costume()
                                
                functions.display_costumes()

                dictionarycostume = functions.dictionary_rent()

                return_costume_Array = {}

                fine_Array = []
                                
                return_loop = True

                while return_loop == True:

                    returnCostumeID = functions.valid_costume_ID_return()

                    returnquantityOfCostume = functions.quantity_return()

                    dictionarycostume[returnCostumeID][3] = str(int(dictionarycostume[returnCostumeID][3]) + returnquantityOfCostume)

                    return_costume_Array[dictionarycostume[returnCostumeID][1]] = dictionarycostume[returnCostumeID][0]

                    functions.stock_costume_infile(dictionarycostume)

                    fineAmount = functions.amount_of_fine(returnquantityOfCostume)

                    fine_Array.append(fineAmount)

                    print("Have you rented any costume previously?")
                    continueReturn = input("Please enter 'n' if you have not rented any costume previously: ").lower()

                    if continueReturn == "n":
                        return_loop = False

                    else:
                        functions.display_customes()
                                
                print("\n")
                nameOfCustomer = input("Enter your name: ")
                                    
                todayDate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                uniquerenturnBillName = "Return_" + nameOfCustomer + "_" + str(datetime.datetime.now().second) + str(datetime.datetime.now().microsecond) + str(datetime.datetime.now().hour) + ".txt"

    # ->To generate invoice/file for the details of the customer for returning<- #
                print("\n")
                print("------------------------------------------")
                print("\t \t Bill Details")
                print("------------------------------------------")
                print("Name of customer:", nameOfCustomer)
                print("Date Time of return:", todayDate)

                fine = 0
                for i in fine_Array:
                    fine = fine + i
                            
                print("Total price is: $" + str(fine))

                print("Rented costumes are: ")
                Id = 1
                for brand,custome in return_costume_Array.items():
                                    
                    print("\t" + str(Id) + ". " + brand + " --- " + custome)
                    Id += 1
                print("------------------------------------------")

                                
                functions.return_bill_generation(uniquerenturnBillName,nameOfCustomer,todayDate,fine,return_costume_Array)

    # -->Action if the customer input is 3<-- # 
            elif option == 3:
                functions.thank_you_message()
                
                continueLoop = False
                invalidInput = False

            else:
                functions.invalid_message()

    except:
        functions.invalid_message()
