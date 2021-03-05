
def xiecheng(func):

    def warpper():
        result = func()
        next(result)
        return result
    return warpper

def yield_test():
    vegetables = []
    while True:
        food = yield vegetables
        if food is None:
            break
        vegetables.append(food)

        print(f"elements in foodlist are:{vegetables}")


@xiecheng
def proxy_gen():

    vegetables = yield from yield_test()
    print(f"final elements in foodlist are{vegetables}")
    yield

def main():
    g = proxy_gen()

    print(g.send(1))
    print(g.send(2))
    print(g.send(3))
    g.send(None)


if __name__ == '__main__':
    main()





