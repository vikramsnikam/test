class Solution:
    def checkStatus(self, a, b, flag):

        if ((a < 0 and b < 0) and flag == True):
            return True

        elif ((a > 0) and (b > 0) and flag == False):
            return True

        elif ((a > 0) and (b > 0) and flag == False):
            return True

        else:
            return True


obj = Solution()
obj.checkStatus(5, 10, True)
