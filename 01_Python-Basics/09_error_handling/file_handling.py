# some methods of file handling

file = open('youtube.txt','w')

try:
    file.write("Hello! Ash")

finally:
    file.close()

# Or we can use 
# No need to close file i this one
with open('youtube.txt','w') as file:
    file.write("Ash is pokemon master")
