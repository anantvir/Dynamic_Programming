"""Author - Anantvir Singh, Problem - Leetcode,  Statement = Decoding I"""

number_string = "1012"
s = []
for c in number_string:
    s.append(c)
length = len(s)+1
cnt =[0]*length             # cnt[i] stores length of string considered so far. E.g cnt[2] stores number of decodings till now in string on length 2
cnt[0] = 1
cnt[1] = 1
def Decode(s,cnt):
    n = len(s)
    for i in range(1,n):
        if s[i] > '0':
            cnt[i+1] = cnt[i]
        if s[i] < '7' and (s[i-1] == '2' or s[i-1] == '1'):
            cnt[i+1] += cnt[i]
    return cnt[n]

print('Total Number of Ways to Decode :',Decode(s,cnt))
