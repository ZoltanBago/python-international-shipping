#!/usr/bin/env python
# coding: utf-8

# # Python Pandas Projektek | Nemzetközi szállítási adatok elemzése
# ---
# 
# ![](logistics.jpg)
# 
# *Kép forrása: pixabay*

# ## 1. Az adatok betöltése és az alapadatok megjelenítése

# ### 1.1. Az adatok betöltése Pandas DataFrame-be
# A `szallitas.csv` nevű fájl adatait betöltjük a Pandas DataFrame-be. 
# 
# Létrehozunk egy változót `szallitas` néven és megjelenítjük az adatkeretet. 

# In[1]:


import pandas as pd

szallitas = pd.read_csv("szallitas.csv")

szallitas


# ### 1.2. Az adatkeret első 5 sorának megjelenítése

# In[2]:


szallitas.head()


# ### 1.3. A hiányzó adatok (NaN) ellenőrzése

# In[3]:


szallitas.info()


# ## 2. Az adatok szűrése

# ### 2.1. Az összes szállítmány kiválasztása, amely Magyarországra érkezett

# In[4]:


szallitas[szallitas["címzett_orszag"] == "Magyarország"]


# ### 2.2. A több, mint 10 kg súlyú szállítmányok kiszűrése

# In[5]:


szallitas[szallitas["suly_kg"] > 10]


# ### 2.3. A Kínából induló, `Elektronika` kategóriájú szállítmányok megjelenítése

# In[6]:


szallitas[(szallitas["felado_orszag"] == "Kína") & (szallitas["termek_kategoria"] == "Elektronika")]


# ## 3. Csoportosítás és aggregáció

# ### 3.1. A szállítmány megjelenítése ország és mennyiség szerint
# Ebben az esetben ki kell számítani, hogy melyik országból mennyi szállítmány érkezett. 
# 
# Ehhez elöször csoportosítani kell az országokat a `gropby()` metódussal a `címzett_orszag` oszlop szerint.
# 
# Ezután az `azonosito` alapján a `count()` metódus segítségével meg kell számolni az elemeket.

# In[7]:


szallitas.groupby("címzett_orszag")["azonosito"].count()


# **A kimenet:**
# 
#     címzett_orszag
#     Franciaország    1
#     Magyarország     4
#     Olaszország      1
#     USA              2
#     Name: azonosito, dtype: int64

# ### 3.2. Az átlagos szállítási idő meghatározása a termék kategória szerint

# In[8]:


szallitas.groupby("termek_kategoria")["szallitasi_ido_nap"].mean()


# **A kimenet:**
# 
#     termek_kategoria
#     Elektronika    17.000000
#     Ruházat        10.666667
#     Élelmiszer      9.000000
#     Name: szallitasi_ido_nap, dtype: float64

# ### 3.3. Az egyes feladó országokból indított szállítmányok teljes súlya

# In[9]:


szallitas.groupby("felado_orszag")["suly_kg"].sum()


# **A kimenet:**
# 
#     felado_orszag
#     Franciaország     7.5
#     Kína             33.7
#     Németország      10.2
#     USA              16.8
#     Name: suly_kg, dtype: float64

# ## 4. Új oszlop hozzáadása és adatmanipuláció

# ### 4.1. Új oszlop létrehozása `suly_lb` néven, amely a súlyt kilogrammból fontba konvertálja
# Létrehozzuk a DataFrame egy új oszlopát úgy, hogy megadjuk a nevét szögletes zárójelben, majd hozzárendeljük az értékeit.
# 
# > 1 kg = 2.20462 lb

# In[10]:


szallitas["suly_lb"] = szallitas["suly_kg"] * 2.20462


# Nézzük meg az új oszlopot a `head()` metódussal.

# In[11]:


szallitas.head()


# ### 4.2. Új oszlop létrehozása `gyors_szallitas` néven, ami True értéket ad, ha a `szallitasi_ido_nap` kisebb, mint 7 nap

# In[12]:


szallitas["gyors_szallitas"] = szallitas["szallitasi_ido_nap"] < 7 


# In[13]:


szallitas.head()


# ---
