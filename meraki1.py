
with open("demofile.txt","w") as f:
    f.write("hi my name is soni")
    f.write("i am 19 years old")
    f.write("i am in BA second year")
    f.write("right now i amm in banglore")
    f.write("persuing software programming")
    f.write("hi my name is soni")
    f.close()

f = open("demofile.txt", "r")
# print(f.read())
print(f.readable())
# print(f.readline())