### COUNTING VOWELS  


vnum = 0
for i in range(len(s)):
    if s[i] in 'aeiou':
        vnum += 1 
        
print 'Number of vowels: ' + str(vnum)



### COUNTING BOBS

maxSubstr = 0
for start in range(len(s)-2):
    if 'bob' == s[start:start+3]:
        maxSubstr += 1

print "Number of times bob occurs is: " + str(maxSubstr)


### ALPHABETICAL SUBSTRINGS

#s = 'abcbcd'
ans = ''
L = []
tempans = ''
for i in range(len(s)):
    tempans = ''
    if i == len(s)-1:
        tempans += s[i]
        break
    else:
        tempans += s[i]
        print tempans
        while s[i] <= s[i+1]:
            tempans += s[i+1]
            i += 1
            if i == len(s)-1:
                break
    L.append(tempans)
    '''
    if len(tempans) > len(ans):
        ans = tempans
    '''
for i in range(len(L)-1,-1,-1):
    if len(L[i]) >= len(ans):
        ans = L[i]

print 'Longest substring in alphabetical order is: ' + ans 