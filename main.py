from argparse import ArgumentParser
from os import remove, listdir
from pathlib import Path

from PIL import Image
from colorama import Fore, init
import sys

init(autoreset=True)


def webp_converter(file: str, output_dir: str, remove_file: bool = False) -> None:
    """
    Converts the input image file to the WebP format and saves it to the specified output directory.

    Parameters:
    - file (str): Path to the input image file.
    - output_dir (str): Directory where the converted WebP file will be saved.
    - remove_file (bool, optional): If True, the input file will be removed after conversion. Default is False.

    Raises:
    - ValueError: If the specified file does not exist or is not a file.

    Returns:
    None
    """

    if not Path(file).is_file():
        raise ValueError("Expected a file but received a directory instead")

    with Image.open(file) as _img:
        _img.convert('RGB').save(
            f'{output_dir}/{Path(file).stem}.webp', 'webp')

    if remove_file:
        remove(file)


def convert_file(file: str, output_dir: str, remove_file: bool) -> None:
    """
    Converts a single file to the WebP format and prints the conversion status.

    Parameters:
    - file (str): Path to the input image file.
    - output_dir (str): Directory where the converted WebP file will be saved.
    - remove_file (bool, optional): If True, the input file will be removed after conversion. Default is False.

    Returns:
    None
    """

    try:
        print(f'\n{Fore.GREEN}[+] Converting {file} ... ')
        webp_converter(f'{file}', output_dir, remove_file)
        print(f'{Fore.GREEN}[+] {file} converted to webp ')
    except Exception as e:
        print(f'{Fore.RED}[-] Unable to convert {file} ({e})')


def convert_dir(directory: str, output_dir: str, remove_file: bool) -> None:
    """
    Converts all files in the specified directory to the WebP format.

    Parameters:
    - directory (str): Path to the input directory containing image files.
    - output_dir (str): Directory where the converted WebP files will be saved.
    - remove_file (bool, optional): If True, the input files will be removed after conversion. Default is False.

    Returns:
    None
    """

    for file in listdir(directory):
        file_path = str(Path(f'{directory}/{file}').absolute())
        if Path(file_path).is_file():
            convert_file(file_path, output_dir, remove_file)


if __name__ == '__main__':
    parser = ArgumentParser(description='Convert Images to webp.')
    parser.add_argument('-f', '--file', help='Convert file', type=str)
    parser.add_argument('-d', '--dir', help='Convert files in dir', type=str)
    parser.add_argument('-o', '--output-dir',
                        help='Output directory', type=str)
    parser.add_argument('-r', '--remove', action='store_true',
                        default=False, help='Remove original image')

    args = parser.parse_args()

    if args.file and args.dir or not args.file and not args.dir:
        print(f'{Fore.RED}[-] Use --file or --dir do not use both\n')
        parser.print_help()
        sys.exit()

    if not args.output_dir:
        args.output_dir = str(Path(args.file).absolute().parent) if args.file else str(
            Path(args.dir).absolute())
        print(f'{Fore.GREEN}[+] Using output directory as {args.output_dir}')

    print(f'{Fore.GREEN}[+] Starting...')

    if args.file:
        convert_file(file=args.file, output_dir=args.output_dir,
                     remove_file=args.remove)
    else:
        convert_dir(directory=args.dir, output_dir=args.output_dir,
                    remove_file=args.remove)

    print(f'\n{Fore.GREEN}[+] Done')
