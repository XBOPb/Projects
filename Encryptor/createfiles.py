x = range(5)
n = 1
for i in x:
    with open("text" + str(n) +".txt" , "w") as file:
        file.write(str(n))
        n += 1
