import os
import pandas as pd
import json
def prepare_data(estate_input, category):
    
    input_data = estate_input.dict()
    # Erstelle ein DataFrame aus dem JSON-Objekt
    df = pd.DataFrame.from_dict(input_data, orient='index').T
    
    df = perform_one_hot_encoding(df, category)
    
    df = convert_xgb_data(df)
    
    return df


def perform_one_hot_encoding(df, category):
    current_dir = os.getcwd()
    # Öffne die JSON-Datei im Lesemodus und lade ihren Inhalt
    with open(os.path.join(current_dir, 'app' ,'estate_fields', category, 'estate_subtypes.json'), 'r') as json_datei:
        subtypes = json.load(json_datei)
        
    with open(os.path.join(current_dir, 'app' ,'estate_fields', category ,'estate_types.json'), 'r') as json_datei:
        types = json.load(json_datei)
        
    with open(os.path.join(current_dir, 'app' ,'estate_fields', category ,'features.json'), 'r') as json_datei:
        features = json.load(json_datei)
        
    with open(os.path.join(current_dir, 'app' ,'estate_fields', category ,'city_list.json'), 'r') as json_datei:
        city_types = json.load(json_datei)
    
    # Füge Spalten für estate_features hinzu
    for feature in features['estate_features']:
        column_name = f'feature_{feature}'.lower()
        df[column_name] = df['features'].apply(lambda x: feature in str(x)) 

    # Füge Spalten für estate_types und estate_subtypes hinzu
    for estate_type in types['estate_types']:
        column_name = f'estate_type_{estate_type}'.lower()
        df[column_name] = df['estate_types'].apply(lambda x: estate_type in x)

    for estate_subtype in subtypes['estate_subtypes']:
        column_name = f'estate_subtype_{estate_subtype}'.lower()
        df[column_name] = df['estate_subtypes'].apply(lambda x: estate_subtype in x)


    # Erstellen Sie ein leeres Dictionary, das die neuen Spalten aufnehmen wird
    new_columns = {}

    for key, city in city_types.items():
        # Erstellung der Spalte für jede Stadt
        # key ist der Spaltenname und city ist der Wert, nach dem wir überprüfen
        new_columns[city] = df['city'].apply(lambda x: city in str(x))

    # Konvertieren Sie das Dictionary in einen DataFrame
    new_columns_df = pd.DataFrame(new_columns)

    # Verbinden Sie den neuen DataFrame mit dem bestehenden DataFrame
    df = pd.concat([df, new_columns_df], axis=1)

    # Entfernen der ursprünglichen Spalten, nachdem Sie sie transformiert haben
    df.drop(['estate_subtypes', 'estate_types', 'features', 'city'], axis=1, inplace=True)
    
    return df
  
def convert_xgb_data(df):
    # Konvertierung der numerischen Spalten von 'object' zu 'float' oder 'int'
    df['postcode'] = pd.to_numeric(df['postcode'], errors='coerce')
    df['plot_area_size_max'] = pd.to_numeric(df['plot_area_size_max'], errors='coerce')
    df['living_area_size_max'] = pd.to_numeric(df['living_area_size_max'], errors='coerce')
    df['rooms_max'] = pd.to_numeric(df['rooms_max'], errors='coerce')
    df['construction_year'] = pd.to_numeric(df['construction_year'], errors='coerce')

    # Konvertierung der Spalte 'is_new' von 'object' zu 'bool', wenn es sich um eine binäre Darstellung handelt
    df['is_new'] = df['is_new'].astype(int)
    
    return df