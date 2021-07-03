import os

for dirpath, dirname, filename in os.walk("/etc"):
    for file in filename:
        comp_path= os.path.join(dirpath,file)
        if file == "hosts":
            print(comp_path)
