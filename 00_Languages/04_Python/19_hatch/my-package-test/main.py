from calc import Operands, add, sub, mul, div

def main():
    a = 10
    b = 2
    print(add(Operands(a=a, b=b)))
    print(sub(Operands(a=a, b=b)))
    print(mul(Operands(a=a, b=b)))
    print(div(Operands(a=a, b=b)))


if __name__ == "__main__":
    main()
