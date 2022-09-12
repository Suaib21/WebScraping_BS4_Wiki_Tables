import requests
from bs4 import BeautifulSoup
import pandas as pd

#Download Wikipage
Wikipage = "https://en.wikipedia.org/wiki/List_of_sovereign_states_and_dependent_territories_by_continent_(data_file)"
results = requests.get(Wikipage)
# print(results.status_code)

if results.status_code == 200:
    soup = BeautifulSoup(results.content,"html.parser")
table = soup.find('table',{'class':'wikitable sortable'})
# print(table.text)

#Loop through all the rows and pull the text
new_table = []
for row in table.find_all('tr')[1:]:
    column_maker = 0
    columns = row.find_all('td')
    new_table.append([column.get_text() for column in columns])
    # print(new_table)

df = pd.DataFrame(new_table,columns=['Con_Code','Alpha2','Alpha3','PhoneCode',"Name"])
df['Name']=df["Name"].str.replace('\n','')

#Create CSV
df.to_csv('E:\Machine Learning\WebScraping\Wiki_table.csv',index=False)
print(df)