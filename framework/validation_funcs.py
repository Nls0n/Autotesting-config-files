from pathlib import Path
import uuid
import re


def is_valid_directory_path(path_str: str) -> bool:
    """Checking whether the string is the absolute path to the directory in the system"""
    if not isinstance(path_str, str):
        return False

    try:
        path = Path(path_str)
        return all([path.is_absolute(), path.exists(), path.is_dir()])
    except (TypeError, OSError):
        return False


def is_valid_uuid(uuid_str: str) -> bool:
    """Checks whether the string is a valid UUID"""
    try:
        uuid_obj = uuid.UUID(uuid_str)
        return str(uuid_obj) == uuid_str.lower()
    except (ValueError, AttributeError, TypeError):
        return False


def is_valid_locale(locale_str: str) -> bool:
    """
Checks the string for compliance:
 - RFC 3066 (for example, "en-US")
- OR Unix locales (for example, "en_US.UTF-8")
    """
    if not isinstance(locale_str, str):
        return False

    # Checking the Unix locale format (en_US.UTF-8)
    unix_pattern = r'^[a-z]{2,3}_[A-Z]{2,3}(\.[a-zA-Z0-9\-]+)?$'
    if re.fullmatch(unix_pattern, locale_str):
        return True

    # Verification of RFC 3066 (en-US)
    rfc_pattern = r'^([a-z]{2,3}|i-[a-z0-9]+)(?:-[a-zA-Z0-9]+)*$'
    return bool(re.fullmatch(rfc_pattern, locale_str.lower()))


def is_convertable_to_int(string: str) -> bool:
    """Checks whether it is possible to convert a string to an integer data type"""
    try:
        int(string.strip())
        return True
    except (ValueError, AttributeError, TypeError):
        return False


def is_convertable_to_float(string: str) -> bool:
    """Checks whether it is possible to convert a string to a float data type"""
    try:
        float(string.strip())
        return True
    except (ValueError, TypeError, AttributeError):
        return False
