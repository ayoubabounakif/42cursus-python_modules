# Put this at the top of your kata02.py file
kata = (2019, 9, 25, 3, 30)

def format_index(digit):
    return '0' + str(digit) if digit <= 9 else str(digit)

print(format_index(kata[1]), format_index(kata[2]), format_index(kata[0]), sep='/', end=" ")
print(format_index(kata[3]), format_index(kata[4]), sep=':')
