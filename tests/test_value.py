import pytest
from framework.validation_funcs import *
from tests.fixtures import sections


@pytest.mark.parametrize(
    'parameter_name, section, expected',
    [
        ('ScanMemoryLimit', 'General', True),
        ('PackageType', 'General', True),
        ('ExecArgMax', 'General', True),
        ('AdditionalDNSLookup', 'General', True),
        ('CoreDumps', 'General', True),
        ('RevealSensitiveInfoInTraces', 'General', True),
        ('ExecEnvMax', 'General', True),
        ('MaxInotifyWatches', 'General', True),
        ('CoreDumpsPath', 'General', True),
        ('UseFanotify', 'General', True),
        ('KsvlaMode', 'General', True),
        ('MachineId', 'General', True),
        ('StartupTraces', 'General', True),
        ('MaxInotifyInstances', 'General', True),
        ('Locale', 'General', True),
        ('ConnectTimeout', 'Watchdog', True),
        ('MaxVirtualMemory', 'Watchdog', True),
        ('MaxMemory', 'Watchdog', True),
        ('PingInterval', 'Watchdog', True),
    ]
)
def test_values(sections, parameter_name, section, expected):
    """Checking the validity of the values of each parameter"""

    value = sections[section][parameter_name]
    exc = f'The parameter value {parameter_name} is invalid'

    if parameter_name in ['ScanMemoryLimit', 'MaxInotifyInstances']:
        assert is_convertable_to_int(value) and (1024 <= int(value) <= 8192), exc

    if parameter_name == 'PackageType':
        assert value.lower() in ['rpm', 'deb'], exc

    if parameter_name in ['ExecArgMax', 'ExecEnvMax']:
        assert is_convertable_to_int(value) and (10 <= int(value) <= 100), exc

    if parameter_name in ['AdditionalDNSLookup', 'CoreDumps', 'RevealSensitiveInfoInTraces', 'UseFanotify', 'KsvlaMode',
                          'StartupTraces']:
        assert value.lower() in ['true', 'false', 'no', 'yes'], exc

    if parameter_name == 'MaxInotifyWatches':
        assert is_convertable_to_int(value) and 1000 <= int(value) <= 1000000, exc

    if parameter_name == 'CoreDumpsPath':
        assert is_valid_directory_path(value), exc

    if parameter_name == 'MachineId':
        assert is_valid_uuid(value), exc

    if parameter_name == 'Locale':
        assert is_valid_locale(value), exc

    if parameter_name == 'ConnectTimeout':
        assert value[-1] == 'm' and is_convertable_to_int(value[:-1]) and 1 <= int(value[:-1]) <= 120, exc

    if parameter_name in ['MaxVirtualMemory', 'MaxMemory']:
        assert value in ['off', 'auto'] or (is_convertable_to_float(value) and 0 < float(value) <= 100), exc

    if parameter_name == 'PingInterval':
        assert is_convertable_to_int(value) and 100 <= int(value) <= 10000, exc
