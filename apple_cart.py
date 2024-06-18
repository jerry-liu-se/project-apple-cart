import json
import pathlib
import time
from pathlib import Path

from flask import Flask, request, render_template

app = Flask(__name__)


def load_saturn_db(db_path: pathlib.Path, enum_path: pathlib.Path):
    """ load the saturn db with enum files """

    with open(enum_path, 'r') as f:
        text = f.read()
        enum_db = json.loads(text)["enums"]

    with open(db_path, 'r') as f:
        text = f.read()
        saturn_db = json.loads(text)["sysvars"]

    return saturn_db, enum_db


@app.route('/', methods=['GET', 'POST'])
def index():

    # db_path = r"C:\Users\SESA675699\CODE\Libra\saturn\test\lib_python\saturndb\json\saturn_sysvarDB.json"
    # enum_path = r"C:\Users\SESA675699\CODE\Libra\saturn\test\lib_python\saturndb\json\saturn_enums.json"
    # start_time = time.time()
    # saturn_db, enum_db = load_saturn_db(Path(db_path), Path(enum_path))
    # print(time.time() - start_time)

    if request.method == 'POST':
        text = request.form.get('textarea')
        print(text)

    return render_template("index.html")



if __name__ == '__main__':
    app.run()
