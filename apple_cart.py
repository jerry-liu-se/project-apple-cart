from flask import Flask, request, render_template

from _load_saturn_db import SATURN_DB, ENUM_DB

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        sysvar = request.form.get('textarea')
        sysvar_data = SATURN_DB[sysvar]

        enum_data = []
        if "enumType" in sysvar_data:
            enum_data = ENUM_DB[sysvar_data.get("enumType")]["enumEntries"]

        print(SATURN_DB[sysvar])

    elif request.method == 'GET':
        pass

    saturn_db_sysvars = list(SATURN_DB)

    return render_template("index.html", sysvars=saturn_db_sysvars)


if __name__ == '__main__':
    app.run()
