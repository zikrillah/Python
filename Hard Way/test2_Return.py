#Setiap fungsi pada python selalu memberikan nilai balikan jika tidak ada akan mengembalikan nilai None

def printAndReturnNothing():
    x = "hello"
    print(x)

def printAndReturn():
    x = "hello"
    print(x)
    return x #Return dikembalikan ke object

def main():
    ret = printAndReturn()
    other = printAndReturnNothing() #Pembentukan objec

    print "ret is: %s" % ret
    print "other is: %s" % other

if __name__ == "__main__":
    main()
