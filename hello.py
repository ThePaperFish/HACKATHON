from os import walk

mypath = input()
File = []
Folder = []

for (dirpath, dirnames, filenames) in walk(mypath):
    File.extend(filenames)
    Folder.extend(dirnames)
    break

print (File,'\n')
print (Folder,'\n')

search = input()
S_result = [f for f in File if search in f]
print (S_result)
