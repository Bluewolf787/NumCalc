import os
from pyfiglet import Figlet
from sty import fg, bg, ef, rs


"""Convert a decimal number into a binary number
"""
def decToBin(value):
    binary = ''

    verbose = fg.li_yellow + ' -' + fg.li_green + ' Decimal to Binary verbose:\n' + fg.rs

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

    verbose += '2^%s = %s < %s\t| r = %s |\tinterim result: %s\n' % (exponent, result_1, value, result_2, binary)

    # 3. is the next lower expenent in the result of step 2. then write a 1 else a 0
    # 4. repeat like in step 3.
    for i in range(exponent):
        new_exponent = exponent - (i + 1)
        if 2 ** new_exponent > result_2:
            binary += '0'
            i += 1

            verbose += '2^%s = %s > %s\t| r = - |\tinterim result: %s\n' % (new_exponent, 2 ** new_exponent, result_2, binary)
        else:
            binary += '1'
            
            verbose += '2^%s = %s < %s\t| r = %s |\tinterim result: %s\n' % (new_exponent, 2 ** new_exponent, result_2, result_2 - 2 ** new_exponent, binary)
            
            result_2 = result_2 - 2 ** new_exponent
            i += 1

    verbose += ' ' * 3 + fg.li_cyan + '-' * 35 + fg.rs + '\n'

    return binary, verbose

"""Convert binary numbers into decimal numbers
"""
def binToDec(value):
    decimal = 0

    verbose = fg.li_yellow + '\n -' + fg.li_green + ' Binary to Decimal verbose:\n' + fg.rs

    # Find all 1's and there position and add those like 2⁰ + 2¹ + 2² + 2³ + ...
    i = 0
    for c in reversed(value):
        if c == '1':
            decimal += 2 ** i

            if i + 1 == len(value):
                verbose += '2^%d = %d\n' % (i, decimal)
            else:
                verbose += '2^%d + ' % i

            i += 1
        else:
            i += 1

    verbose += ' ' * 3 + fg.li_cyan + '-' * 35 + fg.rs + '\n'

    return decimal, verbose


"""The main menu of the app
"""
def menu():
    # Print the header
    figlet = Figlet(font='slant')
    print(fg.yellow + figlet.renderText('NumCalc') + fg.rs)
    print(bg.blue + 'By Bluewolf787 v.BETA-1.0.0' + bg.rs)

    # Print the options
    print(fg.da_cyan + '=' * 33 + fg.rs)
    print('Which number type you want enter?\n' + fg.li_yellow + '\t1.' + fg.rs + ' Decimal (d)\n' + fg.li_yellow + '\t2.' + fg.rs + ' Binary (b)\n' + fg.li_yellow + '\t3.' + fg.rs + ' Octal (o)\n' + fg.li_yellow + '\t4.' + fg.rs + ' Hexadecimal (h)\n' + fg.li_yellow + '\t5.' + fg.rs + ' quit (q)')

    # Get user input
    answer = str(get_input())

    print(fg.da_cyan + '=' * 33 + fg.rs)

    if answer.lower() == 'decimal' or answer.lower() == 'd':
        print('\nEnter a decimal number')
        value = int(get_input())
        decToBin_result = decToBin(value)

        binary = decToBin_result[0]
        bin_verbose = decToBin_result[1]

        print('%s\n - %sBinary result: %s%s%s\n%s' % (fg.li_yellow, fg.li_green, fg.li_red, binary, fg.rs, bin_verbose))
        finish()
    elif answer.lower() == 'binary' or answer.lower() == 'b':
        print('\nEnter a binary number')
        value = str(get_input())
        binToDec_result = binToDec(value)
        decimal = binToDec_result[0]
        dec_verbose = binToDec_result[1]

        print('%s\n - %sDecimal result: %s%s%s\n%s' % (fg.li_yellow, fg.li_green, fg.li_red, decimal, fg.rs, dec_verbose))
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