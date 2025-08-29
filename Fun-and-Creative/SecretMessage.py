while True:
    print("\n1.Encode")
    print("2.Decode")
    print("3.Exit")
    option = int(input("Choose Option: "))
    
    match option:
        case 1:
            encode = input("Enter Message to Encode: ")
            encode_list = []
            for secret in encode:
                if secret.isalpha():
                    message = ord(secret) + 3
                    new_message = chr(message)
                    encode_list.append(new_message)
                else:
                    encode_list.append(secret)
                    print(secret)
            print("Encoded Message is: ","".join(encode_list))

        case 2:
            decode = input("Enter Message to Decode: ")
            decode_list = []
            for de_secret in decode:
                if de_secret.isalpha():
                    new_demessage = ord(de_secret) - 3
                    new_new_demessage = chr(new_demessage)
                    decode_list.append(new_new_demessage)
                else:
                    decode_list.append(de_secret)
                    print(de_secret)
            print("Encoded Message is: ","".join(decode_list))

        case 3:
            print("thanks for using our service.")
            break            

        case _:
            print("Invalid Option: ")
























