import json
from pathlib import Path

def load_json(file_name: str):

    file_path = (Path(__file__).parent.parent/ "test_data"/ file_name)

    with open(file_path, "r", encoding="utf-8") as file:

        return json.load(file)