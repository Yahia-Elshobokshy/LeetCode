class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Define a string of punctuations to remove
        punctuations = '''!()-[]{};:'`"\,<>./?@#$%^&*_~'''

        # Use a list comprehension to filter out the punctuations and join the result
        result = "".join([c.lower() for c in s if c not in punctuations])
        
        # Replace white spaces to join words
        result = result.replace(" ", "")
        
        # Call the helper chechPalindrome function
        # We pass the result string, and the start and end of the string
        return self.checkPalindrome(result, 0, len(result) - 1)

    def checkPalindrome(self, s, l, r):

        # Base condition to check when the left and right
        # pointers have no more elements to check
        if l >= r:
            return True

        # If there is one occurrence where the characters are not equal
        # return false
        if s[l] != s[r]:
            return False

        # Increment left pointer
        # Decrement right pointer
        # Call the function recursively
        # Return the final output
        return self.checkPalindrome(s, l+1, r-1)
