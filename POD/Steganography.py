import cv2

def translating_message_into_values(message):
    values=[]
    for character in message:
        values.append(ord(character))
    return values
def translating_values_into_binary(values):
    binary=[]
    for number in values:
        binary.append(bin(number)[2:].zfill(7))
    return binary
def changing_value(value, bit):
    if bit=='0' and bin(value)[-1]=='0':
        return value
    if bit=='1' and bin(value)[-1]=='1':
        return value
    if bit=='0' and bin(value)[-1]=='1':
        return value-1
    if bit=='1' and bin(value)[-1]=='0':
        return value+1
def hiding_message_inside_image(image,message):
    if(len(image)*len(image[0])<len(message)):
        print("Message is too long, it wouldn't fit in this image.")
    else:
        if ((len(image[0])) % 3 == 0):
            i=0
            j=0
            for character in message:
                image.itemset((i, j * 3, 0), changing_value(image.item(i, j * 3, 0), character[0]))
                image.itemset((i, j * 3, 1), changing_value(image.item(i, j * 3, 1), character[1]))
                image.itemset((i, j * 3, 2), changing_value(image.item(i, j * 3, 2), character[2]))
                image.itemset((i, (j * 3) + 1, 0), changing_value(image.item(i, (j * 3) + 1, 0), character[3]))
                image.itemset((i, (j * 3) + 1, 1), changing_value(image.item(i, (j * 3) + 1, 1), character[4]))
                image.itemset((i, (j * 3) + 1, 2), changing_value(image.item(i, (j * 3) + 1, 2), character[5]))
                image.itemset((i, (j * 3) + 2, 0), changing_value(image.item(i, (j * 3) + 2, 0), character[6]))
                image.itemset((i, (j * 3) + 2, 1), changing_value(image.item(i, (j * 3) + 2, 1), '0'))
                image.itemset((i, (j * 3) + 2, 2), changing_value(image.item(i, (j * 3) + 2, 2), '0'))
                if ((j * 3) + 2) == len(image[0])-1:
                    j=0
                    i+=1
                j+=1
        if ((len(image[0])) % 3 == 1):
            i = 0
            j = 0
            for character in message:
                if ((j * 3) + 2) == len(image[0]) - 1:
                    image.itemset((i, j * 3, 0), changing_value(image.item(i, j * 3, 0), character[0]))
                    image.itemset((i, j * 3, 1), changing_value(image.item(i, j * 3, 1), character[1]))
                    image.itemset((i, j * 3, 2), changing_value(image.item(i, j * 3, 2), character[2]))
                    i+=1
                    j=0
                    image.itemset((i, (j * 3) + 1, 0), changing_value(image.item(i, (j * 3) + 1, 0), character[3]))
                    image.itemset((i, (j * 3) + 1, 1), changing_value(image.item(i, (j * 3) + 1, 1), character[4]))
                    image.itemset((i, (j * 3) + 1, 2), changing_value(image.item(i, (j * 3) + 1, 2), character[5]))
                    image.itemset((i, (j * 3) + 2, 0), changing_value(image.item(i, (j * 3) + 2, 0), character[6]))
                    image.itemset((i, (j * 3) + 2, 1), changing_value(image.item(i, (j * 3) + 2, 1), 0))
                    image.itemset((i, (j * 3) + 2, 2), changing_value(image.item(i, (j * 3) + 2, 2), 0))
                    j+=1
                else:
                    image.itemset((i, j * 3, 0), changing_value(image.item(i, j * 3, 0), character[0]))
                    image.itemset((i, j * 3, 1), changing_value(image.item(i, j * 3, 1), character[1]))
                    image.itemset((i, j * 3, 2), changing_value(image.item(i, j * 3, 2), character[2]))
                    image.itemset((i, (j * 3) + 1, 0), changing_value(image.item(i, (j * 3) + 1, 0), character[3]))
                    image.itemset((i, (j * 3) + 1, 1), changing_value(image.item(i, (j * 3) + 1, 1), character[4]))
                    image.itemset((i, (j * 3) + 1, 2), changing_value(image.item(i, (j * 3) + 1, 2), character[5]))
                    image.itemset((i, (j * 3) + 2, 0), changing_value(image.item(i, (j * 3) + 2, 0), character[6]))
                    image.itemset((i, (j * 3) + 2, 1), changing_value(image.item(i, (j * 3) + 2, 1), 0))
                    image.itemset((i, (j * 3) + 2, 2), changing_value(image.item(i, (j * 3) + 2, 2), 0))
                    j+=1
        if ((len(image[0])) % 3 == 2):
            i = 0
            j = 0
            for character in message:
                if ((j * 3) + 2) == len(image[0]) - 2:
                    image.itemset((i, j * 3, 0), changing_value(image.item(i, j * 3, 0), character[0]))
                    image.itemset((i, j * 3, 1), changing_value(image.item(i, j * 3, 1), character[1]))
                    image.itemset((i, j * 3, 2), changing_value(image.item(i, j * 3, 2), character[2]))
                    image.itemset((i, (j * 3) + 1, 0), changing_value(image.item(i, (j * 3) + 1, 0), character[3]))
                    image.itemset((i, (j * 3) + 1, 1), changing_value(image.item(i, (j * 3) + 1, 1), character[4]))
                    image.itemset((i, (j * 3) + 1, 2), changing_value(image.item(i, (j * 3) + 1, 2), character[5]))
                    i+=1
                    j=0
                    image.itemset((i, (j * 3) + 2, 0), changing_value(image.item(i, (j * 3) + 2, 0), character[6]))
                    image.itemset((i, (j * 3) + 2, 1), changing_value(image.item(i, (j * 3) + 2, 1), 0))
                    image.itemset((i, (j * 3) + 2, 2), changing_value(image.item(i, (j * 3) + 2, 2), 0))
                    j+=1
                else:
                    image.itemset((i, j * 3, 0), changing_value(image.item(i, j * 3, 0), character[0]))
                    image.itemset((i, j * 3, 1), changing_value(image.item(i, j * 3, 1), character[1]))
                    image.itemset((i, j * 3, 2), changing_value(image.item(i, j * 3, 2), character[2]))
                    image.itemset((i, (j * 3) + 1, 0), changing_value(image.item(i, (j * 3) + 1, 0), character[3]))
                    image.itemset((i, (j * 3) + 1, 1), changing_value(image.item(i, (j * 3) + 1, 1), character[4]))
                    image.itemset((i, (j * 3) + 1, 2), changing_value(image.item(i, (j * 3) + 1, 2), character[5]))
                    image.itemset((i, (j * 3) + 2, 0), changing_value(image.item(i, (j * 3) + 2, 0), character[6]))
                    image.itemset((i, (j * 3) + 2, 1), changing_value(image.item(i, (j * 3) + 2, 1), 0))
                    image.itemset((i, (j * 3) + 2, 2), changing_value(image.item(i, (j * 3) + 2, 2), 0))
                    j+=1
        return image
    return 0





img=cv2.imread('gkwtc.jpeg',cv2.IMREAD_COLOR)

message='Is this the real life? Is this just fantasy? Calling the landside, to escape from reality. Open your eyes, look up through the sky and see. Im just a poor boy, I need no symphaty because Im easy come easy come, little high little low. anywhere the wind blows, it doesnt really matters to me...to me. Mamma, I just killed a man. Put a gun against his head, pull the trigger, now he is dead. Mamma, life it just begun, but now Im gonna throw it all away. Maama, uuuuu, didnt mean to make you cry, if Im not back again it starts tommorow, carry on, carry on. Cause it nothing really matters. To late, my time has come, send shivers down my spine, body is aching all the time. Goodbye everybody, I ve got to go. Im gonna live you all behind and face the truth'
values=translating_message_into_values(message)
binary=translating_values_into_binary(values)
image=hiding_message_inside_image(img,binary)
cv2.imwrite('wtc.png',image)
print("Message stored in 'wtc.png'")


#px=img[100,100,0]
#print(bin(px))
#print(bin(img.item(100,100,0)))
#print(translating_values_into_binary(translating_message_into_values('Another one bites the dust')))
