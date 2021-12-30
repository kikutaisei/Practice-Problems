class PalindromeChecker:
    def checkPalindrome(self, string, leftPointer, rightPointer):
        if leftPointer <= rightPointer:
            
            if string[leftPointer] == string[rightPointer]:
                return self.checkPalindrome(string, leftPointer + 1, rightPointer - 1)
            else:
                return False
            
        else:
            return True

string1 = "KAYAK"
testPalindrome1 = PalindromeChecker()
print(testPalindrome1.checkPalindrome(string1, 0, len(string1) - 1)) # Prints "True"

string2 = "FALSE"
testPalindrome2 = PalindromeChecker()
print(testPalindrome2.checkPalindrome(string2, 0, len(string2) - 1)) # Prints "False"
