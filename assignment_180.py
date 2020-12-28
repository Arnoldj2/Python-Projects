import os

directory = 'C:\\New_Directory'
for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        print(os.path.join(directory, filename))
        print(os.path.getmtime(directory))
    else:
        continue


