import sys
import os
import random
import string
import shutil
from pathlib import Path


def random_string(min_length=5, max_length=10):
    """
    Get a random string
    Args:
        min_length: Minimal length of string
        max_length: Maximal length of string
    Returns:
        Random string of ascii characters
    """
    length = random.randint(min_length, max_length)
    return "".join(
        random.choice(string.ascii_uppercase + string.digits) for _ in range(length)
    )


# mod from: https://stackoverflow.com/a/55758785
def create_random_tree(
    basedir,
    nfiles=2,
    nfolders=1,
    repeat=1,
    maxdepth=None,
    sigma_folders=1,
    sigma_files=1,
):
    """
    Create a random set of files and folders by repeatedly walking through the
    current tree and creating random files or subfolders (the number of files
    and folders created is chosen from a Gaussian distribution).
    Args:
        basedir: Directory to create files and folders in
        nfiles: Average number of files to create
        nfolders: Average number of folders to create
        repeat: Walk this often through the directory tree to create new
            subdirectories and files
        maxdepth: Maximum depth to descend into current file tree. If None,
            infinity.
        sigma_folders: Spread of number of folders
        sigma_files: Spread of number of files
    Returns:
       (List of dirs, List of files), all as pathlib.Path objects.
    """
    alldirs = []
    allfiles = []
    for i in range(repeat):
        for root, dirs, files in os.walk(str(basedir)):
            for _ in range(int(random.gauss(nfolders, sigma_folders))):
                p = Path(root) / random_string()
                p.mkdir(exist_ok=True)
                alldirs.append(p)
            for _ in range(int(random.gauss(nfiles, sigma_files))):
                file = random.choice(
                    [
                        f
                        for f in Path("images/").iterdir()
                        if f.is_file and not f.name.startswith(".")
                    ]
                )
                p = Path(root) / ""
                shutil.copy(file, p)
                # p.touch(exist_ok=True)
                allfiles.append(f"{p}/{file}")
            depth = os.path.relpath(root, str(basedir)).count(os.sep)
            if maxdepth and depth >= maxdepth - 1:
                del dirs[:]
    alldirs = list(set(alldirs))
    allfiles = list(set(allfiles))
    return alldirs, allfiles
