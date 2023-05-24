import json
import yaml

def load_json_file(file_path):
    try:
        with open(file_path) as file:
            data = json.load(file)
        print("Wczytano dane z pliku JSON.")
        return data
    except FileNotFoundError:
        print("Nie znaleziono pliku.")
        return None
    except json.JSONDecodeError as e:
        print(f"Niepoprawna składnia pliku JSON. Błąd: {e}")
        return None

def load_yaml_file(file_path):
    try:
        with open(file_path) as file:
            data = yaml.safe_load(file)
        print("Wczytano dane z pliku YAML.")
        return data
    except FileNotFoundError:
        print("Nie znaleziono pliku.")
        return None
    except yaml.YAMLError as e:
        print(f"Niepoprawna składnia pliku YAML. Błąd: {e}")
        return None

def save_json_file(file_path, data):
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
        print("Dane zostały zapisane do pliku JSON.")
    except FileNotFoundError:
        print("Nie znaleziono pliku.")
    except Exception as e:
        print(f"Wystąpił błąd podczas zapisywania danych do pliku. Błąd: {e}")

def save_yaml_file(file_path, data):
    try:
        with open(file_path, 'w') as file:
            yaml.dump(data, file)
        print("Dane zostały zapisane do pliku YAML.")
    except FileNotFoundError:
        print("Nie znaleziono pliku.")
    except Exception as e:
        print(f"Wystąpił błąd podczas zapisywania danych do pliku. Błąd: {e}")

def verify_file_syntax():
    file_path = input("Podaj ścieżkę do pliku JSON lub YAML: ")
    if file_path.endswith(".json"):
        data = load_json_file(file_path)
    elif file_path.endswith(".yml") or file_path.endswith(".yaml"):
        data = load_yaml_file(file_path)
    else:
        print("Nieobsługiwany format pliku. Obsługiwane formaty: .json, .yml, .yaml")
        return
    if data:
        output_file_path = input("Podaj ścieżkę do nowego pliku: ")
        if output_file_path.endswith(".json"):
            save_json_file(output_file_path, data)
        elif output_file_path.endswith(".yml") or output_file_path.endswith(".yaml"):
            save_yaml_file(output_file_path, data)
        else:
            print("Nieobsługiwany format pliku wyjściowego. Obsługiwane formaty: .json, .yml, .yaml")

verify_file_syntax()
