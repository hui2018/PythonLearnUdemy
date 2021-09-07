
class ListNodes(object):
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution:
    def addingNumbers(self, l1, l2, c=0):
        answer = None
        carryOver = 0
        while(l1 != None):
            adding = l1.val + l2.val + carryOver
            carryOver = 0
            if(adding >= 10):
                adding = adding%10
                carryOver = 1
            temp = ListNodes(adding)
            if(answer == None):
                answer = temp
                tail = answer
            else:
                tail.next = temp
                tail = tail.next
            l1 = l1.next
            l2 = l2.next
        if(carryOver > 0):
            temp = ListNodes(carryOver)
            tail.next = temp
            tail = tail.next
        return answer
    def lengthOfLongestSubString(self, s):
        answer = 0
        answer1 = 0
        pre = ""
        for a in s:
            if pre == "":
                pre = a
                answer = 1;
                continue
            if pre != a:
                answer = answer + 1
                pre = a
            else:
                if answer1<answer:
                    answer1 = answer
                answer = 1
                pre = a
        print(answer1)

    def thisTi(self, n):
        if n == 1:
            return n
        else:
            return n * self.thisTi(n - 1)

    def getRange(self, arr, target):
        answer = [None] * 2
        for x in range(len(arr)):
            if(target == arr[x]):
                if(answer[0] is None):
                    answer[0] = x
                    continue
                answer[1] = x
            elif(answer[0] != None and answer[1] != None):
                return answer
        return answer

    def isValid(self,s):
        stack = []
        for x in range(len(s)):
            if(s[x] == '(' or s[x] == '[' or s[x] == '{'):
                stack.append(s[x])
                continue
            else:
                check = stack.pop()
                if(check == '{' and s[x] =='}'):
                    continue
                elif(check == '(' and s[x] ==')'):
                    continue
                elif(check == '[' and s[x] ==']'):
                    continue
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False

    def twoSum(self, list, k):
        hashMap = {}
        for a in range(len(list)):
            if k-list[a] in hashMap:
                return True
            hashMap[list[a]] = a

        return False

    def stairs(self, k):
        if k<3:
            return k
        current = 0
        pre1 = 1
        pre2 = 2
        for i in range(2, k):
            current = pre1+pre2
            pre1 = pre2
            pre2 = current
        return current

if __name__ == "__main__":
    a = Solution()

    #print length of longest substring
    a.lengthOfLongestSubString('abrkaabcdefghijjxxx')

    #fibonacci number
    print(a.thisTi(5))

    #first and last indices of an element
    array = [1,2,2,2,2,3,4,7,8,8]
    x = 2
    print(a.getRange(array, x))

    #isValid parentheses
    s = "()(){(())" #false
    print(a.isValid(s))
    s = "" #true
    print(a.isValid(s))
    s = "([{}])()" #true
    print(a.isValid(s))

    #adding two linked list
    #2->4->3 + 5->6->8 = 7->0->2->1
    l1 = ListNodes(2)
    l1.next = ListNodes(4)
    l1.next.next = ListNodes(3)
    l2 = ListNodes(5)
    l2.next = ListNodes(6)
    l2.next.next = ListNodes(8)
    result = a.addingNumbers(l1,l2)
    while result:
        print(result.val)
        result = result.next

    #two sum
    print(a.twoSum([4, 7, 1, -3, 2], 0))
    print(a.twoSum([4, 7, 1, -3, 2], 6))
    print(a.twoSum([4, 7, 1, -3, 2], 8))

    print(a.stairs(4))
    print(a.stairs(5))