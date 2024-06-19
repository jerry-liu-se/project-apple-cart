from flask import Flask, request, render_template

from load_saturn_db import SATURN_DB, ENUM_DB

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    """ main function point """

    saturn_db_sysvars = list(SATURN_DB)

    if request.method == 'POST':
        sysvar = request.form.get('textarea')

        if sysvar not in SATURN_DB:
            sysvar_data = {}
            print("INVALID SYSVAR")

        else:
            sysvar_data = SATURN_DB[sysvar]

        sysvar_info = [f"{key} : {value}" for key, value in sysvar_data.items()]

        enum_data = []
        if "enumType" in sysvar_data:
            for item in ENUM_DB[sysvar_data.get("enumType")]["enumEntries"]:
                enum_data.append(f"{item['value']} : {item['item']}")

        return render_template('index.html',
                               sysvars=saturn_db_sysvars,
                               sysvar_info=sysvar_info,
                               enum_info=enum_data)

    return render_template("index.html", sysvars=saturn_db_sysvars)


if __name__ == '__main__':
    app.run()
