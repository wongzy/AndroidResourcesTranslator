import json
import os
import xml.etree.cElementTree as ET
import copy

from googletrans import Translator
from script.resource_constants import RESOURCE_SPECIAL_MAP, COMMON_PREFIX, STRING_TAG, DEFAULT_LANGUAGE

RESOURCE_PATH = ''
RESOURCE_LANGUAGE = ''
FILE_SET = set()
LANGUAGE_SET = set()
TRANSLATOR = Translator()
COUNT = 1


# read json config
def read_config():
    with open('../translate_config.json') as json_file:
        json_config = json.load(json_file)
    global RESOURCE_PATH
    global RESOURCE_LANGUAGE
    global FILE_SET
    global LANGUAGE_SET
    global TRANSLATOR
    global COUNT
    RESOURCE_LANGUAGE = json_config['source_language']
    RESOURCE_PATH = json_config['source_path']
    FILE_SET = set(json_config['files_names'])
    LANGUAGE_SET = set(json_config['translate_languages'])


# get folder's name by language
def get_folder_name(_language):
    _folder_name = RESOURCE_PATH + COMMON_PREFIX
    if RESOURCE_SPECIAL_MAP.__contains__(_language):
        _folder_name += RESOURCE_SPECIAL_MAP.get(_language)
    else:
        _folder_name += '-' + _language
    return _folder_name


# get source files string
def read_resource_string():
    _map = {}
    _folder_name = get_folder_name(RESOURCE_LANGUAGE)
    if os.path.exists(_folder_name):
        for file_name in FILE_SET:
            _file_full_name = _folder_name + '/' + file_name
            if not os.path.exists(_file_full_name):
                exit('file ' + file_name + ' not exists, please check translate_config.json to ensure its validity')
            else:
                _map[file_name] = get_file_strings(_file_full_name)
    else:
        exit('Folder ' + _folder_name + ' is not exist，please check translate_config.json to ensure its validity')
    return _map


# read strings from file
def get_file_strings(_file_full_name):
    _tree = ET.parse(_file_full_name)
    # for item in _tree_root.iter():
    #     if item.tag == STRING_TAG:
    #         print(item.text)
    return _tree


# write string to file
def translate_to_other_file(_resource_map, _language):
    _folder_name = get_folder_name(_language)
    create_folder_if_absent(_folder_name)
    for key in _resource_map:
        _file_full_name = _folder_name + '/' + key
        create_file_if_absent(_file_full_name)
        _new_tree = copy.deepcopy(_resource_map[key])
        _new_tree_root = _new_tree.getroot()
        for item in _new_tree_root.iter():
            if item.tag == STRING_TAG:
                res = TRANSLATOR.translate(item.text, src=RESOURCE_LANGUAGE, dest=_language)
                item.text = res.text
        _new_tree.write(_file_full_name, encoding='utf-8', xml_declaration=True)


# create folder
def create_folder_if_absent(_folder_name):
    if not os.path.exists(_folder_name):
        os.makedirs(_folder_name)


# create file
def create_file_if_absent(_full_file_name):
    if not os.path.isfile(_full_file_name):
        fd = open(_full_file_name, mode='w', encoding='utf-8')
        fd.close()
    else:
        with open(_full_file_name, 'r+', encoding='utf-8') as file:
            file.seek(0)
            file.truncate()


# main
read_config()
# add default language to LANGUAGE_LIST
if not RESOURCE_LANGUAGE == DEFAULT_LANGUAGE:
    if not LANGUAGE_SET.__contains__(DEFAULT_LANGUAGE):
        LANGUAGE_SET.add(DEFAULT_LANGUAGE)
file_resources_map = read_resource_string()
if len(file_resources_map) == 0:
    exit('There is no string resource, please check translate_config.json to ensure its validity')
for language in LANGUAGE_SET:
    translate_to_other_file(file_resources_map, language)
    print(language + ' finished. count = ' + COUNT.__str__())
    COUNT = COUNT + 1
