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
                        data = json.load(file)
                    break
                except json.JSONDecodeError as e:
                    print(f"Składnia pliku JSON jest niepoprawna: {str(e)}")
                except Exception as e:
                    print(f"Wystąpił błąd podczas analizy pliku JSON: {str(e)}")

    while True:
        new_file_format = input("Podaj nowe rozszerzenie pliku (xml, yml): ")

        if new_file_format not in ['xml', 'yml']:
            print("Niewspierane nowe rozszerzenie pliku. Obsługiwane rozszerzenia: xml, yml")
        else:
            new_file_path = path_file.rsplit('.', maxsplit=1)[0] + '.' + new_file_format
            with open(new_file_path, 'w') as new_file:
                if new_file_format == 'xml':
                    xml_data = convert_to_xml(data)
                    if xml_data:
                        new_file.write(xml_data)
                elif new_file_format == 'yml':
                    yaml_data = convert_to_yaml(data)
                    if yaml_data:
                        new_file.write(yaml_data)

            print(f"Przekonwertowano plik JSON na nowe rozszerzenie .{new_file_format}")

            break

def convert_to_xml(data):
    xml_data = ""  
    return xml_data

def convert_to_yaml(data):
    yaml_data = ""  
    return yaml_data

parse_arguments()
