def decToBin(value):
    binary = ''

    # 1. search the biggest exponent
    exponent = 0
    while 2 ** exponent < value:
        exponent += 1

        if 2 ** (exponent + 1) > value:
            break

    result_1 = 2 ** exponent
    
    # 2. subtract the result of step 1. from value write down a 1
    result_2 = value - result_1
    binary += '1'

    # 3. is the next lower expenent in the result of step 2. then write a 1 else a 0
    # 4. repeat like in step 3.
    for i in range(exponent):
        new_exponent = exponent - (i + 1)
        if 2 ** new_exponent > result_2:
            binary += '0'
            i += 1
        else:
            binary += '1'
            result_2 = result_2 - 2 ** new_exponent
            i += 1

    return binary


print('NumCalc by Bluewolf787\n')

value = int(input('Enter a dec num: '))

binary = decToBin(value)

print('\nBinary result: %s' % binary)