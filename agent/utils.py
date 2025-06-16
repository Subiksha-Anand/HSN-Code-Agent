import pandas as pd
from fuzzywuzzy import process

def load_hsn_data(file_path='data/HSN_Master_Data.xlsx'):
    df = pd.read_excel(file_path, engine='openpyxl')
    df.columns = df.columns.str.strip().str.replace('\n', '', regex=True)
    print("📋 Cleaned Column Names:", df.columns.tolist()) 
    df.rename(columns={'HSN Code': 'HSNCode', 'Description': 'Description'}, inplace=True)
    df.dropna(inplace=True)
    df['HSNCode'] = df['HSNCode'].astype(str).str.strip()
    df['Description'] = df['Description'].str.strip().str.lower()
    return df

def validate_format(code):
    return code.isdigit() and len(code) in [2, 4, 6, 8]

def validate_existence(code, df):
    return code in df['HSNCode'].values

def get_hierarchy_codes(code):
    return [code[:i] for i in [2, 4, 6] if i < len(code)]

def suggest_hsn(description, df, limit=3):
    desc = description.lower().strip()
    matches = process.extract(desc, df['Description'].tolist(), limit=limit)
    suggestions = []
    for match, score in matches:
        hsn = df[df['Description'] == match]['HSNCode'].values[0]
        suggestions.append((hsn, match, score))
    return suggestions
