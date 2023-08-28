import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score,f1_score, recall_score, precision_score
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LogisticRegression 
 
df_train = pd.read_csv('train.csv')
df_test  = pd.read_csv('test.csv')

# Data Pre-processing
df_train['is_anomaly'] = np.where(df_train['is_anomaly'] == False, 0, 1) 
df_train["Is_anomaly"] = df_train['is_anomaly'].values

df_train.drop('is_anomaly', axis = 1 ,inplace = True)

X_train = df_train[['timestamp','value','predicted']]
y_train = df_train['Is_anomaly']
df_train.head()


mmx_scaler = MinMaxScaler()

# Create scaled datasets 
X_train_M = pd.DataFrame(mmx_scaler.fit_transform(X_train))
X_test_M  = pd.DataFrame(mmx_scaler.transform(X_train))
model=LogisticRegression().fit(X_train,y_train)
y_pred=model.predict(X_test_M)
accuracy_score_ = accuracy_score(y_train, y_pred)  
f1_score_ = f1_score(y_train, y_pred)  
recall_score_ = recall_score(y_train, y_pred)  
precision_score_ = precision_score(y_train, y_pred)  
print('Accuracy: ',accuracy_score_)
print('f1_score_: ',f1_score_)
print('recall_score_: ',recall_score_)
print('precision_score_: ',precision_score_)

