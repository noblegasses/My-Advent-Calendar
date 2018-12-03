rep2 = 0
check2 = False
rep3 = 0
check3 = False
maybe = False
found= False
def read_file(): 
    try:
        f = open("Day2list.txt", "r")
        number = f.read().split('\n')
        f.close()
        return number
    except Exception:
        print ("cannot read file")
codes = read_file()
for x in range (len (codes)):
    #print (codes[x])
    for y in range (len (codes[x])):
        for z in range(len(codes[x])):
            #print (codes[x][ y :y+1] + " , " + codes[x][(z):z+1])
            if codes[x][y:y+1] == codes[x][(z):z+1]:
                if y!=z:
                    maybe = maybe + 1
                    if check2 == False:
                        print (codes[x]+ ": " + codes[x][ y :y+1] + " , " + codes[x][(z):z+1])
                    if check3 == False:
                        print (codes[x]+ ": " + codes[x][ y :y+1] + " , " + codes[x][(z):z+1])
                    # print ("maybe = " +str(maybe))
        if maybe == 1:
            if check2 == False:
                rep2 = rep2 + 1
                check2 = True
                maybe = 0
        if maybe == 2:
            if check3 ==False:
                rep3 =  rep3 + 1
                check3 = True
                maybe = 0
        maybe=0
    check2 = False
    check3 = False
print (rep2)
print (rep3)
value = rep3*rep2
print (value)
