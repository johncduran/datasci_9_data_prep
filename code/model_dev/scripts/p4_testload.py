import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler

loaded_model = pickle.load(open('/home/john_duran/datasci_9_data_prep/code/model_dev/models/scaler_drug.sav, 'rb'))
loaded_scaler = pickle.load(open('/home/john_duran/datasci_9_data_prep/code/model_dev/models/xgboost_drug.sav, 'rb'))

df_test = pd.DataFrame(columns=['panel', 'panel_num', 'unit', 'unit_num', 'stub_name', 'stub_name_num', 'stub_label', 'stub_label_num', 'year', 'year_num', 'age', 'age_num'])

df_test.loc[0] = [1.1, 3, 0, 4.3, 4, 5, 1, 1]
df_test_scaled = loaded_scaler.transform(df_test)

y_test_pred = loaded_model.predict(df_test_scaled)
print(y_test_pred[0])

import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler


loaded_model = pickle.load(open('/home/john_duran/datasci_9_data_prep/code/model_dev/models/scaler_drug.sav, 'rb'))
loaded_scaler = pickle.load(open('/home/john_duran/datasci_9_data_prep/code/model_dev/models/xgboost_suicide.sav, 'rb'))

df_test = pd.DataFrame(columns=['panel', 'panel_num', 'unit', 'unit_num', 'stub_name', 'stub_name_num', 'stub_label', 'stub_label_num', 'year', 'year_num', 'age', 'age_num'])

df_test.loc[0] = [1.1, 3, 0, 4.3, 4, 5, 1, 1]
df_test_scaled = loaded_scaler.transform(df_test)


y_test_pred = loaded_model.predict(df_test_scaled)
print(y_test_pred[0])