def main():
    str1 = "010203040506070809"
    str2 = "123456789"
    str3 = str2.replace("123", "000")
    str4 = "liujiajun_junw"
    str5 = str4.upper()
    str6 = "-".join(str1)
    str7 = "".join(reversed(str4))
    str8 = str4.split("_")
    print(f"str1={str1}")  # str1=010203040506070809
    print(f"str2={str2}")  # str2=123456789
    print(f"str3={str3}")  # str3=000456789
    print(f"str4={str4}")  # str4=liujiajun_junw
    print(f"str5={str5}")  # str5=LIUJIAJUN_JUNW
    print(f"str6={str6}")  # str6=0-1-0-2-0-3-0-4-0-5-0-6-0-7-0-8-0-9
    print(f"str7={str7}")  # str7=wnuj_nujaijuil
    print(f"str8={str8}")  # str8=['liujiajun', 'junw']


if __name__ == '__main__':
    main()
