def clean_columns(df):
    df.columns = df.columns.str.replace('ST', 'State')
    df.columns = df.columns.str.lower().str.replace(' ', '_')
    return df

def clean_rows(df):
    df = df.dropna(how='all')
    return df

def clean_invaled_values(df):
    gender_mapping = {"Femal": "F", "female": "F", "Male": "M"}
    df["gender"].replace(gender_mapping, inplace=True)

    state_mapping = {"Cali": "California", "AZ": "Arizona", "WA": "Washington"}
    df["state"].replace(state_mapping, inplace=True)

    education_mapping = {"Bachelors": "Bachelor"}
    df["education"].replace(education_mapping, inplace=True)

    vehicle_mapping = {"Sports Car": "Luxury", "Luxury SUV": "Luxury", "Luxury Car": "Luxury"}
    df["vehicle_class"].replace(vehicle_mapping, inplace=True)

    df["customer_lifetime_value"] = df["customer_lifetime_value"].str.replace("%", "")
    return df

def format_data_type_float(df):
    df["customer_lifetime_value"] = df["customer_lifetime_value"].apply(lambda x: float(x))
    return df

def format_data_type_(df, column):
    df["number_of_open_complaints"] = df["number_of_open_complaints"].apply(lambda x: int(x.split('/')[1]))
    return df

def fillna_median(df):
    median_value = df['customer_lifetime_value'].median()
    df['customer_lifetime_value'].fillna(median_value, inplace=True)
    return df

def fillna_next(df):
    df['gender'].fillna(method='bfill', inplace=True)
    return df

def remove_duplicates(df):
    cleaned_df = df.drop_duplicates(keep='first')
    return cleaned_df
