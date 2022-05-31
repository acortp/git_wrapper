import json
import os
from typing import Any
from git_wrapper.settings import BASE_DIR
from wrapper import settings

CONFIG_PATH = os.path.join(BASE_DIR, 'wrapper/config.json')


def get_configuration() -> Any:
    with open(CONFIG_PATH, "r") as jsonfile:
        data = json.load(jsonfile)
        jsonfile.close()
    return data


def save_configuration(raw_data) -> None:
    data = {}
    for key in settings.GIT_CONFIG.keys():
        if key in raw_data:
            data.update({key: raw_data[key]})

    settings.GIT_CONFIG.update(data)

    with open(CONFIG_PATH, "w") as jsonfile:
        json.dump(settings.GIT_CONFIG, jsonfile)
        jsonfile.close()


def get_api_choices() -> (Any, Any):
    choices = [(key, key) for key, val in settings.GIT_CONFIG["git_pull_apis"].items()]
    return choices


def set_errors_form(request: Any, form: Any) -> Any:
    text_dict = json.loads(request.text)
    for error in text_dict.get('errors'):
        form.add_error('title', error.get('message'))
    return form
