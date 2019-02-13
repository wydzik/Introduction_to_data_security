import fractions

alphabet_matrix={'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10,
                 'L':11,'M':12,'N':13,'O':14,'P':15,'Q':16,'R':17,'S':18,'T':19,'U':20,
                 'V':21,'W':22,'X':23,'Y':24,'Z':25,' ':26,'.':27,',':28,'-':29,':':30}

alphabet_list=['A','B','C','D','E','F','G','H','I','J','K',
               'L','M','N','O','P','Q','R','S','T','U',
               'V','W','X','Y','Z',' ','.',',','-',':']

def message_convertor_to_values(uppercase_raw_message):
    """Method that converts message into integer values of letters, what simplify calculations"""
    message_into_values=[]
    for letter in uppercase_raw_message:
        message_into_values.append(alphabet_matrix[letter])
    return message_into_values

def encryption(k, message_into_values):
    """Cesar algorithm with multiplication"""
    encrypted_values = []
    i = 0
    for value in message_into_values:
        encrypted_values.append((message_into_values[i] * k) % 31)
        i = i + 1
    return encrypted_values

def translation_of_message(crypted_values):
    """Translating numbers into message"""
    new_message = []
    for value in crypted_values:
        new_message.append(alphabet_list[value])
    return new_message

def eulers_function(n):
    """Method, that calculates Euler's function"""
    amount = 0
    for k in range(1, n + 1):
        if fractions.gcd(n, k) == 1:
            amount += 1
    return amount

def values_decryption(k,message_into_values):
    decrypted_values = []
    i = 0
    for value in message_into_values:
        decrypted_values.append((message_into_values[i] * (k ** (eulers_function(len(alphabet_list))-1))) % len(alphabet_list))
        i = i + 1
    return decrypted_values

#Input from console, output on screen version:
def encryption_input_from_console():
    raw_message=input("Please enter your message: ")
    uppercase_raw_message=raw_message.upper()
    message_into_values=message_convertor_to_values(uppercase_raw_message)

    #print(message_into_values)
    k=int(input("Please enter the value of encryptor: "))

    encrypted_values=encryption(k,message_into_values)
    #print(encrypted_values)

    encrypted_message=translation_of_message(encrypted_values)
    print("".join(encrypted_message))

#Input from file, output to file version:

def encryption_input_from_file():
    input_file=open('lab1_pod_input.txt',mode='r')
    raw_message=input_file.read()

    uppercase_raw_message = raw_message.upper()
    message_into_values = message_convertor_to_values(uppercase_raw_message)

    #print(message_into_values)
    k = 4

    encrypted_values = encryption(k, message_into_values)
    # print(encrypted_values)

    encrypted_message = translation_of_message(encrypted_values)

    output_file=open('lab1_pod_output.txt',mode='w')
    outpucik="".join(encrypted_message)
    output_file.write(outpucik)
    output_file.close()
    print("Result stored in a file: lab1_pod_output.txt")

def decryption_input_from_console():
    raw_message = input("Please enter your message: ")
    uppercase_raw_message = raw_message.upper()
    message_into_values = message_convertor_to_values(uppercase_raw_message)

    k = int(input("Please enter the value of decryptor: "))

    decrypted_values=values_decryption(k,message_into_values)

    decrypted_message=translation_of_message(decrypted_values)
    print("".join(decrypted_message))

def decryption_input_from_file():
    input_file = open('lab1_pod_input_decryption.txt', mode='r')
    raw_message = input_file.read()
    input_file.close()
    uppercase_raw_message = raw_message.upper()
    message_into_values = message_convertor_to_values(uppercase_raw_message)

    k = int(input("Please enter the value of decryptor: "))

    decrypted_values=values_decryption(k,message_into_values)

    decrypted_message=translation_of_message(decrypted_values)
    output_file = open('lab1_pod_output_decryption.txt', mode='w')
    outpucik = "".join(decrypted_message)
    output_file.write(outpucik)
    output_file.close()
    print("Message saved in 'lab1_pod_output_decryption.txt")
def encryption_for_labs():
    input_file = open('lab1_pod_input.txt', mode='r')
    raw_message = input_file.read()

    uppercase_raw_message = raw_message.upper()
    message_into_values = message_convertor_to_values(uppercase_raw_message)


    encrypted_values = encryption(6, message_into_values)
    # print(encrypted_values)

    encrypted_message = translation_of_message(encrypted_values)

    output_file = open('lab1_pod_output.txt', mode='w')
    outpucik = "".join(encrypted_message)
    output_file.write(outpucik)
    output_file.close()
    print("Result stored in a file: lab1_pod_output.txt")


encryption_input_from_console()
decryption_input_from_console()
#encryption_input_from_file()
#decryption_input_from_file()
