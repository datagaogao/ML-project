#!/usr/bin/env python
# coding: utf-8

# ## 1. Get webpage using *requests*

# In[1]:


# install libraries 
pip install requests beautifulsoup4 pandas


# In[17]:


# Send a GET request to the URL
import requests

url= 'https://en.wikipedia.org/wiki/List_of_United_States_insurance_companies'
req = requests.get(url)


# In[18]:


# Check the status code to ensure the request was successful
req


# In[19]:


webpage = req.text


# In[20]:


print(webpage)


# In[21]:


# Parse the HTML content of the page
from bs4 import BeautifulSoup
import pandas as pd

soup = BeautifulSoup(webpage, 'html.parser')


# In[28]:


# Find all headings and their corresponding lists
sections = {
    "Property and casualty insurance": [],
    "Life and annuity": [],
    "Health insurance (major medical insurance)": [],
    "Workers' compensation": []
}


# In[29]:


# Iterate over sections and find corresponding lists
for section in sections:
    header = soup.find('span', id=section.replace(' ', '_'))
    if header:
        ul = header.find_next('ul')
        if ul:
            items = ul.find_all('li')
            sections[section] = [item.text.strip() for item in items]


# In[30]:


# Flatten the lists into a single list of insurance companies
data = []
for section, items in sections.items():
    for item in items:
        data.append([item, section])


# In[31]:


# Create a DataFrame
df = pd.DataFrame(data, columns=["Insurance Company", "Category"])


# In[32]:


# Save the DataFrame to a CSV file
df.to_csv('us_insurance_companies_list.csv', index=False)


# In[33]:


# Display the DataFrame
df.head(20)

