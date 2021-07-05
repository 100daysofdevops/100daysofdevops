import os

for dirpath, dirname, filename in os.walk("/etc/openldap"):
    for file in filename:
        comp_path= os.path.join(dirpath,file)
        if file.endswith(".conf"):
            print(comp_path)
            file_size = os.path.getsize(comp_path)
            print("File size is: ", file_size, "bytes")
