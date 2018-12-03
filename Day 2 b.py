strike = 0
escape = False
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
    for y in range (len (codes)):
        for z in range (len (codes[x])):
            cvalues = [codes[x], codes[y]]
            if x != y:
                if codes [x][z] != codes [y][z]:                
                    if strike == 1:
                        strike = strike + 1
                        break
                    else:
                        strike = strike +1
                        diff= [codes[x][z], codes[y][z], z]
            else:
                strike = 2
        if strike == 2:
            strike = 0
            diff = 0
            cvalues = 0
        else:
            escape = True
            break
    if escape == True:
        break
print (cvalues)
print (diff)

results = cvalues [1][:diff[2]]+ cvalues [1][diff[2]+1:]

print (results)
    
