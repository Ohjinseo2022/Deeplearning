import qrcode

file_path = r"qr.txt"
with open(file_path, "rt", encoding="UTF8") as f:
    read_lines = f.readlines()

    for line in read_lines:
        line = line.strip()
        print(line)
