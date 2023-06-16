import json


def read_json_data(content):
    """Parse json to data"""
    return json.loads(content)


def parse_json_data(content):
    """Parse data to json"""
    return json.dumps(content)
