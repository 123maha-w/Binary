def BinaryToInt(BinaryInput):

    Binary = {'1111101000':1000,'111110100':500,'1100100':100,'110010':50,'1010':10,'101':5,'1':1}

    resultInteger= 0

    for i in range(0, len(BinaryInput)- 1):
        if Binary[BinaryInput [i]] < Binary[BinaryInput [i+2]]:
            resultInteger -= Binary[BinaryInput [i]]

        else:
            BinaryInput += Binary[BinaryInput [i]]
    return resultInteger + Binary[BinaryInput [-1]]

Binary = input("input your Binary :")

print ("integer :",BinaryToInt(Binary))


