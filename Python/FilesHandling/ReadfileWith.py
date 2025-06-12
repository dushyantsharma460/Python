with open("Dushyant.txt" , "r") as f:   # context manager
    content = f.read()
    print(content)
    # No need to write f.close() because the file is already close by default
    # But we can don't write (f.close()) in other file it don't give any error but write f.close() is recommented and good practice
    # Better way to read the file is (with)
    # With automatically close the file even the error occuredd