with open("cube.stl", "rb") as f:
    f.read(80)
    n = int.from_bytes(f.read(4), byteorder="little")
    print(n)
    for i in range(n):
        data = []
        for i in range(4):
            x = int.from_bytes(f.read(4), byteorder="little")
            y = int.from_bytes(f.read(4), byteorder="little")
            z = int.from_bytes(f.read(4), byteorder="little")
            data.append((x, y, z))
        print(data)
        check = int.from_bytes(f.read(2), byteorder="little")
        if not check == 0:
            print("Error")
            break