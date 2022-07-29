#!/opt/homebrew/opt/python@3.10/bin/python3

'''
except Exception contains all Python exceptions except for GeneratorExit, KeyboardInterrupt, SystemExit. So if you use this structure, you can still finish your program by means of a keyboard or commands, which causes SystemExit.
'''
number_one = input('\n')
number_two = input('\n')

try:
    result = int(number_two / number_one)

except ZeroDivisionError:
    print('It seems like you are dividing number_two by 0!')
except (ValueError, TypeError):
    print('Looks like you are not using numbers!')

else:
    print(f'The result - rounded down number - is {result}.')

finally:
    print('Thanks for your participation!')

