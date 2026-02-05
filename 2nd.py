count = 0
with open("hello.py", "r") as file:
    data = file.read()
    count += len(data.split())
    print(f"The number of words in hello.py is: {count}")