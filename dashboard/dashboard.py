# -*- coding: utf-8 -*-
"""dashboard.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1D-46TobiGa5EC6JDevumrxQZax0mzM80
"""

!pip install streamlit

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Pengaturan visualisasi
sns.set(style="whitegrid")
plt.style.use("fivethirtyeight")

# Memuat data
day_data = pd.read_csv('day.csv')

# Mengubah tipe data kolom yang diperlukan di dataset harian
day_data['dteday'] = pd.to_datetime(day_data['dteday'])
day_data['season'] = day_data['season'].astype('category')
day_data['yr'] = day_data['yr'].astype('category')
day_data['mnth'] = day_data['mnth'].astype('category')
day_data['holiday'] = day_data['holiday'].astype('category')
day_data['weekday'] = day_data['weekday'].astype('category')
day_data['workingday'] = day_data['workingday'].astype('category')
day_data['weathersit'] = day_data['weathersit'].astype('category')

st.title('Dashboard Bike Sharing Data')

# Visualisasi distribusi jumlah sepeda yang disewa per musim
st.header('Distribusi Jumlah Sepeda yang Disewa per Musim')
fig, ax = plt.subplots()
sns.boxplot(x='season', y='cnt', data=day_data, ax=ax)
ax.set_title('Distribusi Jumlah Sepeda yang Disewa per Musim')
st.pyplot(fig)

# Tren jumlah sepeda yang disewa dari waktu ke waktu
st.header('Tren Jumlah Sepeda yang Disewa dari Waktu ke Waktu')
fig, ax = plt.subplots(figsize=(15, 6))
day_data.set_index('dteday')['cnt'].plot(ax=ax)
ax.set_title('Tren Jumlah Sepeda yang Disewa dari Waktu ke Waktu')
ax.set_ylabel('Jumlah Sepeda yang Disewa')
st.pyplot(fig)

# Pengaruh musim terhadap jumlah sepeda yang disewa
st.header('Pengaruh Musim Terhadap Jumlah Sepeda yang Disewa')
season_cnt = day_data.groupby('season')['cnt'].sum().reset_index()
fig, ax = plt.subplots()
sns.barplot(x='season', y='cnt', data=season_cnt, ax=ax)
ax.set_title('Pengaruh Musim Terhadap Jumlah Sepeda yang Disewa')
ax.set_xlabel('Musim')
ax.set_ylabel('Jumlah Sepeda yang Disewa')
st.pyplot(fig)