#1から100までの整数
#3で割れるとFizz
#5で割れるとBuzz
#3と5で割れるとFizzBuzz
x = ["FizzBuzz" if i % 3 == 0 and i % 5 == 0 else "Fizz" if i % 3 == 0 else "Buzz" if i % 5 == 0 else i for i in range(1,101)]
print(x)
