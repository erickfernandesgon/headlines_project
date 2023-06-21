import pandas as pd
import numpy as np
new_dataframe = pd.read_json(r'C:\Users\egoncal9\PycharmProjects\pythonProject2\ethos_test\newversion2.json')


#Ministério do Meio Ambiente

#Creating a list with MMA headlines and Dates

lista_mma_headlines = new_dataframe['ministerio_meio_ambiente_news']
lista_mma_dates = new_dataframe['ministerio_meio_ambiente_data']
lista_mma_links = new_dataframe['ministerio_meio_ambiente_link']

#CNA

#Creating new lists for these dataframes
lista_cna_headlines_first, lista_cna_headlines_second = new_dataframe['headline_cna_mainly'], new_dataframe['headline_cna_secondpart']

#Cleaning NaN values and reseting index for CNA


lista_cna_headlines_first.dropna(inplace=True)
lista_cna_headlines_second.dropna(inplace=True)
lista_cna_headlines_first = lista_cna_headlines_first.reset_index(drop=True)
lista_cna_headlines_second = lista_cna_headlines_second.reset_index(drop=True)

#Removing \n\t\t\t characteres for lista_cna_headlines_second[:][0]:
for i in range(len(lista_cna_headlines_second[:][0])):
    lista_cna_headlines_second[i] = lista_cna_headlines_second[i][0]


for elemento in range(len(lista_cna_headlines_second)):
    lista_cna_headlines_second[elemento] = lista_cna_headlines_second[elemento][0].strip()

#Reordening each element for lista_cna_headlines_first in order to remove '[]'

for i in range(len(lista_cna_headlines_first)):
    lista_cna_headlines_first[i] = lista_cna_headlines_first[i][0]

#Concatening the first and second columns

cna_headlines_final = [lista_cna_headlines_first, lista_cna_headlines_second]
cna_headlines_final = pd.concat(cna_headlines_final, ignore_index=True)

#Dropping [3] line in cna_headlines_final:
cna_headlines_final.drop([3], inplace=True)

#Reseting index in cna_headlines_final
cna_headlines_final = cna_headlines_final.reset_index(drop=True)

#Getting the first 5 rows on:

cna_headlines_final = cna_headlines_final[:5]


#Aprosoja
headline_aprosja, date_aprosja, links_aprosja = new_dataframe['headline_aprosja'], new_dataframe['aprosja_dates'], new_dataframe['links_aprosja']


## Removing NaN values
headline_aprosja.dropna(inplace=True)
date_aprosja.dropna(inplace=True)
links_aprosja.dropna(inplace=True)
#Reseting index for headline_aprosja
headline_aprosja = headline_aprosja.reset_index(drop=True)
date_aprosja = date_aprosja.reset_index(drop=True)
links_aprosja = links_aprosja.reset_index(drop=True)


#Dividing the headline_aprosja  items in a list with commas
headline_aprosja = headline_aprosja[0].split("'")



#Replacing \n elements and another elements on headline_aprosja:
replace_this_elements = [r'\n ', r'\n', r'\t', 'Fortalecimento Institucional', "['                              '", "['                              '", "                          ']", '                       ', '                   ', '    ']

for i in range(len(headline_aprosja)):
    for character in replace_this_elements:
        headline_aprosja[i] = headline_aprosja[i].replace(character,'')

# Changing '' for np.nan in headline_aprosja
character_to_change_nan = ["[", "   ",", ", '',']', 'Defesa Agrícola', 'Política Agrícola e Logística']
for i in range(len(headline_aprosja)):
    for character in character_to_change_nan:
        if headline_aprosja[i] == character:
            headline_aprosja[i] = np.nan


#Creating a DataFrame to drop NaN values
headline_aprosja_dataframe_drop = pd.DataFrame(headline_aprosja)
headline_aprosja_dataframe_drop.dropna(inplace=True)
headline_aprosja_dataframe_drop = headline_aprosja_dataframe_drop.reset_index(drop=True)

new_dataframe['links_aprosja'].dropna(inplace=True)
new_dataframe['links_aprosja'] = new_dataframe['links_aprosja'].reset_index(drop=True)

#Spliting the aprosoja links in a list

links_defined = links_aprosja[0].split(',')
links_to_be_removed = [" 'https://www.aprosoja.com.br/comissao/fortalecimento-institucional'", " 'https://www.aprosoja.com.br/comissao/defesa-agricola'",  '" https://www.aprosoja.com.br/comissao/politica-agricola"']

#Creating a looping in order to remove classified links
for i in range(len(links_defined)):
        if links_defined[i] == " 'https://www.aprosoja.com.br/comissao/fortalecimento-institucional'":
            links_defined[i] = np.nan
        if links_defined[i] == " 'https://www.aprosoja.com.br/comissao/defesa-agricola'":
            links_defined[i] = np.nan
        if links_defined[i] == '" https://www.aprosoja.com.br/comissao/politica-agricola"':
            links_defined[i] = np.nan
        if links_defined[i] == " 'https://www.aprosoja.com.br/comissao/sustentabilidade'":
            links_defined[i] = np.nan


#Creating a dictionary to iterate and get the link without repeat
dictionary_links = {'links_label':links_defined}
links_aprosja_without_nan = pd.DataFrame(dictionary_links)

#Iterating over links_aprosja_without_nan to get links that aren't repeat

counter_links = 0
links_aprosja_final = []

for i in range(len(links_aprosja_without_nan)):
    links_aprosja_final.append(links_aprosja_without_nan.iloc[counter_links, 0])
    counter_links = counter_links + 5
    if counter_links == 40:
        break

links_aprosja_final = links_aprosja_final[:5]


#Getting the headlines for aprosoja
counter = 1
headline_aprosja_final = []
for i in range(24):
    headline_aprosja_final.append(headline_aprosja_dataframe_drop.iloc[counter,0])
    counter = counter + 3
    if counter == 16:
        break

counter = 0
dates_aprosja_final = []
for i in range(22):
    dates_aprosja_final.append(headline_aprosja_dataframe_drop.iloc[counter,0])
    counter = counter + 3
    if counter == 15:
        break


#Dropping Na for MMA links:
lista_mma_links.dropna(inplace=True)
lista_mma_headlines.dropna(inplace=True)
lista_mma_dates.dropna(inplace=True)
#Reset index for MMA
lista_mma_headlines = lista_mma_headlines.reset_index(drop=True)
lista_mma_links = lista_mma_links.reset_index(drop=True)
lista_mma_dates = lista_mma_dates.reset_index(drop=True)

#Getting the data for the first 5 values
lista_mma_headlines = list(lista_mma_headlines[0:5])
lista_mma_links = list(lista_mma_links[0:5])

#Removing \n characteres
for i in range(len(lista_mma_dates[0])):
    lista_mma_dates[0][i] = lista_mma_dates[0][i].strip()

lista_dates_only_mma = []
# Putting the date list in the interval greater than one
lista_mma_dates = lista_mma_dates[0][1:]


# Replace null, time and "notícias" with NaN values
for i in range(len(lista_mma_dates)):
    if lista_mma_dates[i] == '':
        lista_mma_dates[i] = np.nan
    if lista_mma_dates[i] == 'Notícia':
        lista_mma_dates[i]= np.nan
    if 'h' in str(lista_mma_dates[i]):
        lista_mma_dates[i] = np.nan

#Transforming the list in a dataframe to drop nan values

lista_mma_dates_dataframe = pd.DataFrame(lista_mma_dates)
lista_mma_dates_dataframe.dropna(inplace=True)

##Reseting index
lista_mma_dates_dataframe = lista_mma_dates_dataframe.reset_index(drop=True)

#Creating a list through MMA dates dataframe
dates_ministerio_meio_ambiente = []
for i in range(len(lista_mma_dates_dataframe)):
    dates_ministerio_meio_ambiente.append(lista_mma_dates_dataframe[0][i])

#Getting the first 5 elements from dates ministério meio ambiente:
dates_ministerio_meio_ambiente = dates_ministerio_meio_ambiente[0:5]

#Getting a new list without \n
lista_mma_headlines_final = []
for i in range(len(lista_mma_headlines)):
    lista_mma_headlines_final.append(lista_mma_headlines[i][1])

#Creating a list to put headlines on
mma_lists_headlines = []
ibram_lists_datas = []

for i in range(5):
    mma_lists_headlines.append(lista_mma_headlines[i][1])

#AMCHAM

#Creating a list with Date and headlines
lista_amcham = new_dataframe['AMCHAM_HEADLINES'].dropna()

#Reset index on AMCHAM headlines after drop NaN values
lista_amcham = lista_amcham.reset_index(drop=True)

#Creating AMCHAM link column
links_amcham = new_dataframe['AMCHAM_LINKS']

#Removing NaN files in Amcham link column

links_amcham = links_amcham.dropna()

#Reset index on AMCHAM headlines after drop NaN values
links_amcham = links_amcham.reset_index(drop=True)

amcham_lists_headlines = []

#Creating a list to split:

for i in range(5):
    amcham_lists_headlines.append(lista_amcham[i])

# Split list

for i in range(len(amcham_lists_headlines)):
    amcham_lists_headlines[i] = amcham_lists_headlines[i].split(r'\n')

#Loop for create a list to dataframe
amcham_list_oficial = []
amcham_datas = []

for i in range(5):
    amcham_list_oficial.append(amcham_lists_headlines[i][49])
    amcham_datas.append(amcham_lists_headlines[i][14])


#fiemg

## Creating a list through fiemg Dataframe
### Headline
fiemg_headline_list = new_dataframe['FIEMG_NEWS_HEADLINE']
fiemg_links_list = new_dataframe['FIEMG_NEWS_HEADLINE_LINK']

#### Dropping the nan values and resetting index
fiemg_headline_list.dropna(inplace=True)
fiemg_headline_list = fiemg_headline_list.reset_index(drop=True)
fiemg_links_list.dropna(inplace=True)
fiemg_links_list = fiemg_links_list.reset_index(drop=True)



fiemg_lists_headlines = []
####Creating a list to split fiemg:

for i in range(7):
    fiemg_lists_headlines.append(fiemg_headline_list[i])

for i in range(7):
    fiemg_lists_headlines[i] = fiemg_lists_headlines[i].split(r'\n')

##### Creating a list to get headlines only:
headlines_fiemg = []
for i in range(len(fiemg_lists_headlines)):
    headlines_fiemg.append(fiemg_lists_headlines[i][8])

#### Creating a list to get dates only:
dates_fiemg = []
for i in range(len(fiemg_lists_headlines)):
    dates_fiemg.append(fiemg_lists_headlines[i][2])

#Creating a list with fiemg source:

fiemglink = ['https://www7.fiemg.com.br']

links_fiemg = []

#Getting the first 5 headlines
headlines_fiemg = headlines_fiemg[0:5]
fiemg_links_list = fiemg_links_list[0:5]
dates_fiemg = dates_fiemg[0:5]

#Iterate through fiemg_links_list concatenating fiemglink and fieg_links_list
for i in range(len(fiemg_links_list)):
    links_fiemg.append(fiemglink[0] + str(fiemg_links_list[i]))

#Creating a link format to each list object
for i in range(len(links_fiemg)):
    links_fiemg[i] = links_fiemg[i].replace("['/Noticias/Detalhe/", "/Noticias/Detalhe/")

#Replacing linespaces in headlines_fiemg
for i in range(len(headlines_fiemg)):
    headlines_fiemg[i] = headlines_fiemg[i].replace(r', ', "")
    headlines_fiemg[i] = headlines_fiemg[i].replace(r'    ''', '')
    headlines_fiemg[i] = headlines_fiemg[i].replace(str(headlines_fiemg[i][0]), '')

#Replacing linespaces in dates and another characteres
for i in range(len(dates_fiemg)):
    dates_fiemg[i] = dates_fiemg[i].replace(r', ',"")
    dates_fiemg[i] = dates_fiemg[i].replace(r'                            ', "")
    dates_fiemg[i] = dates_fiemg[i].replace(dates_fiemg[i][0], "")

#Creating a list with links, headlines and dates

lista_ibram = new_dataframe['IBRAM_HEADLINES']
lista_ibram_links = new_dataframe['IBRAM_LINKS']
lista_ibram_datas = new_dataframe['IBRAM_DATA_HEADLINE']


#Dropping NaN files

new_dataframe['IBRAM_HEADLINES'].dropna(inplace=True)
new_dataframe['IBRAM_LINKS'].dropna(inplace=True)
new_dataframe['IBRAM_DATA_HEADLINE'].dropna(inplace=True)

#Reset index after drop
lista_ibram = lista_ibram.reset_index(drop=True)
lista_ibram_links = lista_ibram_links.reset_index(drop=True)
lista_ibram_datas = lista_ibram_datas.reset_index(drop=True)

#Creating a list to put headlines on
ibram_lists_headlines = []
ibram_lists_datas = []

for i in range(11):
    ibram_lists_headlines.append(lista_ibram[i])

for i in range(11):
    ibram_lists_datas.append(lista_ibram_datas[i])

# Strip list for Ibram dates and headlines

for i in range(len(ibram_lists_headlines)):
    ibram_lists_headlines[i] = ibram_lists_headlines[i][0].strip()

for i in range(len(ibram_lists_datas[0])):
    ibram_lists_datas[0][i] = ibram_lists_datas[0][i].strip()


# Creating a list with the dates
ibram_datas = []
ibram_lists_datas[0] = ibram_lists_datas[0][1:]

# Replace space values with NaN values
for i in range(len(ibram_lists_datas[0])):
    if ibram_lists_datas[0][i] == '':
        ibram_lists_datas[0][i] = np.nan

#Creating a new Dataframe to Drop NaN values

ibram_dataframe_drop_nan = pd.DataFrame(ibram_lists_datas[0])
ibram_dataframe_drop_nan.dropna(inplace=True)

#Reset index

datas_ibram_dataframe = ibram_dataframe_drop_nan.reset_index(drop=True)

#Creating a new list
datas_ibram_cleaned = list(datas_ibram_dataframe[0])

# Creating pandas DataFrame object from a dictionary for AMCHAM

amcham_dictionary = {'HEADLINES AMCHAM': amcham_list_oficial,
        'Datas_AMCHAM': amcham_datas, 'Links AMCHAM':links_amcham}
amcham_dataframe = pd.DataFrame(amcham_dictionary)

# Creating a pandas DataFrame object from a dictionary for IBRAM

ibram_dictionary = {'HEADLINES IBRAM':ibram_lists_headlines, 'LINKS IBRAM':lista_ibram_links, 'IBRAM DATAS':datas_ibram_cleaned}
ibram_dataframe_final = pd.DataFrame(ibram_dictionary)


# Creating a pandas Dataframe from a dictionary for MMA:

mma_dictionary = {'HEADLINES MMA':mma_lists_headlines, 'MMA LINKS': lista_mma_links, 'MMA DATAS':dates_ministerio_meio_ambiente}
ministerio_meio_ambiente_dataframe = pd.DataFrame(mma_dictionary)

# Creating a pandas Dataframe through a dictionary for fiemg:

fiemg_dictionary = {'HEADLINES fiemg':headlines_fiemg, 'DATES fiemg':dates_fiemg, 'Links fiemg': links_fiemg}
fiemg_dataframe = pd.DataFrame(fiemg_dictionary)

#Creating a dictionary and dataframe to APROSOJA

aprosoja_dictionary = {'HEADLINES APROSOJA':headline_aprosja_final, 'DATES APROSOJA':dates_aprosja_final, 'LINKS APROSOJA':links_aprosja_final}
aprosoja_dataframe = pd.DataFrame(aprosoja_dictionary)

