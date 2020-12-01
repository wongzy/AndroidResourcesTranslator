import json

from googletrans import Translator
from script.resource_constants import RESOURCE_SPECIAL_MAP, COMMON_PREFIX


# read json config
def read_config():
    with open('../translate_config.json') as json_file:
        json_config = json.load(json_file)
    return json_config


config = read_config()
print(config["source_language"])
print(config["source_path"])
file_list = config["files_names"]
print(file_list)
language_list = config["translate_languages"]
print(language_list)
