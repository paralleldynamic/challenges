from hashlib import md5

SECRET_KEY = "yzbqklnj"

if __name__ == "__main__":
    i = 1
    while True:
        s = SECRET_KEY + str(i)
        hex = md5(s.encode("utf-8")).hexdigest()
        if hex.startswith("00000"):
            break
        i += 1

    print(f"Part 1: found the correct hex at {i}")

    i = 1
    while True:
        s = SECRET_KEY + str(i)
        hex = md5(s.encode("utf-8")).hexdigest()
        if hex.startswith("000000"):
            break
        i += 1

    print(f"Part 2: found the correct hex at {i}")
