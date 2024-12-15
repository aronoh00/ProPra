import glob
import re
import os
import itertools

# A1
print("all txt files:", glob.glob("*.txt"))

all_items = glob.glob("*")

# A2
file_with_number = [
    item for item in all_items
    if os.path.isfile(item) and re.search(r"\d", item)
]

print("all files with a number:", file_with_number)

# A3
directories = [item for item in all_items if os.path.isdir(item)]

print("all directories:", directories)

# A4
subdir = "9NQn"
file_in_9NQn = glob.glob(f"{subdir}/*")
file_with_two_number = [
    item for item in file_in_9NQn
    if os.path.isfile(item) and re.search(r"\d{2}", os.path.basename(item))]

print("all files in '9NQn' with two numbers:", file_with_two_number)

# A5
hidden_files = [item for item in glob.glob(".*") if os.path.isfile(item)]
print("all hidden files:", hidden_files)

# A6
files_with_bracket = [item for item in all_items
                      if os.path.isfile(item) and "[" in item]
print("all files with '[':", files_with_bracket)

# A7
all_json_files = glob.glob("**/*.json", recursive=True)
json_files_with_m = [
    file for file in all_json_files
    if "m" in os.path.basename(file)
]
print("recursive: all json files with 'm':", json_files_with_m)

# A8
all_text_files = glob.glob("**/*.txt", recursive=True)
textfiles_without_uppercase = [
    file for file in all_text_files
    if re.match(r'^[^A-Z]', os.path.basename(file))
]
print("recursive: all txt files in subdirs without uppercase first letter:", textfiles_without_uppercase)

# A9
txt_files_iterator = glob.glob("**/*.txt", recursive=True)
first_three_results = list(itertools.islice(txt_files_iterator,3))

print("recursive: all txt files, first 3 resultes:", first_three_results)
