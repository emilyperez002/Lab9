def decode(encoded_password):
    decoded = []
    for digit in encoded_password:
        if digit == 4:
            decoded.append("1")
        elif digit == 5:
            decoded.append("2")
        elif digit == 6:
            decoded.append("3")
        elif digit == 7:
            decoded.append("4")
        elif digit == 8:
            decoded.append("5")
        elif digit == 9:
            decoded.append("6")
        elif digit == 0:
            decoded.append("7")
        elif digit == 1:
            decoded.append("8")
        elif digit == 2:
            decoded.append("9")
        elif digit == 3:
            decoded.append("0")
    return "".join(decoded)

encoded_password = [4, 5, 6, 7, 8]  # Replace this with the encoded password list
decoded_password = decode(encoded_password)
print("Decoded password:", decoded_password)
