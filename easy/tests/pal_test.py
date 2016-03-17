def test(f):
    for i in range(1, 1000):
        result = f(i)
        if result == True:
            print(i)
