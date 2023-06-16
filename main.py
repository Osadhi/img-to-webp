from os import remove, listdir
from os.path import isfile
from pathlib import Path

from PIL import Image
from colorama import Fore, init

init(autoreset=True)


def webp_converter(file: str) -> None:
    image = Image.open(file)
    image = image.convert('RGB')
    image.save(f'webps/{Path(file).stem}.webp', 'webp')
    remove(file)


if __name__ == '__main__':
    print(f'{Fore.GREEN}[+] Starting...')
    for file in listdir('images'):
        if isfile(f'images/{file}'):
            try:
                print(f'\n{Fore.GREEN}[+] Converting {file} ... ')
                webp_converter(f'images/{file}')
                print(f'{Fore.GREEN}[+] {file} converted to webp ')
            except Exception as e:
                print(f'{Fore.RED}[-] Unable to convert {file} ({e})')

    print(f'\n{Fore.GREEN}[+] Done')
