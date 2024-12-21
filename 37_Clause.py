try:
    l = [1, 3 ,5, 8]
    i = int(input("Enter the index:"))
    print(l[i])
except:
    print("Some error occured")
finally:
    print("I am always executed")