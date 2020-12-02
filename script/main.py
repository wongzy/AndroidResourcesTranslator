import json
import xml.sax
import os

from googletrans import Translator
from script.resource_constants import RESOURCE_SPECIAL_MAP, COMMON_PREFIX

RESOURCE_PATH = ""
RESOURCE_LANGUAGE = ""
FILE_LIST = ""
TRANSLATE_TYPE = 1
LANGUAGE_LIST = ""


# read json config
def read_config():
    with open('../translate_config.json') as json_file:
        json_config = json.load(json_file)
    global RESOURCE_PATH
    global RESOURCE_LANGUAGE
    global FILE_LIST
    global TRANSLATE_TYPE
    global LANGUAGE_LIST
    RESOURCE_LANGUAGE = json_config["source_language"]
    RESOURCE_PATH = json_config["source_path"]
    FILE_LIST = json_config["files_names"]
    TRANSLATE_TYPE = json_config["translate_type"]
    LANGUAGE_LIST = json_config["translate_languages"]


# get folder's name by language
def get_folder_name(_language):
    _folder_name = RESOURCE_PATH + COMMON_PREFIX
    if RESOURCE_SPECIAL_MAP.__contains__(_language):
        _folder_name += RESOURCE_SPECIAL_MAP.get(_language)
    else:
        _folder_name += "-" + _language
    return _folder_name


# get source files string
def read_resource_string():
    _map = {}
    _folder_name = get_folder_name(RESOURCE_LANGUAGE)
    if os.path.exists(_folder_name):
        for file_name in FILE_LIST:
            _file_full_name = _folder_name + '/' + file_name
            if not os.path.exists(_file_full_name):
                exit("file " + file_name + " not exists, please check translate_config.json to ensure its validity")
            else:
                _map[file_name] = get_file_strings(_file_full_name)
    else:
        exit("Folder " + _folder_name + " is not exist，please check translate_config.json to ensure its validity")
    return _map


# read strings from file
def get_file_strings(_file_full_name):
    return ""


# main
read_config()
file_resources_map = read_resource_string()
if len(file_resources_map) == 0:
    exit("There is no string resource, please check translate_config.json to ensure its validity")
