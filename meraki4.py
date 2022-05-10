f = open("demofile.txt", "r")
for x in f:
  print(x) 

  f = open("demofile.txt", "r")
print(f.readline())
f.close()