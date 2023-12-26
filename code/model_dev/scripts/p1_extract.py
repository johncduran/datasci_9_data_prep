import pandas as pd 

datalink = 'https://data.cdc.gov/resource/95ax-ymtc.csv'

# dataset 1
df = pd.read_csv('/home/john_duran/datasci_9_data_prep/datasets/Drug_overdose_death_rates__by_drug_type__sex__age__race__and_Hispanic_origin__United_States_20231224 (1).csv')
df.size
df.sample(5)
len(df)


df.to_csv('/home/john_duran/datasci_9_data_prep/code/model_dev/data/raw/drug_overdose.csv', index=False)

df.to_pickle('/home/john_duran/datasci_9_data_prep/code/model_dev/data/raw/drug_overdose.pkl')


# dataset 2
df = pd.read_csv('//home/john_duran/datasci_9_data_prep/datasets/Death_rates_for_suicide__by_sex__race__Hispanic_origin__and_age__United_States_20231224.csv')
df.size
df.sample(5)
len(df)


df.to_csv('/home/john_duran/datasci_9_data_prep/code/model_dev/data/raw/death_suicide.csv', index=False)

df.to_pickle('/home/john_duran/datasci_9_data_prep/code/model_dev/data/raw/death_suicide.pkl')
