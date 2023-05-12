#!/usr/bin/env python
# coding: utf-8

# In[6]:


#A python program to display all the header tags from wikipedia.org and make datframe
import requests
r = requests.get('https://en.wikipedia.org/wiki/Main_Page')
import pandas as pd
from bs4 import BeautifulSoup
soup = BeautifulSoup(r.text, 'html.parser')
heading_tags =["h1", "h2", "h3"]
for tags in soup.find_all(heading_tags):
    print(tags.name + '   ' + tags.text.strip())
    results = soup.find_all(heading_tags)
first_result = results[0]
first_result
records=[]
for result in results:
    Tagname= tags.name
    Headine=result.find('span').text
    records.append((Tagname,Headine))
    import pandas as pd
df = pd.DataFrame(records, columns=['Tagname', 'Headine'])

df.head()


# In[135]:


from bs4 import BeautifulSoup
import requests
import pandas as pd
# Downloading imdb top 50 movie's data
url = 'https://www.imdb.com/list/ls055386972/?st_dt=&mode=simple&page=1&ref_=ttls_vw_smp&sort=list_order,asc'
response = requests.get(url)
soup = BeautifulSoup(response.text,'html.parser')
Result = soup('div', class_="lister-item mode-simple")
first_Result = Result[0]
first_Result
records=[]
for result in Result:
    movietital=result.find('span',class_='lister-item-header').text[5:-9]
    Releaseyear=result.find('span',class_='lister-item-year text-muted unbold').text[1:-1]
    rating = result.find('strong').text[2:-4]
    records.append((movietital,Releaseyear,rating))
    import pandas as pd
df = pd.DataFrame(records, columns=['movietital', 'Releaseyear','rating'])

df.head()


# In[10]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




