# TRY CASE
try:
    f = open('text.txt', 'w')
    f.write("Writing Data to file")
except IOError:
    print("Error: can\'t find file or read data")
else:
    # else will work only if try is executed
    print("Written content in the file successfully")
    f.close()

# EXCEPT CASE

try:
    f = open('text.txt', 'r')
    f.write("Writing Data to file")
except:
    # wxcept block will work for any error caught other than any happened in "try" block
    print("Error: can\'t find file or read data")
else:
    # else will work only if try is executed
    print("Written content in the file successfully")
    f.close()

# FINALLY CASE
try:
    f = open('text.txt', 'w')
    f.write("Writing Data to file")
except IOError:
    print("Error: can\'t find file or read data")
finally:
    # will execute after every possible case 
    print("PROGRAM WORKED")
