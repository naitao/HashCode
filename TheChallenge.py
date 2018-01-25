
# Finished duration: 2.5 hours
# Data: 01/24/2018
# Exame URL: https://techdevguide.withgoogle.com/paths/advanced/compress-decompression/#!

def cutNum(strings):
    count = 0
    numString = ''
    for offset in range(len(strings)):
        if strings[offset].isdigit():
            numString += strings[offset]
            count += 1
        if strings[offset] == '[':
            num = int(numString)
            return num, count

def cutString(strings):
    str = ''
    left_count = 0
    for offset in range(len(strings)):
       if strings[offset] == '[':
           left_count += 1
       if strings[offset] == ']':  
           left_count -= 1
       str += strings[offset]
       if left_count == 0:
           return [str[1:-1], offset+1]

def num_there(str):
    return any(i.isdigit() for i in str)

def addStrs(times, str):
    strings = ''
    for time in range(times):           
        strings += str
    return strings

strings = input("Please input number[string]:")

while num_there(strings):
    fullString = ''
    subString = ''
    count = 0
    num = 0
    offset = 0
    while (offset<len(strings)):
        if strings[offset].isdigit():
            num, count = cutNum(strings[offset:])
            offset += count
            subString, count = cutString(strings[offset:])
            offset += count
            fullString += addStrs(num, subString)
            #print("offset=", offset)
        else:
            fullString += strings[offset]
            offset += 1
    strings = fullString

print(strings)
