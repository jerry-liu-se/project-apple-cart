import keyring
import requests


def load_saturn_db():
    """ query saturn db files """

    token = keyring.get_password("GITHUB_PAT", "GITHUB_PAT_USER")
    auth_header = {'Authorization': f'bearer {token}'}

    url = "https://raw.githubusercontent.com/SchneiderProsumer/scc_saturndb/main/json/saturn_sysvarDB.json"
    req = requests.get(url, headers=auth_header)
    sysvar_data = req.json()["sysvars"]

    saturn_db = {}
    for item in sysvar_data:
        saturn_db[item["sysvarName"]] = item

    url = "https://raw.githubusercontent.com/SchneiderProsumer/scc_saturndb/main/json/saturn_enums.json"
    req = requests.get(url, headers=auth_header)
    enum_data = req.json()["enums"]

    enum_db = {}
    for item in enum_data:
        enum_db[item["name"]] = item

    return saturn_db, enum_db
