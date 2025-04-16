import pytest
from tests.fixtures import sections


def test_parameter_count(sections):
    """Checking for the number of parameters"""
    assert len(sections['General']) + len(sections['Watchdog']) == 19, 'The number of parameters is invalid'


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
def test_parameters(sections, parameter_name, section, expected):
    """Checking for the validity of locations"""
    assert (parameter_name in sections[section]) == expected, f'Parameter {parameter_name} has a invalid location'
