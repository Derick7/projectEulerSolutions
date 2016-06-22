from collections import defaultdict

class ProjectEulerProblem:
    
    title = """Smallest multiple"""
    subTitle = """Problem 5"""
    ProblemStatement = """
    2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

    What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
    """
    def primeFactorsCounted(self,num):
        c = 2
        primeFactorCountDict = defaultdict(int)
        while(num > 1):
            if num % c == 0:
                num = num/c
                primeFactorCountDict[c] += 1
            else:
                c += 1
        return primeFactorCountDict

    def implementation(self):
        limit = 20
        evenlyDivisibleDict = defaultdict(int)
        for i in range(2,limit+1):
            pfc = self.primeFactorsCounted(i)
            for x in pfc:
                if pfc[x] > evenlyDivisibleDict[x]:
                    evenlyDivisibleDict[x]=pfc[x]
        evenlyDivisibleNum = 1
        for x in evenlyDivisibleDict:
            evenlyDivisibleNum *= (x**evenlyDivisibleDict[x])
        print evenlyDivisibleNum

def main():
    ProjectEulerProblem().implementation()

if __name__ == "__main__":
    main()