def round_numeric_columns(df: pd.DataFrame) -> pd.DataFrame:
    df2=df.copy()
    numeric_columns = df.select_dtypes(include='number')
    df2[numeric_columns.columns] = df2[numeric_columns.columns].round(2)
    return df2

def select_and_drop_countries(df: pd.DataFrame) -> pd.DataFrame:
    df2 = df.copy()
    countries_to_keep = ['Brazil', 'Colombia', 'Costa Rica', 'Mexico', 'Perú']
    df2 = df2[df2['Country'].isin(countries_to_keep)]
    return df2