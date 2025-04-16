import pytest
from tests.fixtures import sections


def test_sections_names(sections):
    """Checking for the correct number of sections"""
    assert len(sections) == 3, "Incorrect number of sections"


@pytest.mark.parametrize(
    'section_name, expected',
    [
        ('General', True),
        ('Watchdog', True),
    ]
)
def test_sections_count(sections, section_name, expected):
    """Checking the validity of section names"""
    assert (section_name in sections) == expected, f'Section {section_name} not found'


def test_section_duplicates(sections):
    """Checking if there are duplicates"""
    assert sections['Duplicate'] is False, f'Sections have duplicates'
