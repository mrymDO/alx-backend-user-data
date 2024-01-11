#!/usr/bin/env python3
"""
filtered logger
"""
import re
from typing import List
import logging

PII_FIELDS = ["name", "email", "phone", "ssn", "password"]


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """
        initiailization
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        filter values in incoming log record
        """
        record.msg = filter_datum(
                self.fields, self.REDACTION, record.msg, self.SEPARATOR)
        return super().format(record)


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


def get_logger() -> logging.Logger:
    """returns a logger"""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    handler = logging.streamHandler()
    handler.setFormatter(fields=PII_FIELDS)
    logger.addHandler(handler)

    return logger
