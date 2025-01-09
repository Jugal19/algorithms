###############################################################################################################
# Name: Jugal Patel
# File Name: main.py
# Description: Implement a function that returns the minimum number of scalar multiplications needed
#              to compute the mulitplication of n Matrices A1 * A2 * ... * An. The function takes the
#              matrices' dimensions as an array.
#              
#              Use the function to return the minimum number of scalar multiplications of the following
#              matrices A1 * A2 * A3 * A4:
#
#              A1 = [3 by 7]
#              A2 = [7 by 4]
#              A3 = [4 by 5]
#              A4 = [5 by 2]
#
# Date Started: October/19/2024 at 12:00 pm
# Date Completed: October/19/2024 at 1:18 pm
###############################################################################################################

def matrix_chain_order(p):

    n = len(p) - 1 # is the number of spaces in a matrix
    m = [[0] * n for i in range(n)] 
    s = [[0] * n for i in range(n)] 

    # created a for loop to calculate the minimum number of scalar multiplications
    for i in range(1, n):
        m[i][i] = 0

    for l in range(2, n + 1):
        for i in range(1, n - l + 2):
            j = i + l - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k
    return m, s # returns the minimum number of scalar multiplications
