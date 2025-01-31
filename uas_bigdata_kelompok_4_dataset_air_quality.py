# -*- coding: utf-8 -*-
"""UAS_BIGDATA_KELOMPOK 4_DATASET AIR QUALITY.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/19vwTpD3FlR3hm_stdB6K8tEmMNCwNsSS

# UAS BIG DATA & PREDICTIVE ANALITYCS KELOMPOK 4

Anggota Kelompok :
1. Ainnur Rafli              (20.11.3639)
2. Fransiska Sindhi Kusuma   (20.11.3659)
3. Ema Devani Putri          (20.11.3663)
4. Mardiyatun Mardiah        (20.11.3617)
5. Sakantu Buka Mujtaba      (20.11.3626)

Kelas : 20-S1IF-06

Dataset : Air Quality

## Dataset
"""

# Commented out IPython magic to ensure Python compatibility.
# Import Library.
from scipy import stats
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline

df = pd.read_csv('/content/AirQuality.csv')
df.head() # Melihat lima data pertama.

"""## Proses EDA"""

df.tail() #untuk menampilkan 5 data terakhir

df.shape #untuk mengetahui jumlah baris dan kolom

df.columns #menampilkan nama nama kolom

df.index

df.describe() #mendeskripsikan data.

df.boxplot() #menampilkan boxplot.

df.isna() #mencari missing value.

df.isna().sum() #menampilkan jumlah missing value.

df.duplicated().sum() #menampilkan jumlah data yang duplikat

df.dtypes #menampilkan tipe data .

df.describe(include = "all") #distribusi data.

"""## Korelasi"""

df.corr()# menampilkan korelasi antar data.

sns.heatmap(df.corr()) #menampilkan semua korelasi antar kolom dalam bentuk heatmap

#Menampilkan semua korelasi dalam bentuk heatmap dengan angka korelasinya
plt.figure(figsize=(25,10))
heatmap = sns.heatmap(df.corr(), vmin=-1, vmax=1, annot=True)
heatmap.set_title('Correlation Heatmap', fontdict={'fontsize':12}, pad=12);

df[['AH','CO(GT)','T','RH']].corr() #menampilkan korelasi antara 'AH','CO(GT)','T', dan 'RH'.

pearson_coef, p_value = stats.pearsonr(df['C6H6(GT)'],df['CO(GT)'])
print("The Pearson Correlation Coefficient is", pearson_coef," with a P-Value of P =", p_value)
#menampilkan koefisien pearson.

sns.regplot(x="C6H6(GT)", y="CO(GT)", data=df)
plt.ylim(0,)
# menampilkan grafik kadar C6H6 dan CO.

plt.plot(df['AH'], df['CO(GT)']) #visualisasi data AH dan CO.

sns.heatmap(
    df[['C6H6(GT)','CO(GT)','AH','T','RH','NO2(GT)']].corr(),
    annot=True,
    center=0,
);
# Menampilkan heatmap korelasi antar data tersebut.

sns.pairplot(df)

"""## Prediksi/Forecast dengan Regresi"""

plt.scatter(df['CO(GT)'], df['RH'], color='gold')
plt.show()

"""### Data Preparation

#### Membagi Data Train dan Test
"""

# Membagi data train dan test

np.random.seed(42)
split = np.random.rand(len(df)) < 0.8
train = df[split]
test = df[~split]

# Mendefinisikan X_train, y_train, X_test, dan y_test

X_train = np.asanyarray(train[['CO(GT)']])
y_train = np.asanyarray(train[['RH']])

X_test = np.asanyarray(test[['CO(GT)']])
y_test = np.asanyarray(test[['RH']])

"""###Modeling

#### Linier Regression dengan Satu Variable Bebas
"""

from sklearn.linear_model import LinearRegression

# Membuat dan melatih model
lr_model = LinearRegression()
lr_model.fit(X_train, y_train)

# Coefficient dan Intercept
print ('Coefficients: ', lr_model.coef_)
print ('Intercept: ', lr_model.intercept_)

"""#### Visualisasi Linier Regression"""

# Visualisasi dengan scatter plot

plt.scatter(X_train, y_train,  color='blue')
plt.plot(X_train, lr_model.coef_[0][0]*X_train + lr_model.intercept_[0], '-r')
plt.xlabel('CO(GT)')
plt.ylabel('RH')

"""#### Prediksi"""

# Menguji model dengan X_test

y_pred = lr_model.predict(X_test)

print('Data asli: \n', y_test[0:10])
print('\n')
print('Hasil prediksi: \n', y_pred[0:10])

"""#### Evaluasi"""

from sklearn.metrics import mean_absolute_error, mean_squared_error

# Menampilkan MAE dan MSE
print('Mean Absolute Error (MAE): %.2f' % mean_absolute_error(y_pred, y_test))
print('Mean Squared Error (MSE): %.2f' % mean_squared_error(y_pred, y_test))