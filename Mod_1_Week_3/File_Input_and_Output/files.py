'''
# r = Read
# a = Append
# w = Write
# x = Exclusive creation (fails if file exists)
'''

# Read - error if file does not exist

f = open('names.txt', 'r')
# print(f.read())
# print(f.read(4))

# print(f.readline())
# print(f.readline())
# Reads a single line

for line in f:
    print(line)
    
f.close()

# try:
#     f = open("names.txt")
#     print(f.read())
# except: 
#     print("File does not exist")
# finally:
#     f.close()

# Append - create file if it does not exist
f = open('names.txt', 'a')
f.write("Neil\n")
f.close()

f = open('names.txt')
print(f.read())
f.close()

#Write (Overwrite)
f = open('context.txt', 'w')
f.write('I deleted everything in this file')
f.close()

f= open('context.txt')
print(f.read())
f.close()

