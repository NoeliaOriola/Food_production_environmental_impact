def round_numeric_columns(df: pd.DataFrame) -> pd.DataFrame:
    df2=df.copy()
    numeric_columns = df.select_dtypes(include='number')
    df2[numeric_columns.columns] = df2[numeric_columns.columns].round(2)
    return df2

def replace_nan_with_mean_for_rows(df):
    
    plant_mean1 = df.iloc[0:4, 1:].mean()
    animal_mean1 = df.iloc[4:11, 1:].mean()

    
    df.iloc[10, 1:] = df.iloc[10, 1:].fillna(plant_mean1)
    df.iloc[11, 1:] = df.iloc[11, 1:].fillna(animal_mean1)

    return df
def replace_nan_with_mean_for_rows(df):
    
    plant_mean1 = df.iloc[0:4, 1:].mean()
    animal_mean1 = df.iloc[4:11, 1:].mean()

    
    df.iloc[10, 1:] = df.iloc[10, 1:].fillna(plant_mean1)
    df.iloc[11, 1:] = df.iloc[11, 1:].fillna(animal_mean1)

    return df
    
def replace_nan_with_mean_for_rows(df):
    
    plant_mean = df.iloc[:33, 1:].mean()  

    
    animal_mean = df.iloc[33:43, 1:].mean()  

   
    df.iloc[44, 0:] = df.iloc[44, 0:].fillna(plant_mean)

   
    df.iloc[43, 0:] = df.iloc[43, 0:].fillna(animal_mean)

    return df