"""This is a simple Children's game written in python it will print 'Fizz' when gets a number which is divisible by
3, prints 'Buzz' when gets a number which is divisible by 5 and 'FizzBuzz' when gets a number which is divisible
both by 3 and 5."""

for num in range(1, 101):  # This will print numbers ranging from 1 to 100
    if num % 15 == 0:
        print("Fizz Buzz")  # This will print 'FizzBuzz' in places of number divisible by both 3 and 5
    elif num % 5 == 0:
        print("Buzz")  # This will print 'Buzz' in places of numbers divisible by 5.
    elif num % 3 == 0:
        print("Fizz")  # This will print 'Fizz' in places of numbers divisible by 3.
    else:
        print(num)