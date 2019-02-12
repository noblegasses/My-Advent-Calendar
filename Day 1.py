#test to demonstrate
number = []
total = [0]
escape = False
value = []
def read_file(): 
    try:
        f = open("Day1list.txt", "r")
        number = f.read().split('\n')
        f.close()
        return number
    except Exception:
        print ("cannot read file")

number = read_file()
number = [int(i) for i in number]
while True:
    for x in range (len(number)):
        
        total.append(total[len(total)-1] + int(number[x]))
        for y in range (len(total)):
            if total[len(total)-1] == total [y]:
                if len (total)-1 != y:
                    print("found one!")
                    value.append( total [len(total)-1])
                    escape = True
                    break
        if escape == True:
            break
    if escape == True:
        break
print(value)
print (len(total))
#print (total)
