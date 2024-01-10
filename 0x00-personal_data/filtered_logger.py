#!/usr/bin/env python3
"""
Regex-ing
"""
import re
from typing import List


def filter_datum(
     fields: List[str], redaction: str, message: str, separator: str) -> str:
    """
    returns the log message obfuscated
    """
    for f in fields:
        message = re.sub(
            "{}=.*?{}".format(f, separator),
            "{}={}{}".format(f, redaction, separator),
            message,
        )
    return message
