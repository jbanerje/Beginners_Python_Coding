#File IO Operation
import os

# This would give location of the current directory
curr_dir = os.getcwd();
print ("Current Directory : ", curr_dir)

# Open a file
fo = open("test.txt", "r+")
str = fo.read(10);
print ("Read String is : ", str)

# Check current position
position = fo.tell();
print ("Current file position : ", position)

# Reposition pointer at the beginning once again
position = fo.seek(0, 0);
str = fo.read(10);
print ("Again read String is : ", str)
# Close opend file
fo.close()
