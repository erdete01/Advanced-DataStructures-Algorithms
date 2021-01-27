import sys

def tenis(x, y, mySet, p, q):
    if x == y: return False, 0
    winner = 0
    if x < y:
        winner = 1
        x, y = y, x
        p, q = q, p
    # Federer wins
    if q == 'federer': return False, winner
    # 6 wins
    if x < 6: return False, winner
    if x == 6: return y <= 4, winner
    if x == 7 and mySet < 2: return (y in (5, 6)), winner
    if x >= 7 and mySet == 2: return x == y+2, winner
    return False, winner

def main(data):
    res = list()
    for i in data.readlines(): res.append(i.strip().split())
    p, q, n = res[0][0], res[0][1], int(res[1][0])
    res.pop(0)
    res.pop(0)
    for item in range(n):
        win = [0, 0]
        mySet = res[item]
        passed = True
        for j in range(len(mySet)):
            s = mySet[j]
            x, y = map(int, s.split(':'))
            passed &= win[0] < 2
            passed &= win[1] < 2
            output, winner = tenis(x, y, j, p, q)
            win[winner] += 1
            passed &= output
        if passed and (win[0] == 2 or win[1] == 2): print('da')
        else: print('ne')

if __name__ == "__main__":
    main(sys.stdin)