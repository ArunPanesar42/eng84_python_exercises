class FizzBuzz():

    # Initialise fizz and buzz values
    def __init__(self):
        self.fizz = 3
        self.buzz = 5

    # Checks if a number is "fizz"
    def is_fizz(self, num):
        return num % self.fizz == 0

    # Checks if a number is "buzz"
    def is_buzz(self, num):
        return num % self.buzz == 0

    # Checks if a number is "fizzbuzz"
    def is_fizzbuzz(self, num):
        return self.is_fizz(num) and self.is_buzz(num)

    # Generate numbers from 1 to 100 with fizzbuzz
    def gen_100_num(self):
        for num in range(1, 101):  # starts at 1
            if self.is_fizzbuzz(num):
                print("FizzBuzz")
            elif self.is_fizz(num):
                print("Fizz")
            elif self.is_buzz(num):
                print("Buzz")
            else:
                print(num)


# Using the class
fizz_buzz_object = FizzBuzz()
print(fizz_buzz_object.is_fizz(21))
print(fizz_buzz_object.is_buzz(35))
print(fizz_buzz_object.is_fizzbuzz(45))
fizz_buzz_object.gen_100_num()