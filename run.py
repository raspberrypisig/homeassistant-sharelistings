import os
import json
from pathlib import Path

def listFiles(basedir, requestedPath, glob):
    requestedFiles = Path(basedir).joinpath(requestedPath).glob(glob)
    requestedFiles = list(map(str, list(requestedFiles)))
    resultJson = json.dumps(requestedFiles)
    print(requestedFiles)
    print(resultJson)
    return resultJson


if __name__ == "__main__":
    basedir = "/share"
    listFiles(basedir, 'snoopdogg', '*.mp3')
