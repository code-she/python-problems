def boxprint(symbol, width, height):
    print(symbol*width)


    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)

    print(symbol * width)

boxprint('*', 15, 5)
