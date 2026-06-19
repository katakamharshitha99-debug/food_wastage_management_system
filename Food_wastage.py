#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


providers = pd.read_csv(r"D:\Labmentix\Food waste management system\providers_data.csv")
receivers = pd.read_csv(r"D:\Labmentix\Food waste management system\receivers_data.csv")
food = pd.read_csv(r"D:\Labmentix\Food waste management system\food_listings_data.csv")
claims = pd.read_csv(r"D:\Labmentix\Food waste management system\claims_data.csv")


# In[3]:


print(providers.info())
print(receivers.info())
print(food.info())
print(claims.info())


# In[4]:


print(providers.isnull().sum())
print(receivers.isnull().sum())
print(food.isnull().sum())
print(claims.isnull().sum())

# No null values


# In[5]:


providers.fillna("Unknown", inplace=True)
receivers.fillna("Unknown", inplace=True)
food.fillna("Unknown", inplace=True)
claims.fillna("Unknown", inplace=True)


# In[6]:


providers.drop_duplicates(inplace=True)
receivers.drop_duplicates(inplace=True)
food.drop_duplicates(inplace=True)
claims.drop_duplicates(inplace=True)


# In[7]:


food["Expiry_Date"] = pd.to_datetime(food["Expiry_Date"])

claims["Timestamp"] = pd.to_datetime(
    claims["Timestamp"]
)


# In[8]:


import os

os.makedirs("data", exist_ok=True)

providers.to_csv("data/providers_clean.csv", index=False)


# In[9]:


import os
print(os.getcwd())


# In[10]:


providers.to_csv(
    r"D:\Labmentix\food wastage project\providers_clean.csv",
    index=False
)

receivers.to_csv(
    r"D:\Labmentix\food wastage project\receivers_clean.csv",
    index=False
)

food.to_csv(
    r"D:\Labmentix\food wastage project\food_clean.csv",
    index=False
)

claims.to_csv(
    r"D:\Labmentix\food wastage project\claims_clean.csv",
    index=False
)

print("All cleaned files saved successfully!")


# In[11]:


# EDA 
providers.shape[0]
receivers.shape[0]


# In[12]:


food["Food_Type"].value_counts()


# In[13]:


food["Meal_Type"].value_counts()


# In[14]:


claims["Status"].value_counts()


# In[15]:


print(providers.describe())
print(receivers.describe())
print(food.describe())
print(claims.describe())


# In[16]:


food["Expiry_Date"] = pd.to_datetime(food["Expiry_Date"])
claims["Timestamp"] = pd.to_datetime(claims["Timestamp"])


# In[17]:


print("Providers:", providers.duplicated().sum())
print("Receivers:", receivers.duplicated().sum())
print("Food:", food.duplicated().sum())
print("Claims:", claims.duplicated().sum())


# In[18]:


print("Total Food Quantity:", food["Quantity"].sum())
print("Average Quantity:", food["Quantity"].mean())
print("Maximum Quantity:", food["Quantity"].max())


# In[19]:


provider_type = providers["Type"].value_counts()

plt.figure(figsize=(8,5))
provider_type.plot(kind="bar")
plt.title("Provider Type Distribution")
plt.show()


# In[20]:


food.groupby("Provider_Type")["Quantity"].sum().sort_values(ascending=False)


# In[21]:


receivers["Type"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.title("Receiver Types")
plt.show()


# In[22]:


food["Food_Type"].value_counts()


# In[23]:


plt.figure(figsize=(8,5))

sns.countplot(
    data=food,
    x="Food_Type"
)

plt.title("Food Type Distribution")
plt.show()


# In[24]:


food["Meal_Type"].value_counts()


# In[25]:


plt.figure(figsize=(8,5))

sns.countplot(
    data=food,
    x="Meal_Type"
)

plt.title("Meal Type Distribution")
plt.show()


# In[26]:


city_food = food["Location"].value_counts().head(10)

city_food.plot(
    kind="bar",
    figsize=(10,5)
)

plt.title("Top Cities by Food Listings")
plt.show()


# In[27]:


food.groupby("Location")["Quantity"]\
    .sum()\
    .sort_values(ascending=False)\
    .head(10)


# In[28]:


food.groupby("Location")["Quantity"]\
    .sum()\
    .sort_values(ascending=False)\
    .head(10)\
    .plot(kind="bar")


# In[29]:


claims["Status"].value_counts()


# In[30]:


claims["Status"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.title("Claim Status")
plt.show()


# In[31]:


food_claims = claims.merge(
    food,
    on="Food_ID"
)

food_claims["Food_Name"]\
    .value_counts()\
    .head(10)


# In[32]:


food_claims["Food_Name"]\
    .value_counts()\
    .head(10)\
    .plot(kind="bar")


# In[33]:


claims.groupby("Receiver_ID")\
      .size()\
      .sort_values(ascending=False)\
      .head(10)


# In[34]:


claims.groupby("Receiver_ID")\
      .size()\
      .sort_values(ascending=False)\
      .head(10)\
      .plot(kind="bar")


# In[35]:


merged = claims.merge(
    food,
    on="Food_ID"
)

merged = merged.merge(
    providers,
    on="Provider_ID"
)


# In[36]:


success = merged[
    merged["Status"]=="Completed"
]

success.groupby("Name")\
       .size()\
       .sort_values(ascending=False)\
       .head(10)


# In[37]:


food_provider = food.merge(
    providers,
    on="Provider_ID"
)


# In[38]:


food_provider.groupby("Name")["Quantity"]\
             .sum()\
             .sort_values(ascending=False)\
             .head(10)


# In[39]:


food_provider.groupby("Name")["Quantity"]\
             .sum()\
             .sort_values(ascending=False)\
             .head(10)\
             .plot(kind="bar")


# In[40]:


food["Days_Left"] = (
    food["Expiry_Date"] -
    pd.Timestamp.today()
).dt.days


# In[41]:


food[food["Days_Left"] <= 7]


# In[42]:


sns.histplot(food["Days_Left"], bins=20)
plt.title("Food Expiry Distribution")
plt.show()


# In[43]:


claims["Month"] = claims["Timestamp"].dt.month_name()
claims["Month"].value_counts()


# In[44]:


claims["Month"].value_counts().plot(
    kind="bar"
)

plt.title("Monthly Claims")
plt.show()


# In[45]:


numeric_cols = food[["Quantity"]]

sns.heatmap(
    numeric_cols.corr(),
    annot=True
)

plt.show()






