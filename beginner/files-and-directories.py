from pathlib import Path 

# Absolute path examples 
# c:\Program Files\Microsoft
# /usr/local/bin
# Relative path 

path = Path("ecommerce")
print(path.exists()) # checks if folder or file exists

path = Path("emails")
# print(path.mkdir()) # creates directory 
# print(path.rmdir()) # removes directory

path = Path()
for file in path.glob('*.py'): # searches for all python files
    print(file)

for file in path.glob('*'): # searches for all files
    print(file)




