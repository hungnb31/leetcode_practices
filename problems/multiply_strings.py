class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == "0" or num2 == "0":
            return "0"
    
        list1 = []
        for i,v in enumerate(num1):
            x = "0" * (len(num1) - 1 - i)
            list1.append(v + x)
        list2 = []
        for i,v in enumerate(num2):
            x = "0" * (len(num2) - 1 - i)
            list2.append(v + x)
        
        result = 0
        for x in list1:
            for y in list2:
                result += int(x) * int(y)
                
        return str(result)