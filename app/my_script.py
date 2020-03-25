def enlarge(i):
    return i*100


## Remove from the global scope in order to import other things from this script
#my_number = float(input("Please input a number:"))
#
#n = str(enlarge(my_number))
#print("Enlarding the number:" + n)

if __name__ == "__main__":
    #only run this if invoved from command line, not if imported from another file
    my_number = float(input("Please input a number:"))
    n = str(enlarge(my_number))
    print("Enlarding the number:", n)