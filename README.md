# Convert Images to WebP

This Python application provides a utility to convert image files to WebP format. 

## Getting Started

These instructions will get you up and running with the application on your local machine.

### Prerequisites

- Python 3.x

### Installation

- Clone the repo
- Navigate into cloned directory
```bash
cd <repository>
```
- Open the terminal or cmd in this directory. Install packages by using the command below.
```bash
pip install -r requirements.txt
```


### Usage
Here's how to use the script:
```bash
python main.py -h
```
This will show the help message and explain the possible arguments:
```
usage: main.py [-h] [-f FILE] [-d DIR] [-o OUTPUT_DIR] [-r]

Convert Images to webp.

options:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  Convert file
  -d DIR, --dir DIR     Convert files in dir
  -o OUTPUT_DIR, --output-dir OUTPUT_DIR
                        Output directory
  -r, --remove          Remove original image
```

### Examples
To convert a single file:
```bash
python main.py -f /path/to/image.jpg
```
To convert all files in a directory:
```bash
python main.py -d /path/to/directory
```
To output the converted images to a specific directory:
```bash
python main.py -f /path/to/image.jpg -o /path/to/output/directory
```
To remove the original image after conversion:
```bash
python main.py -f /path/to/image.jpg -r
```
### License
This project is licensed under the terms of the MIT license.