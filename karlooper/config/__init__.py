# -*-coding:utf-8-*-
"""

store global config data

>>>set_cli_data({"port": 8080})
>>>data = get_cli_data()

"""


__CLI_DATA = dict({})


def set_cli_data(data):
    """set global config data

    :param data: a dict contain global config data
    :return:

    """
    global __CLI_DATA
    for key in data:
        __CLI_DATA[key] = data[key]


def get_cli_data():
    global __CLI_DATA
    return __CLI_DATA
