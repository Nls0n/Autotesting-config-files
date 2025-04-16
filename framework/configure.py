import os
from pathlib import Path


def get_config_path() -> str:
    """Returns the path to the configuration from the CONFIG_PATH environment variable.
    If the variable is not specified, it uses the default path"""
    default_path = "/var/opt/kaspersky/config.ini"
    return os.environ.get("CONFIG_PATH", default_path)


def parse_file() -> dict:
    """Parses configuration file data"""
    sections = {'Duplicate': False}
    used = []
    current_section = None
    os.environ['CONFIG_PATH'] = get_config_path()
    path = Path(os.environ['CONFIG_PATH'])
    with open(path, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                if line[0] == '[' and line[-1] == ']':
                    section = line[1:-1]
                    if section not in used:
                        sections[section] = {}
                        current_section = section
                        used.append(section)
                    else:
                        sections['Duplicate'] = True
                if '=' in line:
                    parameter, value = map(str.strip, line.split('=', 1))
                    sections[current_section][parameter] = value
    return sections
