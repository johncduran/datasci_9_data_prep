import pandas as pd 
from sklearn.preprocessing import OrdinalEncoder

## dataset 1
df = pd.read_csv('/home/john_duran/datasci_9_data_prep/code/model_dev/data/raw/drug_overdose.csv')

df.columns
 
df.columns = df.columns.str.lower().str.replace(' ', '_')
df.columns

df.dtypes 
len(df)

#dates 
selected_columns = ['year', 'year_num']

df_dates = df[selected_columns]

df_dates.to_csv('/home/john_duran/datasci_9_data_prep/code/model_dev/data/processed/drug_dates.csv', index=False)

#panel
selected_columns = ['panel', 'panel_num']

df_dates = df[selected_columns]

df_dates.to_csv('/home/john_duran/datasci_9_data_prep/code/model_dev/data/processed/drug_panel.csv', index=False)


# unit

selected_columns = ['unit', 'unit_num']

df_dates = df[selected_columns]

df_dates.to_csv('/home/john_duran/datasci_9_data_prep/code/model_dev/data/processed/drug_unit.csv', index=False)

# stub
selected_columns = ['stub_name', 'stub_name_num']

df_dates = df[selected_columns]

df_dates.to_csv('/home/john_duran/datasci_9_data_prep/code/model_dev/data/processed/drug_stub_name.csv', index=False)

# stub label
selected_columns = ['stub_label', 'stub_label_num']

df_dates = df[selected_columns]

df_dates.to_csv('/home/john_duran/datasci_9_data_prep/code/model_dev/data/processed/drug_stub_label.csv', index=False)

# age
selected_columns = ['age', 'age_num']

df_dates = df[selected_columns]

df_dates.to_csv('/home/john_duran/datasci_9_data_prep/code/model_dev/data/processed/drug_age.csv', index=False)


# all integers combined 
selected_columns = ['panel_num', 'unit_num', 'stub_name_num', 'stub_label_num', 'year_num', 'age_num']

df_drugs_num = df[selected_columns]
df_drugs_num.to_csv('/home/john_duran/datasci_9_data_prep/code/model_dev/data/processed/drugs_num.csv', index=False)




# dataset 2
import pandas as pd 
from sklearn.preprocessing import OrdinalEncoder

## get data raw
df = pd.read_csv('/home/john_duran/datasci_9_data_prep/code/model_dev/data/raw/death_suicide.csv')

## get column names
df.columns

## do some data cleaning of colun names, 
## make them all lower case, replmove white spaces and rpelace with _ 
df.columns = df.columns.str.lower().str.replace(' ', '_')
df.columns


## get data types
df.dtypes # nice combination of numbers and strings/objects 
len(df)

#dates 
selected_columns = ['year', 'year_num']

df_dates = df[selected_columns]

df_dates.to_csv('/home/john_duran/datasci_9_data_prep/code/model_dev/data/processed/suicide_dates.csv', index=False)


# unit

selected_columns = ['unit', 'unit_num']

df_dates = df[selected_columns]

df_dates.to_csv('/home/john_duran/datasci_9_data_prep/code/model_dev/data/processed/suicide_unit.csv', index=False)

# stub
selected_columns = ['stub_name', 'stub_name_num']

df_dates = df[selected_columns]

df_dates.to_csv('/home/john_duran/datasci_9_data_prep/code/model_dev/data/processed/suicide_stub_name.csv', index=False)

# stub label
selected_columns = ['stub_label', 'stub_label_num']

df_dates = df[selected_columns]

df_dates.to_csv('/home/john_duran/datasci_9_data_prep/code/model_dev/data/processed/suicide_stub_label.csv', index=False)

# age
selected_columns = ['age', 'age_num']

df_dates = df[selected_columns]

df_dates.to_csv('/home/john_duran/datasci_9_data_prep/code/model_dev/data/processed/suicide_age.csv', index=False)


# all integers combined 
selected_columns = ['unit_num', 'stub_name_num', 'stub_label_num', 'year_num', 'age_num']

df_deaths_num = df[selected_columns]
df_deaths_num.to_csv('/home/john_duran/datasci_9_data_prep/code/model_dev/data/processed/suicide_num.csv', index=False)

