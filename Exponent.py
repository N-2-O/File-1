while True:
    n = int(input('Number: '))
    e = int(input('Exponent: '))
    total = n
    while e > 1:
        total = total * n
        e = e - 1
    print(total)
        
