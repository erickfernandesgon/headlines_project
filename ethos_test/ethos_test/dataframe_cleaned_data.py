import pandas as pd
import numpy as np
import re
new_dataframe = pd.read_json(r'C:\Users\egoncal9\PycharmProjects\pythonProject2\ethos_test\newversion2.json')

#Alesp

alesp_headlines = new_dataframe['headline_alesp']
alesp_links = new_dataframe['links_alesp']
alesp_dates = new_dataframe['data_publicacao_alesp']

#Cleaning NaN values and resetting index for alesp_dates
alesp_dates.dropna(inplace=True),
alesp_dates = alesp_dates.reset_index(drop=True)

#Cleaning NaN values and resetting index for links_alesp
alesp_links.dropna(inplace=True),
alesp_links = alesp_links.reset_index(drop=True)

#Splitting alesp_links into a list
alesp_links = alesp_links[0].split(',')

#Getting the elements as of index 1
alesp_links = alesp_links[1:]

#Getting the 39 links only:
alesp_links = alesp_links[:39]

#Getting pair values only
counter = 0
alesp_links_pair = []
for i in range(len(alesp_links)):
    alesp_links_pair.append(alesp_links[counter])
    counter = counter + 2
    if counter == 38:
        break

#Getting the first five elements:
alesp_links_pair = alesp_links_pair[:11]
#Stripping the list to remove space on links:
for i in range(len(alesp_links_pair)):
    alesp_links_pair[i] = alesp_links_pair[i].strip()

#Stripping the list in order to remove "'":
for i in range(len(alesp_links_pair)):
    alesp_links_pair[i] = alesp_links_pair[i].strip("'")

#Creating a link to alespwebsite
website_alesp_link = 'https://www.al.sp.gov.br/'
links_final_alesp = []

#Iterate over a list of links and concatening the link with another part
for i in range(len(alesp_links_pair)):
    links_final_alesp.append(str(website_alesp_link) + str(alesp_links_pair[i]))

#Cleaning NaN values and resetting index for alesp_headlines
alesp_headlines.dropna(inplace=True)
alesp_headlines = alesp_headlines.reset_index(drop=True)

#Removing elements that use "\n" through a loop
alesp_removing_list = [r' \r\n \t\t\t \r\n \t\t          \r\n  \r\n  \r\n  \r\n  \r\n  \r\n  \r\n  \r\n  \r\n  \r\n ', r' \r\n \t \r\n \t\t \r\n  \r\n \t\t\t', " 'Paz nos estádios", " 23'",' Autor ', ' Resumo', 'Buscar ', 'Pesquisa mais abrangente',' Título ', r' \xa0 ', 'Notícias ', r'\t', r'\t\t', r' \r\n ', r'\t\t\t', r'\t \r\n \t\t', r'\t\t\t         ',r'\t\t\t\t\t',r' \r\n \t', r' \r\n  \r\n ', r' \r\n \t \r\n \t\t \r\n  \r\n \t\t\t', r' \r\n \t\t\t \r\n \t\t          \r\n  \r\n  \r\n  \r\n  \r\n  \r\n  \r\n  \r\n  \r\n  \r\n ', 'Informações: imprensa@al.sp.gov.br', r' \r\n  \r\n \t\t\t \r\n  \r\n \t\t \r\n \t\t \r\n \t',r'  \r\n \t\t\t\t', r' \r\n \t\t\t\t\t',r' \r\n  \r\n  \r\n \t\t\t \r\n \t\t\t', r' \r\n  \r\n \t\t\t', r' \r\n Notícias  \r\n  \r\n ', r' \r\n \t\t\t\t\t\t']

pattern = r"(?<=')\s*,\s*(?=')"

#Splitting commas in alesp_headlines
for i in range(len(alesp_headlines)):
    alesp_headlines = re.split(pattern, alesp_headlines[i])

#Replacing some values in list splitted to empty values
for i in range(len(alesp_headlines)):
    for variable in range(len(alesp_removing_list)):
        alesp_headlines[i] = alesp_headlines[i].replace(alesp_removing_list[variable], '')


#Getting the part of the list that have headlines only
alesp_headlines = alesp_headlines[:285]


#Verifying if the elements in the list have string part 'Publicado em: ' and switch it for NaN values
string_remove = 'Publicado em: '
for i in range(len(alesp_headlines)):
    if string_remove in str(alesp_headlines[i]):
        alesp_headlines[i] = ''

alesp_to_nan = ["''"," ''", " '         '", "[''", '', " '", '         ', str(alesp_headlines[3]), "[", ', ', "' '"]
#Changing empty values for NaN values
for i in range(len(alesp_headlines)):
    for element in alesp_to_nan:
        if alesp_headlines[i] == element:
            alesp_headlines[i] = np.nan

#Creating a Dataframe to alesp_headlines, removing NaN values, dropingna and replace values:
alesp_dataframe_headlines = pd.DataFrame(alesp_headlines)
alesp_dataframe_headlines.dropna(inplace=True)
alesp_dataframe_headlines = alesp_dataframe_headlines.reset_index(drop=True)

#Getting the first 11 elements on alesp_headlines
alesp_dataframe_headlines = alesp_dataframe_headlines[:11]
#Creating a list using alesp_dataframe_headlines
alesp_headlines_list = []
for i in range(len(alesp_dataframe_headlines)):
   alesp_headlines_list.append(alesp_dataframe_headlines.iloc[i,0])

#Getting the first 11 dates on alesp_dates
alesp_dates = alesp_dates[:11]

#Replacing 'Publicado em' for ''
for i in range(len(alesp_dates)):
    alesp_dates[i] = alesp_dates[i].replace('Publicado em: ', '')

#Getting dates without time for alesp_dates[0][12:]
for i in range(len(alesp_dates)):
    alesp_dates[i] = alesp_dates[i][2:12]

#Creating a dictionary to alesp_headlines and links_final_alesp
alesp_dictionary = {'HEADLINES ALESP':alesp_headlines_list, 'LINKS ALESP':links_final_alesp, 'DATES ALESP':alesp_dates}

#Creating the final dataframe with alesp_final_dataframe
alesp_final_dataframe = pd.DataFrame(alesp_dictionary)

#Instituto Sócio Ambiental

#Creating a list with mapa headlines and Dates
lista_mapa_headlines = new_dataframe['headline_mapa']
lista_mapa_links = new_dataframe['links_mapa']
lista_mapa_dates = new_dataframe['date_mapa']

#Cleaning NaN values for lista_mapa_headlines, lista_mapa_dates and lista_mapa_links:
lista_mapa_headlines.dropna(inplace=True)
lista_mapa_links.dropna(inplace=True)
lista_mapa_dates.dropna(inplace=True)

#Reset index forlista_mapa_headlines, lista_mapa_dates and lista_mapa_links:
lista_mapa_headlines = lista_mapa_headlines.reset_index(drop=True)
lista_mapa_links = lista_mapa_links.reset_index(drop=True)
lista_mapa_dates = lista_mapa_dates.reset_index(drop=True)

#Getting the dates for each headline from list_mapa_dates and reset index:
lista_mapa_dates = lista_mapa_dates[23:32]
lista_mapa_dates = lista_mapa_dates.reset_index(drop=True)

#Getting dates without []
for i in range(len(lista_mapa_dates)):
    lista_mapa_dates[i] = lista_mapa_dates[i][0]

#Turning lista_mapa_dates out object to a list
lista_mapa_dates = list(lista_mapa_dates)

#Getting date format to a format without a time selecting [i] from len and first 10 letters from character
for i in range(len(lista_mapa_dates)):
    lista_mapa_dates[i] = lista_mapa_dates[i][:10]

#Getting the first five dates from lista_mapa_dates
lista_mapa_dates = lista_mapa_dates[:5]

#Getting the links in the lista_mapa_links without any character that don't have link and reseting:
lista_mapa_links = lista_mapa_links[3:22] #Getting the links without empty lists
lista_mapa_links = lista_mapa_links.reset_index(drop=True) #Resetting index
lista_mapa_links = lista_mapa_links[4:18] #Getting the links without empty lists again
lista_mapa_links = lista_mapa_links.reset_index(drop=True) #Resetting the index

#Getting the first five links from lista_mapa_links:
lista_mapa_links = lista_mapa_links[:5]

#Getting the links without '[]':
for i in range(len(lista_mapa_links)):
    lista_mapa_links[i] = lista_mapa_links[i][0]

#Turning the object lista_mapa_links into a list:
lista_mapa_links = list(lista_mapa_links)

#Turning this object in a list
#Getting the items in lista_mapa_headlines from the third  and reset it:
lista_mapa_headlines = lista_mapa_headlines[4:] #Getting the data from third element
lista_mapa_headlines = lista_mapa_headlines.reset_index(drop=True) #Resetting index
lista_mapa_headlines = lista_mapa_headlines[3:21] #Getting the data from the third element again
lista_mapa_headlines = lista_mapa_headlines.reset_index(drop=True) #Resetting index

#Getting the first five elements for lista_mapa_headlines
lista_mapa_headlines = lista_mapa_headlines[:5]

#Getting the headlines from lista_mapa_headlines without breaklines:
for i in range(len(lista_mapa_headlines[:20])):
    lista_mapa_headlines[i] = lista_mapa_headlines[i][1]

#Getting the first five headlines for lista_mapa_
lista_mapa_headlines = lista_mapa_headlines[:5]

#Creating a list to get all elements from lista_mapa_headlines:
lista_mapa_headlines_list = list(lista_mapa_headlines)

#Ministério do Meio Ambiente
#Creating a list with MMA headlines and Dates
lista_mma_headlines, lista_mma_dates, lista_mma_links = new_dataframe['ministerio_meio_ambiente_news'], new_dataframe['ministerio_meio_ambiente_data'], new_dataframe['ministerio_meio_ambiente_link']

#CNA
#Creating new lists for these dataframes
lista_cna_headlines_first, lista_cna_headlines_second = new_dataframe['headline_cna_mainly'], new_dataframe['headline_cna_secondpart']

#Creating new lists for these dataframes in links case:
cna_first_links, cna_second_links = new_dataframe['links_cna'], new_dataframe['links_cma_part2']
cna_dates = new_dataframe['CNA_DATA']

#Cleaning NaN values and reseting index for CNA
#Headlines
lista_cna_headlines_first.dropna(inplace=True)
lista_cna_headlines_second.dropna(inplace=True)
lista_cna_headlines_first = lista_cna_headlines_first.reset_index(drop=True)
lista_cna_headlines_second = lista_cna_headlines_second.reset_index(drop=True)

#Links
cna_first_links.dropna(inplace=True)
cna_second_links.dropna(inplace=True)
cna_first_links = cna_first_links.reset_index(drop=True)
cna_second_links = cna_second_links.reset_index(drop=True)

#Dates
cna_dates.dropna(inplace=True)
cna_dates = cna_dates.reset_index(drop=True)

#Removing \n\t\t\t characteres for lista_cna_headlines_second[:][0]:
for i in range(len(lista_cna_headlines_second)):
    lista_cna_headlines_second[i] = lista_cna_headlines_second[i][0]
for elemento in range(len(lista_cna_headlines_second)):
    lista_cna_headlines_second[elemento] = lista_cna_headlines_second[elemento].strip()

#Reordening each element for lista_cna_headlines_first in order to remove '[]'
for i in range(len(lista_cna_headlines_first)):
    lista_cna_headlines_first[i] = lista_cna_headlines_first[i][0]

#Removing \n\t\t\t\t\t characters for cna_dates:
for i in range(len(cna_dates)):
    cna_dates[i] = cna_dates[i].replace(r'\n\t\t\t\t\t', '')

for i in range(len(cna_dates)):
    cna_dates[i] = cna_dates[i].replace(r'\n\t\t\t\t', '')

#Concatenate cna_links and cna_headlines_first and cna_headlines_secomd:
cna_headlines_final = [lista_cna_headlines_first, lista_cna_headlines_second]
cna_headlines_final = pd.concat(cna_headlines_final, ignore_index=True)
links_cna_final = [cna_first_links, cna_second_links]
links_cna_final = pd.concat(links_cna_final, ignore_index=True)

#Dropping [3] line in cna_headlines_final:
#cna_headlines_final.drop([3], inplace=True)
#cna_headlines_final = cna_headlines_final.reset_index(drop=True)

#Getting the first 5 rows on:
cna_headlines_final = cna_headlines_final[:5]
links_cna_final = links_cna_final[:5]
cna_dates = cna_dates[:5]


#Removing titles with \n\t\t\t
for i in range(len(cna_headlines_final)):
    cna_headlines_final[i] = cna_headlines_final[i].strip()


#Governo de São Paulo website
sp_government_headline = new_dataframe['headline_governo_sampa']

#Dropping NaN values and resetting index
sp_government_headline.dropna(inplace=True)
sp_government_headline = sp_government_headline.reset_index(drop=True)

#Creating a list for SP Government from a split
list_government_sp = sp_government_headline[0].split("'")

#Stripping the list to remove breaklines
for i in range(len(list_government_sp)):
    list_government_sp[i] = list_government_sp[i].strip(r'        \n                          \n       ')

#Removing dates characters
for i in range(len(list_government_sp)):
    if len(list_government_sp[i]) == 18:
        list_government_sp[i] = np.nan
    elif len(list_government_sp[i]) == 17:
        list_government_sp[i] = np.nan

#From 24 item:
list_government_sp = list_government_sp[23:]

#Removing another characters on list_government_sp:
list_of_characters_toremove = ['400', '1', '2', '[', '»', ',', ']', '…']
for i in range(len(list_government_sp)):
    for value in range(len(list_of_characters_toremove)):
        if list_government_sp[i] == list_of_characters_toremove[value]:
            list_government_sp[i] = np.nan

#Switching '' characters for np.nan:
for i in range(len(list_government_sp)):
    if list_government_sp[i] == '':
        list_government_sp[i] = np.nan

#Creating a DataFrame and removing nan values using drop and reset
government_headlines_dataframe = pd.DataFrame(list_government_sp)
government_headlines_dataframe.dropna(inplace=True)
government_headlines_dataframe = government_headlines_dataframe.reset_index(drop=True)

#Getting headlines with pair values only.


gov_counter = 0
for i in range(len(government_headlines_dataframe[0])):
    government_headlines_dataframe[0][i] = government_headlines_dataframe[0][gov_counter]
    gov_counter = gov_counter + 2
    if gov_counter == 18:
        break

#Getting the first five headlines for government_headlines_dataframe:
government_headlines_dataframe = government_headlines_dataframe[0][:5]

#Getting the links for government_sp with a new dataframe:
government_links_dataframe = new_dataframe['links_governo_sampa']

#Dropping and reseting index for government_links_dataframe
government_links_dataframe.dropna(inplace=True)
government_links_dataframe = government_links_dataframe.reset_index(drop=True)


#Splitting government_links_dataframe:
government_links_dataframe = government_links_dataframe[0].split("'")

#Creating a list with odd values for links_government_sp_counter:
government_sampa_counter_links = 1

for i in range(len(government_links_dataframe)):
    government_links_dataframe[i] = government_links_dataframe[government_sampa_counter_links]
    government_sampa_counter_links = government_sampa_counter_links + 2
    if government_sampa_counter_links == 41:
        break

#Getting pair links for governement_links_dataframe:
government_counter_links_two = 0
for i in range(len(government_links_dataframe)):
    government_links_dataframe[i] = government_links_dataframe[government_counter_links_two]
    government_counter_links_two = government_counter_links_two + 2
    if government_counter_links_two == 46:
        break

#Getting the five links for governement_links_dataframe:
government_links_dataframe = government_links_dataframe[:5]

#Getting dates for headline_data_sampa:

##Drop nan values and reset_index
government_date_sampa = new_dataframe['headline_data_sampa']
government_date_sampa.dropna(inplace=True)
government_date_sampa = government_date_sampa.reset_index(drop=True)

#Getting five values only for governement_date_sampa
government_date_sampa = government_date_sampa[:5]

#Getting the first part of the date in government_governement_date_sampa:
for i in range(len(government_date_sampa)):
    government_date_sampa[i] = government_date_sampa[i][0][:10]

#Creating a dictionary for government_date_sampa, governement_links_dataframe and government_headlines_dataframe:
government_sampa_dictionary = {'HEADLINES GOVERNO SP':government_headlines_dataframe, 'LINK DA NOTÍCIA GOVERNO SP':government_links_dataframe, 'DATA DA HEADLINE':government_date_sampa}

#Creating a DataFrame for government_sampa_dictionary
government_sampa_dataframe = pd.DataFrame(government_sampa_dictionary)

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

#Desenvolvimento São Paulo
headline_desenvolvimento_sampa = new_dataframe['headline_desenvolvimento_sampa']  # headlines
links_desenvolvimento_sampa = new_dataframe['links_desenvolvimento_sampa']   #links
headline_data_sampa = new_dataframe['headline_data_sampa'] #dates

#Cleaning NaN values and reset_index for headline_desenvolvimento_sampa and link_desenvolvimento_sampa
headline_desenvolvimento_sampa.dropna(inplace=True) #headlines
headline_desenvolvimento_sampa = headline_desenvolvimento_sampa.reset_index(drop=True) #headlines
(headline_desenvolvimento_sampa[0])
links_desenvolvimento_sampa.dropna(inplace=True) #links
links_desenvolvimento_sampa = links_desenvolvimento_sampa.reset_index(drop=True) #links

#Getting the first index for links_desenvolvimento_sampa:
links_desenvolvimento_sampa = links_desenvolvimento_sampa[0]

#Splitting links_desenvolvimento_sampa into a list
links_desenvolvimento_sampa = links_desenvolvimento_sampa.split(",")
counter_new = 0

#Iterating over links_desenvolvimento_sampa to get pair numbers only
for i in range(len(links_desenvolvimento_sampa)):
    links_desenvolvimento_sampa[i] = links_desenvolvimento_sampa[counter_new]
    counter_new = counter_new + 2
    if counter_new == 24:
        break

#Replacing '[' character in links_desenvolvimento_sampa[0]
links_desenvolvimento_sampa[0] = links_desenvolvimento_sampa[0].replace('[', ' ')

#Getting the first 5 values in links_desenvolvimento_sampa:
links_desenvolvimento_sampa = links_desenvolvimento_sampa[:5]

#Drop and reset in headline_data_sampa
headline_data_sampa.dropna(inplace=True) #dates
headline_data_sampa = headline_data_sampa.reset_index(drop=True)

#Getting dates from :21 and resetting index
headline_data_sampa = headline_data_sampa[21:]
headline_data_sampa = headline_data_sampa.reset_index(drop=True)

#Getting the first 5 dates from headline_date_sampa
headline_data_sampa = headline_data_sampa[:5]

#Creating a list with the elements of the 5 lists from headline_data_sampa
headline_data_sampa_list = []
for i in range(5):
    headline_data_sampa_list.append(headline_data_sampa[i][0].strip()) #strip to remove linebreaks

#Creating a list with breaklines:
breaklines_to_remove = [r'\n\n\t\t\t\t\t\t\n\t\t\t\t\t\t\t', r'\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t', r'\n\t\t\t\t\t\t\t\t\t\t', r'\t\t\t\t\t\t\t\t\t', r'\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t', r'\t', r'\n\t\t\t\t\t\t\t\t\t', r'\n\n\t\t\t\t\t\t\n\t\t\t\t\t', r'\n\t\t\t\t\t\t\t\t', r'\n', r'\t\t\t\t\t\t\t', r'\t\t\t\t\t\t']

#Removing characters with breaklines
for i in range(len(headline_desenvolvimento_sampa)):
    for breakline in range(len(breaklines_to_remove)):
        headline_desenvolvimento_sampa[i]= headline_desenvolvimento_sampa[i].replace(breaklines_to_remove[breakline], '')
(headline_desenvolvimento_sampa[0])
#Splitting headline_desenvolvimento_sampa:
headline_desenvolvimento_sampa = headline_desenvolvimento_sampa[0].split("'")

#Creating a list with the characteres that will be changed in headline_desenvolvimento_sampa
characteres_remov_desenvolv_sampa_part2 = ['[', '', ', ', ']']

#Transform '' elements in np.nan values
for i in range(len(headline_desenvolvimento_sampa)):
   for character in range(len(characteres_remov_desenvolv_sampa_part2)):
      if headline_desenvolvimento_sampa[i] == characteres_remov_desenvolv_sampa_part2[character]:
          headline_desenvolvimento_sampa[i] = np.nan

#Creating a new dataframe from headline_Desenvolvimento_sampa
headline_desenvolvimento_sampa_dataframe = pd.DataFrame(headline_desenvolvimento_sampa)

#Dropping nan values and reseting index for headline_desenvolvimento_sampa_dataframe:
headline_desenvolvimento_sampa_dataframe.dropna(inplace=True)
headline_desenvolvimento_sampa_dataframe = headline_desenvolvimento_sampa_dataframe.reset_index(drop=True)

#Turn dates values on NaN values
for i in range(len(headline_desenvolvimento_sampa_dataframe[0])):
    if len(headline_desenvolvimento_sampa_dataframe[0][i]) == 10:
        headline_desenvolvimento_sampa_dataframe[0][i] = np.nan

#Dropping NaN values and resetting index in headline_sampa_dataframe:
headline_desenvolvimento_sampa_dataframe.dropna(inplace=True)
headline_desenvolvimento_sampa_dataframe = headline_desenvolvimento_sampa_dataframe.reset_index(drop=True)

#Getting the pair values in headline_desenvolvimento_sampa_dataframe only:
counter_headline = 0

for i in range(len(headline_desenvolvimento_sampa_dataframe)):
    headline_desenvolvimento_sampa_dataframe[0][i] = headline_desenvolvimento_sampa_dataframe.iloc[counter_headline,0]
    counter_headline = counter_headline + 2
    if counter_headline == 24:
        break

#Getting the first five headlines on headline_desenvolvimento_sampa_dataframe
headline_desenvolvimento_sampa_dataframe = headline_desenvolvimento_sampa_dataframe[:5]

#Creating a list using headline_desenvolvimento_sampa_dataframe
headline_desenvolvimento_sampa_list = []
for i in range(5):
    headline_desenvolvimento_sampa_list.append(headline_desenvolvimento_sampa_dataframe.iloc[i,0])

#Replacing \n elements and another elements on headline_aprosja:
replace_this_elements = ['PESAR', r'\n ', r'\n', r'\t', 'Fortalecimento Institucional', "['                              '", "['                              '", "                          ']", '                       ', '                   ', '    ']

for i in range(len(headline_aprosja)):
    for character in replace_this_elements:
        headline_aprosja[i] = headline_aprosja[i].replace(character,'')

# Changing '' for np.nan in headline_aprosja
character_to_change_nan = ["[", "   ",", ", '',']', 'Defesa Agrícola', 'Política Agrícola e Logística', 'Sustentabilidade', 'Fortalecimento Institucional']
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
    if lista_mma_dates[i] == 'Notícias':
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

#Getting links from amcham with two similar elements:
list_links_amcham = []
for i in range(len(links_amcham)):
    list_links_amcham.append(links_amcham.iloc[i])


#Creating a list to split links and headlines:
amcham_lists_headlines = []
for i in range(5):
    amcham_lists_headlines.append(lista_amcham[i])

# Split list amcham_lists_headlines and list_links_amcham
for i in range(len(amcham_lists_headlines)):
    amcham_lists_headlines[i] = amcham_lists_headlines[i].split(r'\n')
    list_links_amcham[i] = list_links_amcham[i].split(',') #Spliting the list in comma
    list_links_amcham[i] = list_links_amcham[i][0] #Changing each element of the list for link

links_amcham = list_links_amcham

#Loop for create a list to dataframe
amcham_list_oficial = []
amcham_datas = []

for i in range(5):
    amcham_list_oficial.append(amcham_lists_headlines[i][49])
    amcham_datas.append(amcham_lists_headlines[i][14])

##fiemg
## Creating a list through #fiemg Dataframe
### Headline
#fiemg_headline_list = new_dataframe['#fiemg_NEWS_HEADLINE']
#fiemg_links_list = new_dataframe['#fiemg_NEWS_HEADLINE_LINK']


#print(#fiemg_links_list)
#### Dropping the nan values and resetting index
#fiemg_headline_list.dropna(inplace=True)
#fiemg_headline_list = #fiemg_headline_list.reset_index(drop=True)
#fiemg_links_list.dropna(inplace=True)
#fiemg_links_list = #fiemg_links_list.reset_index(drop=True)

#fiemg_lists_headlines = []
####Creating a list to split #fiemg:
#for i in range(7):
    #fiemg_lists_headlines.append(#fiemg_headline_list[i])
#for i in range(7):
    #fiemg_lists_headlines[i] = #fiemg_lists_headlines[i].split(r'\n')

##### Creating a list to get headlines only:
#headlines_#fiemg = []
#for i in range(len(#fiemg_lists_headlines)):
    #headlines_#fiemg.append(#fiemg_lists_headlines[i][8])

#### Creating a list to get dates only:
#dates_#fiemg = []
#for i in range(len(#fiemg_lists_headlines)):
    #dates_#fiemg.append(#fiemg_lists_headlines[i][2])

#Creating a list with #fiemg source:
#fiemglink = ['https://www7.#fiemg.com.br']
#links_#fiemg = []

#Getting the first 5 headlines
#headlines_#fiemg = headlines_#fiemg[0:5]
#fiemg_links_list = #fiemg_links_list[0:5]
#dates_#fiemg = dates_#fiemg[0:5]

#Iterate through #fiemg_links_list concatenating #fiemglink and fieg_links_list
#for i in range(len(#fiemg_links_list)):
   # links_#fiemg.append(#fiemglink[0] + str(#fiemg_links_list[i]))

#Creating a link format to each list object
#for i in range(len(links_#fiemg)):
   # links_#fiemg[i] = links_#fiemg[i].replace("['/Noticias/Detalhe/", "/Noticias/Detalhe/")

#Replacing linespaces in headlines_#fiemg
#for i in range(len(headlines_#fiemg)):
   # headlines_#fiemg[i] = headlines_#fiemg[i].replace(r', ', "")
   # headlines_#fiemg[i] = headlines_#fiemg[i].replace(r'    ''', '')
   # headlines_#fiemg[i] = headlines_#fiemg[i].replace(str(headlines_#fiemg[i][0]), '')

#Replacing linespaces in dates and another characteres
#for i in range(len(dates_#fiemg)):
   # dates_#fiemg[i] = dates_#fiemg[i].replace(r', ',"")
  # dates_#fiemg[i] = dates_#fiemg[i].replace(r'                            ', "")
   # dates_#fiemg[i] = dates_#fiemg[i].replace(dates_#fiemg[i][0], "")

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
amcham_dictionary = {'HEADLINES AMCHAM': amcham_list_oficial, 'Datas_AMCHAM': amcham_datas, 'Links AMCHAM':links_amcham}
amcham_dataframe = pd.DataFrame(amcham_dictionary)

# Creating a pandas DataFrame object from a dictionary for IBRAM
ibram_dictionary = {'HEADLINES IBRAM':ibram_lists_headlines, 'LINKS IBRAM':lista_ibram_links, 'IBRAM DATAS':datas_ibram_cleaned}
ibram_dataframe_final = pd.DataFrame(ibram_dictionary)

#Getting the first 5 rows for Ibram
ibram_dataframe_final = ibram_dataframe_final.iloc[:5,:]

# Creating a pandas Dataframe from a dictionary for MMA:
mma_dictionary = {'HEADLINES MMA':mma_lists_headlines, 'MMA LINKS': lista_mma_links, 'MMA DATAS':dates_ministerio_meio_ambiente}
ministerio_meio_ambiente_dataframe = pd.DataFrame(mma_dictionary)

# Creating a pandas Dataframe through a dictionary for #fiemg:
#fiemg_dictionary = {'HEADLINES #fiemg':headlines_#fiemg, 'DATES #fiemg':dates_#fiemg, 'Links #fiemg': links_#fiemg}
#fiemg_dataframe = pd.DataFrame(#fiemg_dictionary)

#Creating a dictionary and dataframe to APROSOJA
aprosoja_dictionary = {'HEADLINES APROSOJA':headline_aprosja_final, 'DATES APROSOJA':dates_aprosja_final, 'LINKS APROSOJA':links_aprosja_final}
aprosoja_dataframe = pd.DataFrame(aprosoja_dictionary)

#Creating a dictionary and a DataFrame to CNA
cna_dictionary = {'CNA_HEADLINES':cna_headlines_final, 'DATES_CNA':cna_dates, 'LINKS CNA':links_cna_final}
cna_dataframe = pd.DataFrame(cna_dictionary)

#Creating a dictionary and DataFrame to Ministerio da Agricultura e Pecuaria
mapa_dictionary = {'MAPA_HEADLINES':lista_mapa_headlines, 'MAPA_LINKS':lista_mapa_links, 'DATES_MAPA':lista_mapa_dates}
mapa_dataframe = pd.DataFrame(mapa_dictionary)

#Creating a dictionary and DataFrame to Desenvolvimento SP
desenvolvimento_dictionary = {'HEADLINES DESENVOLVIMENTO SP':headline_desenvolvimento_sampa_list, 'LINK':links_desenvolvimento_sampa, 'DATA DA NOTÍCIA':headline_data_sampa_list}
desenvolvimento_dataframe = pd.DataFrame(desenvolvimento_dictionary)