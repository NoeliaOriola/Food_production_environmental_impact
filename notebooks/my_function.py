def round_numeric_columns(df: pd.DataFrame) -> pd.DataFrame:
    df2=df.copy()
    numeric_columns = df.select_dtypes(include='number')
    df2[numeric_columns.columns] = df2[numeric_columns.columns].round(2)
    return df2
