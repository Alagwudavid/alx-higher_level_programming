#!/usr/bin/python3

"""
<<<<<<< HEAD
Python Module created by @Phina
=======
Python Module created by phinafati
>>>>>>> b0203d7989c3251a49a6f434a773a08a5675cf8b
"""


def write_file(filename="", text=""):
    """
    function that writes text to a utf-8 encoded file
    Arguments:
        filename (str): The name of the file
        text (str): The text to write
    Return:
        A file with text written
    """
    with open(filename, 'w', encoding='utf-8') as my_file:
<<<<<<< HEAD
        return my_file.write(text)
=======
        return my_file.write(text
>>>>>>> b0203d7989c3251a49a6f434a773a08a5675cf8b
