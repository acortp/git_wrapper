import json
from typing import Any


def get_configuration() -> Any:
    with open("config.json", "r") as jsonfile:
        data = json.load(jsonfile)
        jsonfile.close()
    return data


def save_configuration(data) -> None:
    with open("config.json", "w") as jsonfile:
        json.dump(data, jsonfile)
        jsonfile.close()
