# I,m write some way for sumertion numbers


# __________first solution__________


def sumeration():
     num1 = float(input('Enter First Number: '))
     num2 = float(input('Enter Secend Number: '))

     sum = (num1 + num2)
     print(sum)

sumeration()


# ___________Secend Solution_________


def getNumber(num1, num2):
     sum = (num1 + num2)
     print(sum)

getNumber(10, 10.5)


# ___________threed solution__________


class sumertion :
     def get_all_numbers():
          num1 = float(input("Enter Number: "))
          num2 = float(input("Enter Number: "))

          sum = (num1 + num2)

          if sum is not None:
               'Moshkeli pish omade !'
          print(sum)
     get_all_numbers()


# ___________fourd solution___________


class Summation:
    def get_all_numbers(self):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        result = num1 + num2
        
        if result is not None:  
            print(result)
        else:
            print('Moshkeli pish amade!')

my_summation = Summation()
my_summation.get_all_numbers()
