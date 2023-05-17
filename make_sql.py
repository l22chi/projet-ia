import pandas as pd
import codecs
from tqdm import tqdm

dataset = "time_series.csv"
df = pd.read_csv(dataset)

create_database = '''CREATE DATABASE IF NOT EXISTS projet;'''
use_database = '''USE projet;'''

with codecs.open('time_series.sql', 'a+', 'utf-8') as f:
    f.write(create_database)
    f.write('\n\n')
    f.write(use_database)
    f.write('\n\n')


create_tables = '''CREATE TABLE projet.time_series (
    id INT,
    date DATE NOT NULL,
    red NUMERIC (4, 3) DEFAULT 0,
    nir NUMERIC (4, 3) DEFAULT 0,
    swir NUMERIC (4, 3) DEFAULT 0,
    class INT,
);'''

with codecs.open('time_series.sql', 'a+', 'utf-8') as f:
    f.write(create_tables)
    f.write('\n\n')


insert_tables = '''INSERT INTO projet.time_series (
    id,
    date,
    red,
    nir,
    swir,
    class
)'''

with codecs.open('time_series.sql', 'a+', 'utf-8') as f:
    f.write(insert_tables)
    f.write('\n')


values_tables = '''VALUES'''

with codecs.open('time_series.sql', 'a+', 'utf-8') as f:
    f.write(values_tables)
    f.write('\n')

for index, row in tqdm(df.iterrows()):

    value = f'''    (
        {row['id']},
        '{str(row['date']).replace('-','')}',
        {row['red']},
        {row['nir']},
        {row['swir']},
        {row['class']},
    ),'''
    
    with codecs.open('time_series.sql', 'a+', 'utf-8') as f:
        f.write(value)
        f.write('\n')
    