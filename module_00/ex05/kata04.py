# Put this at the top of your kata04.py file
kata = (0, 4, 132.42222, 10000, 12345.67)

def format_index(digit):
    return '0' + str(digit) if digit <= 9 else str(digit)

output = 'module_' + format_index(kata[0]), 'ex_' + format_index(kata[1])
print(*output, sep=', ', end=" ")
print(': {:.2f}, {:.2e}, {:.2e}'.format(kata[2], kata[3], kata[4]))