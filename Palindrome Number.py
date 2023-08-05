class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        temp = x
        revnum = 0
        while temp != 0:
            digit = temp % 10
            revnum = revnum * 10 + digit
            temp//=10
        if(revnum == x):
            return True
        else:
            return False
