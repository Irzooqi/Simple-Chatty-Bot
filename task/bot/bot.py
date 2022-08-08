def greet(bot_name, birth_year):
    print('Hello! My name is ' + bot_name + '.')
    print('I was created in ' + birth_year + '.')


def remind_name():
    print('Please, remind me your name.')
    name = input()
    print('What a great name you have, ' + name + '!')


def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print("Your age is " + str(age) + "; that's a good time to start programming!")


def count():
    print('Now I will prove to you that I can count to any number you want.')

    num = int(input())
    curr = 0
    while curr <= num:
        print(curr, '!')
        curr = curr + 1


def test():
    print("Let's test your programming knowledge.")
    print("what is the use of a function?")
    print("1. it's used for fun")
    print("2. functions can make the code nicer!")
    print("3. functions save time and effort in programming!")
    x = int(input())
    if x == 3:
        print('Completed, have a nice day!')
    else:
        print("please, try again")


def end():
    print('Congratulations, have a nice day!')


greet('Damon', '2022')  # change it as you need
remind_name()
guess_age()
count()
test()
end()
