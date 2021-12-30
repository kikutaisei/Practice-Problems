class RecursiveFibonacciSequence:
    def calculateNTerm(self, n):
        if n > 2:
            return self.calculateNTerm(n - 1) + self.calculateNTerm(n - 2)
        else:
            return 1

testFibonacci1 = RecursiveFibonacciSequence()
print(testFibonacci1.calculateNTerm(6)) # Prints "8"

testFibonacci2 = RecursiveFibonacciSequence()
print(testFibonacci2.calculateNTerm(10)) # Prints "55"
