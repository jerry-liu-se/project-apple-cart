import json
import os
from pathlib import Path


def clone_saturn_db():
    """  """


def load_saturn_db(db_path: Path, enum_path: Path):
    """ load the saturn db with enum files """

    with open(enum_path, 'r') as f:
        text = f.read()
        enum_data = json.loads(text)["enums"]

    enum_db = {}
    for item in enum_data:
        enum_db[item["name"]] = item

    with open(db_path, 'r') as f:
        text = f.read()
        sysvar_data = json.loads(text)["sysvars"]

    saturn_db = {}
    for item in sysvar_data:
        saturn_db[item["sysvarName"]] = item

    return saturn_db, enum_db


SATURN_DB_PATH = Path(os.getcwd()).parents[0] / 'scc_saturndb' / 'json'

SATURN_DB, ENUM_DB = load_saturn_db(SATURN_DB_PATH / "saturn_sysvarDB.json",
                                    SATURN_DB_PATH / "saturn_enums.json")
