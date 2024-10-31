import pandas as pd

def load_data(url):
    return pd.read_csv(url)

def clean_column_names(df):
    df.columns = df.columns.str.replace(' ', '_').str.lower()
    return df

def rename_state_column(df):
    df.rename(columns= {'st': 'state'}, inplace=True)
    return df

def clean_gender_column(df):
    df['gender'] = df['gender'].replace(['Femal', 'female'], 'F')
    df['gender'] = df['gender'].replace('Male', 'M')
    return df

def rename_states(df):
    state_rename = {'AZ': 'Arizona', 'Cali': 'California', 'WA': 'Washington'}
    df['state'] = df['state'].replace(state_rename)
    return df

def clean_education_column(df):
    df["education"] = df["education"].replace("Bachelors", "Bachelor")
    return df

def clean_customer_lifetime_value(df):
    df["customer_lifetime_value"] = df["customer_lifetime_value"].str.strip('%').astype(float)
    return df

def clean_vehicle_class(df):
    vehicle = {'Sports Car': 'Luxury', 'Luxury SUV': 'Luxury', 'Luxury Car': 'Luxury'}
    df['vehicle_class'] = df['vehicle_class'].replace(vehicle)
    return df

def extract_middle_value(s):
    s = str(s)
    if '/' in s:
        return int(s.split('/')[1])
    return 0

def clean_open_complaints(df):
    df['number_of_open_complaints'] = df["number_of_open_complaints"].apply(extract_middle_value)
    return df

def fill_missing_values(df):
    for col in df.select_dtypes(include=['float64', 'int64']).columns:
        df[col] = df[col].fillna(df[col].mean())
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].fillna(df[col].mode()[0])
    return df

def convert_numeric_columns(df):
    for col in df.select_dtypes(include=['float64', 'int64']).columns:
        df[col] = df[col].astype(int)
    return df

def remove_duplicates(df):
    df = df.drop_duplicates()
    df = df.reset_index(drop=True)
    return df

def main(url):
    df = load_data(url)
    df = clean_column_names(df)
    df = rename_state_column(df)
    df = clean_gender_column(df)
    df = rename_states(df)
    df = clean_education_column(df)
    df = clean_customer_lifetime_value(df)
    df = clean_vehicle_class(df)
    df = clean_open_complaints(df)
    df = fill_missing_values(df)
    df = convert_numeric_columns(df)
    df = remove_duplicates(df)
    df.to_csv("cleaned_file.csv", index=False)
    print(df.head())

if __name__ == "__main__":
    data_url = "https://raw.githubusercontent.com/data-bootcamp-v4/data/main/file1.csv"
    main(data_url)
