a= int(input("Enter 1 or 2 to select the pattern : "))
def lowerTri():
    for i in range(5, 0, -1):
        for j in range(0, 5-i):
            print(end=" ")
        for j in range(0, i):
            print("*", end=" ")
        print()
def upperTrin():
        k = 4
        for i in range(1, 5):
            for j in range(1, k):
                print(end=" ")
            k = k - 1
            for j in range(0, i+1):
                print("- ", end="")
            print("\r") 
if a==1:
    lowerTri()
    upperTrin()   
elif a==2:
    lowerTri()
else:
    print('Invalid Input')

