#!/usr/bin/python
class Homework:
    
    def hex_converter():
    

        while True:
            try:
                # Try to convert bunary to decimal
        
                decimal_num = int(input("Enter a binary number: "), 16)
        
                # If we fail we ask again user to enter binary number
        
            except ValueError:
                print ("Your input is not a hex number! Please try again.")
            else:
                print (decimal_num)
                
                # Exit program if the conversion from binary to decimal was successful
                exit_prompt = str(input("Do you wish to close the programe yes or no : "))
                if exit_prompt == 'yes' :
                    break
                elif exit_prompt == 'no' :
                    pass
            # print converted decimal number

    def binary_to_decimal() :

        try:
            binary_num = int(input("Ender a binary number to:"), 2)
            binary_number = int(input("Ender a binary number to:"), 2)
        except ValueError:
            print ("Your input is not a binary number! Please try again.")
        else:
            print(binary_num + binary_number)





















    
