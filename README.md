# file_sorter.py
A (very) simple configurable file sorter written in Python.

## Dependencies
The one and only one dependency is termcolor.
Install using pip:
```bash
pip install termcolor
```

## Usage
Copy the **file_sorter.py** file into the directory that contains files that need to be sorted.
Run the script:
```bash
python file_sorter.py
```
## Configuration

### Month Names
```python
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
```
### More Files
```python
file_extension_folder = {
    ".mp4" : "Відео",
    ".jpg" : "Фото",
    ".file_extension" : "Directory Name",
    [...]
}
```
