SECRET_PIN = "1234"
tries      = 0

while tries < 3:
#################### enter and verify 1st time ######################    
    input_pin = input("Enter your PIN: ")
    if input_pin == SECRET_PIN:
        print("Access granted")
        tries = 1000
    else:
        print("Access denied")
#################### enter and verify 1st time ######################   
    tries += 1
    