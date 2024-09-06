import os
import collections

# A3
home = os.path.expanduser("~")
print("home directory: ", home)

# A4
path_exists = os.path.exists(home)
print("home directory exists: ", path_exists)


if path_exists:

    # A5
    content = os.listdir(home)
    print("home directory content: ", content)
    absolute_path = [os.path.join(home, item) for item in content]

    # A6
    if len(absolute_path) >= 3:
        print("an entry in the home directory: ", absolute_path[2])
    else:
        print("home directory does not have enough entries")

    # A7
    direct = 0
    file = 0
    for item in absolute_path:
        if os.path.isdir(item):
            direct += 1
        elif os.path.isfile(item):
            file += 1

    print("number of directories: ", direct)
    print("number of files: ", file)

    # A8
    biggist_file = None
    biggist_size = 0

    last_craeted_file = None
    last_created_time = 0

    last_canged_file = None
    last_canged_time = 0

    extension = []

    for item in absolute_path:
        if os.path.isfile(item):
            size = os.path.getsize(item)
            if size > biggist_size:
                biggist_size = size
                biggist_file = item

            created_time = os.path.getctime(item)
            if created_time > last_created_time:
                last_created_time = created_time
                last_craeted_file = item

            changed_time = os.path.getmtime(item)
            if changed_time > last_canged_time:
                last_canged_time = changed_time
                last_canged_file = item
            extension.append(os.path.splitext(item)[1])

    extension_counter = collections.Counter(extension)
    most_common_extension = extension_counter.most_common(1)[0][0] if extension_counter else "None"

    print("biggist file: ", biggist_file)
    print("last created file: ", last_craeted_file)
    print("last changed file: ", last_canged_file)
    if most_common_extension == "":
        print("most common extension: \"\" ")

else:
    print("home directory does not exist")

# A9
cwd = os.getcwd()
relativ_path = os.path.relpath(cwd, home)
print("relative path from home to cwd: ", relativ_path)

# A10
relativ_path_to_home = os.path.join(home, cwd)
path_home_to_cwd_and_back = os.path.join(cwd, relativ_path_to_home)
print("path from home to cwd and back: ", path_home_to_cwd_and_back)

# A11
path_normilized = os.path.normpath(path_home_to_cwd_and_back)
print("relativ path normilized: ", path_normilized)
