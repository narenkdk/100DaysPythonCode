#Day 77: Automation script


#Write a script to automate file renaming.

import os

# Directory containing files
directory = "path/to/your/directory"

# User-defined renaming options
prefix = "new_"
suffix = "_renamed"
old_ext = ".txt"  # Set to None to rename all files
new_ext = ".log"  # Set to None to keep the same extension
replace_text = ("oldword", "newword")  # Set to None to skip

def rename_files(directory, prefix="", suffix="", old_ext=None, new_ext=None, replace_text=None):
    for filename in os.listdir(directory):
        old_path = os.path.join(directory, filename)

        if not os.path.isfile(old_path):
            continue  # Skip directories

        name, ext = os.path.splitext(filename)
        
        if old_ext and ext != old_ext:
            continue  # Skip files that don't match the old extension

        # Apply renaming rules
        new_name = prefix + name + suffix

        if replace_text:
            new_name = new_name.replace(replace_text[0], replace_text[1])

        new_extension = new_ext if new_ext else ext
        new_filename = new_name + new_extension
        new_path = os.path.join(directory, new_filename)

        os.rename(old_path, new_path)
        print(f'Renamed: {filename} -> {new_filename}')

# Run the script
rename_files(directory, prefix, suffix, old_ext, new_ext, replace_text)
