import os
from pyfiglet import Figlet
from sty import fg, bg, ef, rs


"""Convert a decimal number into a binary number
"""
def decToBin(value):
    binary = ''

    explaination = ' ' * 3 + '-' * 14 + fg.li_green + '\n - Decimal to Binary verbose:\n' + fg.rs

    if value == 0:
        return '0'

    # 1. search the biggest exponent
    exponent = 0
    while 2 ** exponent <= value:
        exponent += 1

        if 2 ** (exponent + 1) > value:
            break

    result_1 = 2 ** exponent
    
    # 2. subtract the result of step 1. from value write down a 1
    result_2 = value - result_1
    binary += '1'

    explaination += '2^%s = %s < %s\t| r = %s |\tinterim result: %s\n' % (exponent, result_1, value, result_2, binary)

    # 3. is the next lower expenent in the result of step 2. then write a 1 else a 0
    # 4. repeat like in step 3.
    for i in range(exponent):
        new_exponent = exponent - (i + 1)
        if 2 ** new_exponent > result_2:
            binary += '0'
            i += 1

            explaination += '2^%s = %s > %s\t| r = - |\tinterim result: %s\n' % (new_exponent, 2 ** new_exponent, result_2, binary)
        else:
            binary += '1'
            
            explaination += '2^%s = %s < %s\t| r = %s |\tinterim result: %s\n' % (new_exponent, 2 ** new_exponent, result_2, result_2 - 2 ** new_exponent, binary)
            
            result_2 = result_2 - 2 ** new_exponent
            i += 1

    explaination += ' ' * 3 + '-' * 14 + '\n'

    return binary, explaination


"""The main menu of the app
"""
def menu():
    # Print the header
    figlet = Figlet(font='slant')
    print(fg.yellow + figlet.renderText('NumCalc') + fg.rs)
    print(bg.blue + 'By Bluewolf787 v.BETA-1.0.0' + bg.rs)

    # Print the options
    print(fg.da_cyan + '=' * 33 + fg.rs)
    print(
        '''Which number type you want enter?
    1. Decimal (d)
    2. Binary (b)
    3. Octal (o)
    4. Hexadecimal (h)
    5. quit (q)''')

    # Get user input
    answer = str(get_input())

    print(fg.da_cyan + '=' * 33 + fg.rs)

    if answer.lower() == 'decimal' or answer.lower() == 'd':
        print('\nEnter a decimal number')
        value = int(get_input())
        decToBin_result = decToBin(value)

        binary = decToBin_result[0]
        bin_explaination = decToBin_result[1]

        print('%s\n - Binary result: %s%s%s\n%s' % (fg.li_green, fg.li_red, binary, fg.rs, bin_explaination))
        finish()
    elif answer.lower() == 'quit' or answer.lower() == 'q':
        exit_numcalc()
    else:
        finish()

"""Shown when a operation is finished
"""
def finish():
    print(fg.da_cyan + '=' * 41 + fg.rs + '\nType in c to go back to menu or q to quit')
    answer = str(get_input())

    while answer.lower() != 'c' and answer.lower() != 'q':
        answer = str(get_input())

    if answer.lower() == 'c':
        clear_cli()
        menu()
    elif answer.lower() == 'q':
        exit_numcalc()

"""Get input from the user
"""
def get_input():
    return input(fg.da_magenta + '> ' + fg.rs)

"""Clear the CLI
"""
def clear_cli():
    os.system('cls' if os.name == 'nt' else 'clear')

"""Exit NumCalc
"""
def exit_numcalc():
    clear_cli()
    exit()

if __name__ == '__main__':
    clear_cli()
    menu()