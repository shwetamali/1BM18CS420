def gameboard(size):
    for x in range(size):
        for y in range(size*(size-1)+1):
            if(y%size!=0 and y != size):
                print("-",end="")
            else:
                print(" ",end="")
        print('')
        if x != (size-1):
            for i in range(size*(size-1)+1):
                if i%size == 0:
                    print("|",end="")
                else:
                    print(" ",end="")
                
            print('')
size= int(input("Enter the size of game board : "))
gameboard(size)
