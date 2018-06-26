# Open a file
fo = open("foo.txt", "w+")

fo.write( "Python is a great language.\nYeah its great!!\n");

# Close opend file
fo.close()

fo = open("foo.txt", "r+")
str_file = fo.read()

print(str_file)

# Close opend file
fo.close()
