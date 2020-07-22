def saveSerialData(data):
    with open("data.txt", "a") as f:
        f.write(data)
        f.close()
