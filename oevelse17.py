from os.path import exists

from_file = "test.txt"
to_file = "new_test.txt"

# we could do these two on one line, how?
in_file = open(from_file) ; indata = in_file.read()

out_file = open(to_file, 'w')
out_file.write(indata)