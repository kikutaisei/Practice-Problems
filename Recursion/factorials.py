class Factorial:
    def calculateFactorial(self, n):
        if n >= 1:
            return n * self.calculateFactorial(n - 1)
        else:
            return 1

factorialTest1 = Factorial()
print(factorialTest1.calculateFactorial(4)) # Prints "24"

factorialTest2 = Factorial()
print(factorialTest2.calculateFactorial(3)) # Prints "6"
