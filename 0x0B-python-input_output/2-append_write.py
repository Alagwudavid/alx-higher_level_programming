#!/usr/bin/python3
<<<<<<< HEAD
#!/usr/bin/python3
"""
function that appends a string
=======
"""
function that appends string
>>>>>>> b0203d7989c3251a49a6f434a773a08a5675cf8b
"""


def append_write(filename="", text=""):
<<<<<<< HEAD
    """eturns the number of characters added:"""
=======
    """returns of number of characters added:"""
>>>>>>> b0203d7989c3251a49a6f434a773a08a5675cf8b
    with open(filename, 'a', encoding='utf=8') as f:
        return f.write(text)
