"""Problem- Leetcode, Statement - Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area."""
# Brute force is O(mn^2) its still acceptable, Dynamic Programming solutions is not as intuitive as Matrix chain, LCS or rod cutting etc.

matrix = [[1,0,1,0,0],[1,0,1,1,1],[1,1,1,1,1],[1,0,0,1,0]]

def Maximal_Square(M):
    rows = len(M)
    columns = len(M[0])
    maxLength = 0
    for i in range(rows):
        for j in range(columns):
            if M[i][j] == 1:
                length = 1
                flag = True
                x = j+1
                y = i+1
                while(flag == True and y < rows and x < columns):
                    if M[y][x] != 1:
                        flag = False
                        break
                    if M[y-1][x] != 1:
                        flag = False
                        break
                    if M[y][x-1] != 1:
                        flag = False
                        break
                    if flag:
                        length += 1
                    x += 1
                    y +=1
                if length > maxLength:
                    maxLength = length
    return maxLength**2

    
print(Maximal_Square(matrix))
