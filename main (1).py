luhya_numbers = {
    "0": "sihaya",
    "1": "halala",
    "2": "viviri",
    "3": "vidaru",
    "4": "vinne",
    "5": "virano",
    "6": "sita",
    "7": "saba",
    "8": "mnane",
    "9": "tisa",
    "10": "ehumi",
    "20": "mahumi ishirini",
    "30": "mahumi kadaru",
    "40": "mahumi khane",
    "50": "mahumi karano",
    "60": "mahumi sita",
    "70": "mahumi saba",
    "80": "mahumi mnane",
    "90": "mahumi tisa"
}

def analyze_luhya_number(number):
    if number.isdigit() and 0 <= int(number) <= 99:
        if len(number) == 1:
            return luhya_numbers.get(number, "Invalid number")
        else:
            if number == "10":
                return luhya_numbers[number]
            else:
                tens_digit = number[0] + "0"
                ones_digit = number[1]
                if ones_digit == "0":
                    return luhya_numbers[tens_digit]
                else:
                    return luhya_numbers[tens_digit] + " nde " + luhya_numbers[ones_digit]
    else:
        return "Invalid input, please enter a valid number (0-99)."

# Main loop
print(" EXAMPLES :")
print("15:is -> "+ analyze_luhya_number("15"))
print("24:is -> "+ analyze_luhya_number("24"))  
print("10:is -> "+ analyze_luhya_number("10"))  
print( "On input 101: -> "+ analyze_luhya_number("101")) 

# prompt user to input number
while True:
    user_input = input("Enter a number (0-99), or enter 0 to exit: ")
    if user_input == "0":
        break
    print(analyze_luhya_number(user_input))
