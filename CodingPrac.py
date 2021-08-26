
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

if __name__ == "__main__":
    a = Solution()

    a.lengthOfLongestSubString('abrkaabcdefghijjxxx')
    print(a.thisTi(5))

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