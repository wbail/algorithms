#link:https://leetcode.com/problems/matrix-diagonal-sum/
#id:1572

"""
Runtime: 88 ms, faster than 70.47% of Python online submissions for Matrix Diagonal Sum.
Memory Usage: 13.7 MB, less than 19.29% of Python online submissions for Matrix Diagonal Sum.

"""

class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        
        #print('mat', mat)
        
        if len(mat) == 1:
            
            return mat[0][0]
        
        count = (len(mat) - 1)
        result = 0
        
        """
            0 1 2 3
            -------
        0 [[7,3,1,9],
        1  [3,4,6,9],
        2  [6,9,6,6],
        3  [9,5,8,5]]
        """
        
        
        for i in range(len(mat)):

            #print('i:', i)

            for j in range(len(mat)):

                #print('j:', j)

                if i == j:

                    #print('i =', i, '| j =', j, 'mat[i][j]:', mat[i][j])

                    result = result + mat[i][j]

                if j == count:
                    result = result + mat[i][j]
                    count = count - 1
        

        if len(mat) % 2 != 0:
            result = result - (mat[len(mat) // 2][len(mat) // 2])
            #print('result:', result)
    
        return result