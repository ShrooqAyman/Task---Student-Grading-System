import json
import csv


def read_json_file(file):
    """
    Read and load a json file and return the data as a dictionary.

    Args:
        file (str): path of the json file.

    Returns:
        dict: the data from the json file as a dictionary.
    """
    try:
        with open(file, "r") as file:
            data = json.load(file)
            return data
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON {e}.")
        return

    except Exception as e:
        print(f"Error: {e}")
        return


def read_csv(csv_file):
    """
    Read a csv file.

    Args:
        csv_file (str): path to the csv file.

    Returns:
        list: 
    """
    try:
        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)
            rows = list(reader)
            for row in rows:
                for key, value in row.items():
                    if type(value) == list:
                        continue
                    try:
                        row[key] = int(value)
                    except ValueError:
                        pass
            return rows

    except FileNotFoundError:
        print(f"{csv_file} not found.")
        return
