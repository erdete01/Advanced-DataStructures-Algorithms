def hash_mid_sqr(key, size):
    """Find hash using mid-square method"""
    myNum = 0
    for i in range(len(key)):
        myNum += ord(key[i])
    print(myNum % size)
print(hash_mid_sqr("coronavirus", 7))