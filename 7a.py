def overlapping():
    file1=open("/home/bmsce/Desktop/happy.txt","r")
    file2=open("/home/bmsce/Desktop/prime.txt","r")
    if file1 and file2:
        str1=file1.read()
        str2=file2.read()
        l1=str1.split(',')
        l2=str2.split(',')
        print("Overlapped numbers are:")
        for i in l1:
            for j in l2:
                if i==j:
                        print(j)
        file1.close()
        file2.close()
overlapping()


****************************OUTPUT*******************************
Overlapped numbers are:
 7
 13
 19
 23
 31
 79
 97
 103
 109
 139
 167
 193
 239
 263
 293
 313
 331
 367
 379
 383
 397
 409
 487
 563
 617
 653
 673
 683
 709
 739
 761
 863
 881
 907
 937
