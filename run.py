from pathlib import Path
from flask import Flask, jsonify

app = Flask(__name__)
BASEDIR = "/share"
HOST="0.0.0.0"
PORT=8000

def listFiles(basedir, requestedPath, glob="*"):
    files = Path(basedir).joinpath(requestedPath).glob(glob)
    files = list(map(str, list(files)))
    return jsonify(files)

def listDir(basedir, requestedPath):
  p = Path(basedir).joinpath(requestedPath)
  directories =  [str(x) for x in p.iterdir() if x.is_dir()]
  return jsonify(directories)

@app.route('/files/<path:req>/filter/<path:glob>')
def listSelectedFilesInPath(req, glob):
    return listFiles(BASEDIR, req, glob)

@app.route('/files/<path:req>')
def listAllFilesInPath(req):
    return listFiles(BASEDIR, req)

@app.route('/directories/<path:req>')
def listSubdirectories(req):
    return listDir(BASEDIR, req)

@app.route('/')
def default():
    return listDir(BASEDIR, "")

if __name__ == "__main__":
    app.run(host=HOST, port=PORT)

