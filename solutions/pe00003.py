class ProjectEulerProblem:
    
    title = """Largest prime factor"""
    subTitle = """Problem 3 """
    ProblemStatement = """
    The prime factors of 13195 are 5, 7, 13 and 29.

    What is the largest prime factor of the number 600851475143 ?
    """
    def largestPrimeFactors(self,n):
        factors = set()
        count = 2
        while n>1:
            if  n%count == 0:
                n /= count
                factors.add(count)
            else:
                count +=1
        print "Prime factors = " + str([x for x in factors])
        print "Largest Prime Factor = " + str(count)

    def implementation(self):
        num = 600851475143
        self.largestPrimeFactors(num)


def main():
    ProjectEulerProblem().implementation()

if __name__ == "__main__":
    main()