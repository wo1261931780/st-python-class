def main():
    n1 = 10
    n2 = 15
    ch = ''
    for i in range(10):
        print("菜单输入一个操作符：+，-，*，/")
        ch = input()
        print(f"ch={ch}")
        if ch == "+":
            print(f"sum={n1 + n2}")
        elif ch == "-":
            print(f"substrate={n1 - n2}")
        elif ch == "/":
            print(f"divide={n1 / n2}")
        elif ch == "*":
            print(f"product={n1 * n2}")
        elif ch == "q":
            print("exit code:q")
            break
        else:
            print("error string")


if __name__ == '__main__':
    main()
