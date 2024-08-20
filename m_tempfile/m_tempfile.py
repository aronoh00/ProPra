import tempfile, os

# A1
with tempfile.TemporaryDirectory(prefix="propra-") as temp_dir:
    print("path of temp dir:", temp_dir)
    
    # A2
    std_temp_dir = tempfile.gettempdir()
    print("OS standard temp dir:", std_temp_dir)

    # A3, A4
    with tempfile.NamedTemporaryFile(delete=False, mode='w') as temp_file:
        temp_file.write("Das ist der Inhalt meiner temporären Datei.")
        print("temp file:", temp_file.name)
        #A5
        temp_file.close()
        file_exists = os.path.exists(temp_file.name)
        print("temp file exists afer closing:", file_exists)
        #A6
        temp_file = open(temp_file.name, "r")
        print("temp file content:", temp_file.read())

    #A7
    file_exists_after_with = os.path.exists(temp_file.name)
    print("temp file exists afer with statement:", file_exists_after_with)

    #A8
    with tempfile.TemporaryFile() as temp_file:
        print("unnamed temp file name:", temp_file.name)

    #A9
    with tempfile.SpooledTemporaryFile(max_size=1024, mode='w+') as spooled_file:
        print("spooled temp file name:", spooled_file.name)
        #A10
        spooled_file.write("Das ist der Inhalt meiner spooled temp file." *50)
        print("spooled temp file name after reaching 1KB size:", spooled_file.name)

#A11
print("temp dir exists after with statement:", os.path.exists(temp_dir))
print("temp file exists after with statement:", os.path.exists(temp_file.name))
print("spooled temp file exists after with statement:", os.path.exists(spooled_file.name))
