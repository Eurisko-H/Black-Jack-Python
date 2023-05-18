import json
import os
import logging
from logging.config import dictConfig


def start_logger():
    folder = os.path.dirname(__file__)
    file = os.path.join(folder, 'log.json')
    try:
        if not os.path.exists('logs'):
            os.mkdir('logs')
    except OSError as e:
        print("Error while creating the file", e)

    with open(file, 'r', encoding='utf-8') as fin:
        config = json.load(fin)
        dictConfig(config)
    return logging.getLogger('hasan')
