import sys

def houseLawn(num, size, m, l):
    myList = list()
    for i in range(num):  
        v1,v2,v3,v4 = m[i].split(',')
        v1, v2, v3, v4 = map(int, (v1, v2, v3, v4))
        time = (10080 // (v3 + v4)) * v3 + min(10080 % (v3 + v4), v3)
        if size <= time * v2 and v2 * v3 * 10080 >= size * (v3 + v4): myList.append((v1, i, l[i]))
    if len(myList) == 0: print('no such mower')
    else:
        myList = sorted(myList)
        for v1, i, l[i] in myList:
            if v1 == myList[0][0]: print(l[i])
            else: break

def main(data):
    aLine = data.readlines()
    myList, values, l, m = list(), list(), list(), list()
    for i in aLine: myList.append(i.strip().split(",", 1))
    for i in myList[0]: values.append(i.split())
    s, n = int(values[0][0]), int(values[0][1])
    myList = myList[1::]
    for i in myList: l.append(i[0])
    for i in myList: m.append(i[1])
    houseLawn(n,s,m,l)

if __name__ == "__main__":
    main(sys.stdin)