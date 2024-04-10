def encode():
    password = str(input("Please enter your password to encode: "))
    encoded = []
    for i in range(len(password)):
        if password[i] == "1":
            encoded.append(4)
        elif password[i] == "2":
            encoded.append(5)
        elif password[i] == "3":
            encoded.append(6)
        elif password[i] == "4":
            encoded.append(7)
        elif password[i] == "5":
            encoded.append(8)
        elif password[i] == "6":
            encoded.append(9)
        elif password[i] == "7":
            encoded.append(0)
        elif password[i] == "8":
            encoded.append(1)
        elif password[i] == "9":
            encoded.append(2)
        elif password[i] == "0":
            encoded.append(3)

