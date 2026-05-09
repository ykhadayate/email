import pandas as pd

FILE_PATH = "Role3_05-05-2026_Count-284.xlsx"

def load_data():
    df = pd.read_excel(FILE_PATH, engine="openpyxl")
    df.fillna("", inplace=True)
    return df

def save_data(df):
    df.to_excel(FILE_PATH, index=False)

# CREATE
def add_record(new_data):
    df = load_data()
    df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
    save_data(df)

# UPDATE
def update_record(email, updated_data):
    df = load_data()
    df.loc[df["Mail-Id"] == email, updated_data.keys()] = updated_data.values()
    save_data(df)

# DELETE
def delete_record(email):
    df = load_data()
    df = df[df["Mail-Id"] != email]
    save_data(df)

# SEARCH
def search_records(name="", dept=""):
    df = load_data()

    if name:
        df = df[
            df["First-Name"].str.contains(name, case=False) |
            df["Last-Name"].str.contains(name, case=False)
        ]

    if dept:
        df = df[df["Department"].str.contains(dept, case=False)]

    return df
