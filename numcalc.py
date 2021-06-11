import os
from pyfiglet import Figlet
from sty import fg, bg, ef, rs


### DECIMAL

"""Convert a decimal number into a binary number
"""
def decToBin(value):
    bin_num = '0b'

    verbose = fg.li_yellow + ' -' + fg.li_green + ' Decimal to Binary verbose:\n' + fg.rs

    if value == 0:
        return '0', ''

    # 1. search the biggest exponent
    exponent = 0
    while 2 ** exponent <= value:
        exponent += 1

        if 2 ** (exponent + 1) > value:
            break

    result_1 = 2 ** exponent
    
    # 2. subtract the result of step 1. from value write down a 1
    result_2 = value - result_1
    bin_num += '1'

    verbose += '2^%s = %s < %s\t|\tr = %s\t|\tinterim result: %s\n' % (exponent, result_1, value, result_2, bin_num)

    # 3. is the next lower expenent in the result of step 2. then write a 1 else a 0
    # 4. repeat like in step 3.
    for i in range(exponent):
        new_exponent = exponent - (i + 1)
        if 2 ** new_exponent > result_2:
            bin_num += '0'
            i += 1

            verbose += '2^%s = %s > %s\t|\tr = -\t|\tinterim result: %s\n' % (new_exponent, 2 ** new_exponent, result_2, bin_num)
        else:
            bin_num += '1'
            
            verbose += '2^%s = %s < %s\t|\tr = %s\t|\tinterim result: %s\n' % (new_exponent, 2 ** new_exponent, result_2, result_2 - 2 ** new_exponent, bin_num)
            
            result_2 = result_2 - 2 ** new_exponent
            i += 1

    verbose += '\n' + ' ' * 3 + fg.li_cyan + '-' * 35 + fg.rs + '\n'

    return bin_num, verbose

"""Convert decimal into hexadecimal numbers
"""
def decToHex(value):
    hex_num = '0x'

    verbose = fg.li_yellow + ' -' + fg.li_green + ' Decimal to Hexadecimal verbose:\n' + fg.rs

    # 1. Search for the smallest 16 potency which is bigger than value the highest occupied hexadecimal digit is one place below - example: 2345 -> 16³ = 4096 -> 16² = 256
    exponent = 1
    while 16 ** exponent < value:
        exponent += 1
    
    exponent -= 1

    # 2. Divide value by the highest hexadecimal digit the integer result is the wanted digit on the first place keep calculating with the rest- example: 2345 / 256 = 9, r = 41, interim result = 9
    # From 10 hex values are written as A - F
    # 3. Repeat step 2. until 16⁰ - example: 41 / 16 = 2, r = 9, , interim result = 92
    # The rest 9 can written down just like that because it's a ones-digit - example: final result = 929
    integer  = 0
    for i in range(exponent + 1):
        verbose_helper = value
        
        integer = int(value / 16 ** exponent)
        value %= 16 ** exponent

        if integer == 10:
            hex_num += 'A'
        elif integer == 11:
            hex_num += 'B'
        elif integer == 12:
            hex_num += 'C'
        elif integer == 13:
            hex_num += 'D'
        elif integer == 14:
            hex_num += 'E'
        elif integer == 15:
            hex_num += 'F'
        else:
            hex_num += str(integer)

        verbose += '16^{0} = {1}\t|\t{2} / {1} = {3}\t|\tr = {4}\t|\tinterim result: {5}\n'.format(exponent, 16 ** exponent, verbose_helper, integer, value, hex_num)

        exponent -= 1

    verbose += '\n' + ' ' * 3 + fg.li_cyan + '-' * 35 + fg.rs + '\n'

    return hex_num, verbose

"""Convert decimal numbers into octal numbers
"""
def decToOct(value):
    oct_num  = '0o'
    verbose = fg.li_yellow + ' -' + fg.li_green + ' Decimal to Octal verbose:\n' + fg.rs

    exponent = 1
    while 8 ** exponent < value:
        exponent += 1

    exponent -= 1

    integer = 0
    for i in range(exponent + 1):
        verbose_helper = value

        integer = int(value / 8 ** exponent)
        value %= 8 ** exponent

        oct_num += str(integer)

        verbose += '8^{0} = {1}\t|\t{2} / {1} = {3}\t|\tr = {4}\t|\tinterim result: {5}\n'.format(exponent, 8 ** exponent, verbose_helper, integer, value, oct_num)

        exponent -= 1

    verbose += '\n' + ' ' * 3 + fg.li_cyan + '-' * 35 + fg.rs + '\n'

    return oct_num, verbose


### BINARY

"""Convert binary numbers into decimal numbers
"""
def binToDec(value):
    dec_num = 0
    verbose = fg.li_yellow + ' -' + fg.li_green + ' Binary to Decimal verbose:\n' + fg.rs

    # Find all 1's and there position and add those like 2⁰ + 2¹ + 2² + 2³ + ...
    value = value.lstrip('0')
    i = 0
    for c in reversed(value):
        if c == '1':
            dec_num += 2 ** i

            if i + 1 == len(value):
                verbose += '2^%d = %d\n' % (i, dec_num)
            else:
                verbose += '2^%d + ' % i

            i += 1
        else:
            i += 1

    verbose += '\n' + ' ' * 3 + fg.li_cyan + '-' * 35 + fg.rs + '\n'

    return dec_num, verbose

"""Convert binary numbers into octal numbers
"""
def binToOct(value):
    oct_num = '0o'
    bin_split = []
    verbose = fg.li_yellow + ' -' + fg.li_green + ' Binary to Octal verbose:\n' + fg.rs + 'Binary\tOctal\tinterim result\n'

    oct_table = {'000': '0', '001': '1', '010': '2', '011': '3', '100': '4', '101': '5', '110': '6', '111': '7'}

    # Split the binary number into blocks with 3 digits
    value = value.lstrip('0')
    while value != '':
        bin_split.append(value[-3:])
        value = value[:-3]

    for i in reversed(bin_split):
        # Fill up those blocks without 3 digits with 0's
        current_block = i.rjust(3, '0')

        # Search the Octal number to all blocks
        oct_num += oct_table[current_block]

        verbose += '{0}\t{1}\t{2}\n'.format(current_block, oct_table[current_block], oct_num)

    verbose += '\n' + ' ' * 3 + fg.li_cyan + '-' * 35 + fg.rs + '\n'

    return oct_num, verbose

"""Convert binary numbers into hexadecimal numbers
"""
def binToHex(value):
    hex_num = '0x'
    bin_split = []
    verbose = fg.li_yellow + ' -' + fg.li_green + ' Binary to Hexadecimal verbose:\n' + fg.rs + 'Binary\tHexadecimal\tinterim result\n'

    hex_table = {'0000': '0', '0001': '1', '0010': '2', '0011': '3', '0100': '4', '0101': '5', '0110': '6', '0111': '7', '1000': '8', '1001': '9', '1010': 'A', '1011': 'B', '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'}

    # Split the binary number into blocks with 4 digits
    value = value.lstrip('0')
    while value != '':
        bin_split.append(value[-4:])
        value = value[:-4]

    for i in reversed(bin_split):
        # Fill up those blocks without 4 digits with 0's
        current_block = i.rjust(4, '0')

        # Search the Hex number to all blocks
        hex_num += hex_table[current_block]

        verbose += '{0}\t{1}\t\t{2}\n'.format(current_block, hex_table[current_block], hex_num)

    verbose += '\n' + ' ' * 3 + fg.li_cyan + '-' * 35 + fg.rs + '\n'

    return hex_num, verbose


### OCTAL

"""Convert octal numbers into decimal numbers
"""
def octToDec(value):
    dec_num = 0
    verbose = fg.li_yellow + ' -' + fg.li_green + ' Octal to Decimal verbose:\n' + fg.rs

    position = 0
    for digit in reversed(str(value)):
        dec_num += (8 ** position) * int(digit)

        if position + 1  == len(str(value)):
            verbose += '8^%d * %s = %d\n' % (position, digit, dec_num)
        else:
            verbose += '8^%d * %s + ' % (position, digit)

        position += 1

    verbose += '\n' + ' ' * 3 + fg.li_cyan + '-' * 35 + fg.rs + '\n'

    return dec_num, verbose

"""Convert octal numbers into binary numbers
"""
def octToBin(value):
    bin_num = ''
    verbose = fg.li_yellow + ' -' + fg.li_green + ' Octal ti Binary verbose:\n' + fg.rs + 'Octal\tBinary\tinterim result\n'

    bin_table = {0: '000', 1: '001', 2: '010', 3: '011', 4: '100', 5: '101', 6: '110', 7: '111'}
    oct_split = []
    for digit in str(value):
        oct_split.append(int(digit))

    for i in oct_split:
        bin_num += bin_table[i]

        verbose += '{0}\t{1}\t{2}\n'.format(i, bin_table[i], bin_num.lstrip('0'))

    verbose += '\n' + ' ' * 3 + fg.li_cyan + '-' * 35 + fg.rs + '\n'

    return bin_num.lstrip('0'), verbose


### Menus

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
    answer = str(get_input()).lower()

    print(fg.da_cyan + '=' * 33 + fg.rs)

    if answer == 'decimal' or answer == 'd':
        print('\nEnter a decimal number')
        value = 0
        while True:
            try:
                value = int(get_input())
                break
            except ValueError:
                print(bg.red + 'Invalid decimal number' + bg.rs)

        # Decimal into Binary
        decToBin_result = decToBin(value)
        bin_num = decToBin_result[0]
        bin_verbose = decToBin_result[1]
        print('%s\n - %sBinary result: %s%s%s\n%s' % (fg.li_yellow, fg.li_green, fg.li_red, bin_num, fg.rs, bin_verbose))

        # Decimal into Octal
        decToOct_result = decToOct(value)
        oct_num = decToOct_result[0]
        oct_verbose = decToOct_result[1]
        print('%s - %sOctal result: %s%s%s\n%s' % (fg.li_yellow, fg.li_green, fg.li_red, oct_num, fg.rs, oct_verbose))


        # Decimal into Hexadecimal
        decToHex_result = decToHex(value)
        hex_num = decToHex_result[0]
        hex_verbose = decToHex_result[1]
        print('%s - %sHexadecimal result: %s%s%s\n%s' % (fg.li_yellow, fg.li_green, fg.li_red, hex_num, fg.rs, hex_verbose))

        finish()
    elif answer == 'binary' or answer == 'b':
        print('\nEnter a binary number')
        value = ''
        while True:
            is_valid = True
            value = str(get_input())
            for i in value:
                if i != '0' and i != '1':
                    print(bg.red + 'Invalid binary number' + bg.rs)
                    is_valid = False
            if is_valid:
                break

        binToDec_result = binToDec(value)
        dec_num = binToDec_result[0]
        dec_verbose = binToDec_result[1]
        print('%s\n - %sDecimal result: %s%s%s\n%s' % (fg.li_yellow, fg.li_green, fg.li_red, dec_num, fg.rs, dec_verbose))

        binToOct_result = binToOct(value)
        oct_num = binToOct_result[0]
        oct_verbose = binToOct_result[1]
        print('%s - %sOctal result: %s%s%s\n%s' % (fg.li_yellow, fg.li_green, fg.li_red, oct_num, fg.rs, oct_verbose))

        binToHex_result = binToHex(value)
        hex_num = binToHex_result[0]
        hex_verbose = binToHex_result[1]
        print('%s - %sHexadecimal result: %s%s%s\n%s' % (fg.li_yellow, fg.li_green, fg.li_red, hex_num, fg.rs, hex_verbose))

        finish()
    elif answer == 'octal' or answer == 'o':
        print('\nEnter a octal number')
        value = 0
        while True:
            is_valid = True
            try:
                value = int(get_input())
                for d in str(value):
                    if int(d) >= 0 and int(d) <= 7:
                        break
                    else:
                        is_valid = False
                        print(bg.red + 'Invalid octal number' + bg.rs)
                        break
            except ValueError:
                print(bg.red + 'Invalid octal number' + bg.rs)
                is_valid = False

            if is_valid:
                break

        octToDec_result = octToDec(value)
        dec_num = octToDec_result[0]
        dec_verbose = octToDec_result[1]
        print('%s\n - %sDecimal result: %s%s%s\n%s' % (fg.li_yellow, fg.li_green, fg.li_red, dec_num, fg.rs, dec_verbose))
        
        octToBin_result = octToBin(value)
        bin_num = octToBin_result[0]
        bin_verbose = octToBin_result[1]
        print('%s - %sBinary result: %s%s%s\n%s' % (fg.li_yellow, fg.li_green, fg.li_red, bin_num, fg.rs, bin_verbose))


        finish()
    elif answer == 'quit' or answer == 'q':
        exit_numcalc()
    else:
        finish()

"""Shown when a operation is finished
"""
def finish():
    print(fg.da_cyan + '=' * 41 + fg.rs + '\nType in c to go back to menu or q to quit')
    answer = str(get_input()).lower()

    while answer != 'c' and answer != 'q':
        answer = str(get_input())

    if answer == 'c':
        clear_cli()
        menu()
    elif answer == 'q':
        exit_numcalc()


### Utilites

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