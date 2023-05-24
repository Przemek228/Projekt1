import sys
import os

def parse_arguments():
    while True:
        path_file = input("Podaj ścieżkę do pliku: ")

        if not os.path.exists(path_file):
            print("Podany plik nie istnieje.")
        elif not os.path.isfile(path_file):
            print("Podany plik nie jest plikiem.")
        else:
            file_format = path_file.split('.')[-1]

            if file_format not in ['xml', 'json', 'yml', 'yaml']:
                print("Niewspierany format pliku. Obsługiwane formaty: .xml, .json, .yml, .yaml")
            else:
                print(f"Wybrano plik z rozszerzeniem .{file_format}")
                break

    return path_file, file_format

path_file, file_format = parse_arguments()
