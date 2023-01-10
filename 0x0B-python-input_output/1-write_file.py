#!/usr/bin/python3
"""
write file function
"""


def write_file(filename="", text=""):
    """The write file function"""

    with open(filename, 'w', encoding="utf-8") as f:
        f.write(text)
    return (len(text))
