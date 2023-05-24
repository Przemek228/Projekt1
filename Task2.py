import sys
import os
import json

def parse_arguments():
    while True:
        path_file = input("Podaj ścieżkę do pliku: ")

        if not os.path.exists(path_file):
            print("Podany plik nie istnieje.")
        elif not os.path.isfile(path_file):
            print("Podany plik nie jest plikiem.")
        else:
            file_format = path_file.split('.')[-1]

            if file_format != 'json':
                print("Niewspierany format pliku. Obsługiwany format: .json")
            else:
                try:
                    with open(path_file, 'r') as file:
                        json.load(file)
                    print(f"Wybrano plik z rozszerzeniem .{file_format} o poprawnej składni JSON.")
                    break
                except json.JSONDecodeError as e:
                    print(f"Składnia pliku JSON jest niepoprawna: {str(e)}")
                except Exception as e:
                    print(f"Wystąpił błąd podczas analizy pliku JSON: {str(e)}")

    return path_file, file_format

path_file, file_format = parse_arguments()
