import os, datetime, shutil
from termcolor import colored

os.system('color')

directory_path = os.path.dirname(os.path.abspath(__file__))

files = os.listdir(directory_path)
file_index = 1
files_count = len(files)

month_names = [
    "Січень",
    "Лютий",
    "Березень",
    "Квітень",
    "Травень",
    "Червень",
    "Липень",
    "Серпень",
    "Вересень",
    "Жовтень",
    "Листопад",
    "Грудень"
]

file_extension_folder = {
    ".mp4" : "Відео",
    ".jpg" : "Фото"
}

for filename in files:
    file_path = os.path.join(directory_path, filename)
    file_extension = os.path.splitext(filename)[1]

    if os.path.isfile(file_path) and (file_extension in file_extension_folder):
        timestamp = os.path.getmtime(file_path)
        date = datetime.datetime.fromtimestamp(timestamp)

        month = date.month
        year = date.year

        destination_directory = f"{directory_path}\{file_extension_folder[file_extension]}\{month_names[month - 1]} - {year}"

        print(f"{file_index}/{files_count} Processing file: {colored(str(filename), 'blue')}. Established destination directory: {colored(str(destination_directory), 'light_blue')}")
        print("Checking for destination directory existence...")

        if not os.path.exists(destination_directory):
            os.makedirs(destination_directory)
            print(f"[ {colored('FAIL', 'red')} ] Not found. Creating a new destination directory: {destination_directory}")
        else:
            print(f"[ {colored('OK', 'green')} ] Destination directory was found. Moving file...")

        shutil.move(file_path, os.path.join(destination_directory, filename))

        print(f"[ {colored('OK', 'green')} ] File has been successfully moved to {destination_directory}\{filename}")
        file_index += 1
    else:
        print(f"[ {colored('FAIL', 'red')} ] Unsupported file type.")
        files_count -= 1

print("Done. Press enter to exit.")
input()
