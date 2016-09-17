def sqrt(n):
    return int(n**0.5)

abcSum = 1000
abcPdt = 0

searchRange = [x for x in range(abcSum/2,0,-1)]

for i in searchRange:
    for j in [x for x in searchRange if x<i]:
        k = 1000 - (i + j)
        if k in searchRange and k<j:
            if (i**2) == ((j**2)+(k**2)):
                abcPdt = i*j*k
                print str(i) +"    "+ str(j) +"    "+ str(k)

print abcPdt
