import os
from pathlib import Path

def listFiles(basedir, requestedPath, glob):
    allFiles = Path(basedir).joinpath(requestedPath).glob(glob)
    for f in allFiles:
      print(str(f))


if __name__ == "__main__":
    basedir = "/share"
    listFiles(basedir, 'snoopdogg', '*.mp3')
