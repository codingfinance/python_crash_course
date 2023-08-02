# stripping name

def remove_pref_suf(fname: str):

    print(fname.removeprefix(".txt"))
    print(fname.removesuffix(".txt"))

if __name__ == '__main__':
    remove_pref_suf("python_notes.txt")
