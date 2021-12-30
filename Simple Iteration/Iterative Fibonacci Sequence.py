class IterativeFibonacci:
    def calculateNTerm(self, n):
        if n > 2:
            leftValue = 1
            rightValue = 1
            
            for i in range(n - 2):
                currentLeftValue = rightValue
                currentRightValue = leftValue + rightValue
                
                leftValue = currentLeftValue
                rightValue = currentRightValue

            return rightValue        
                
        else:
            return 1

testFibonacci1 = IterativeFibonacci()
print(testFibonacci1.calculateNTerm(6)) # Prints "8"

testFibonacci2 = IterativeFibonacci()
print(testFibonacci2.calculateNTerm(10)) # Prints "55"
