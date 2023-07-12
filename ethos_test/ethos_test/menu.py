from dataframe_cleaned_data import * #IMPORT THE ANOTHER CODE WITH DATA FROM EACH ASSOCIATION


#MENU FOR EACH ASSOCIATIONS
print(10*'=' +  ' Selecione a associação ou fonte de notícia desejada ' + 10*'=')
print('1 - IBRAM')
print('2 - AMCHAM')
print('3 - CNA')
print('4 - APROSOJA')
print('5 - Desenvolvimento São Paulo ')
print('6 - Alesp')
print('7 - FIEMG')
print('8 - Instituto Socioambiental')
print('9 - Ministério do Meio Ambiente')
print('10 - Governo de São Paulo')

#THE OPTIONS SELECTED FOR ASSOCIATION
fonte = input('Opção Selecionada: ')

#FUNCTION FOR IBRAM
def ibram_function():
    lista_ibram_nova = []
    for i in range(len(ibram_dataframe_final)):
        lista_ibram_nova.append(ibram_dataframe_final.iloc[i,0])
        lista_ibram_nova.append(ibram_dataframe_final.iloc[i,1])
        #Concatening headline with link and changing the lista_ibram_nova:
    return print(lista_ibram_nova)

#FUNCTION FOR AMCHAM
def amcham_function():
    lista_amcham_nova = []
    counter = 0
    for i in range(len(amcham_dataframe)):
        lista_amcham_nova.append(amcham_dataframe.iloc[i,0])
        lista_amcham_nova.append(amcham_dataframe.iloc[i,2])
    return print(lista_amcham_nova)

#FUNCTION FOR CNA
def cna_function():
    lista_cna_nova = []
    counter = 0
    for i in range(len(cna_dataframe)):
        lista_cna_nova.append(cna_dataframe.iloc[i,0])
        lista_cna_nova.append(cna_dataframe.iloc[i,2])
    return print(lista_cna_nova)

#FUNCTION FOR APROSOJA
def aprosoja_function():
    lista_aprosoja_nova = []
    for i in range(len(aprosoja_dataframe)):
        lista_aprosoja_nova.append(aprosoja_dataframe.iloc[i,0])
        lista_aprosoja_nova.append(aprosoja_dataframe.iloc[i,2])
        #Concatening headline with link and changing the lista_ibram_nova:
    return print(lista_aprosoja_nova)

#FUNCTION FOR DEVELOPMENT SP
def desenvolvimento_function():
    lista_desenvolvimento_nova = []
    counter = 0
    for i in range(len(desenvolvimento_dataframe)):
        lista_desenvolvimento_nova.append(desenvolvimento_dataframe.iloc[i,0])
        lista_desenvolvimento_nova.append(desenvolvimento_dataframe.iloc[i,1])
    return print(lista_desenvolvimento_nova)

#FUNCTION FOR ALESP
def alesp_function():
    lista_alesp_nova = []
    counter = 0
    for i in range(len(alesp_final_dataframe)):
        lista_alesp_nova.append(alesp_final_dataframe.iloc[i,0])
        lista_alesp_nova.append(alesp_final_dataframe.iloc[i,1])
    return print(lista_alesp_nova)

#Function for FIEMG
def fiemg_function():
    lista_fiemg_nova = []
    counter = 0
    for i in range(len(fiemg_dataframe)):
        lista_fiemg_nova.append(fiemg_dataframe.iloc[i,0])
        lista_fiemg_nova.append(fiemg_dataframe.iloc[i,2])
    return print(lista_fiemg_nova)

#Function for Enviromental Ministery
def meioambiente_function():
    lista_ambiente_nova = []
    counter = 0
    for i in range(len(ministerio_meio_ambiente_dataframe)):
        lista_ambiente_nova.append(ministerio_meio_ambiente_dataframe.iloc[i,0])
        lista_ambiente_nova.append(ministerio_meio_ambiente_dataframe.iloc[i,1])
    return print(lista_ambiente_nova)

#Function for SP Government
def governo_sampa_function():
    lista_governo_sampa_nova = []
    counter = 0
    for i in range(len(government_sampa_dataframe)):
        lista_governo_sampa_nova.append(government_sampa_dataframe.iloc[i,0])
        lista_governo_sampa_nova.append(government_sampa_dataframe.iloc[i,1])
    return print(lista_governo_sampa_nova)

#IF ELSE CONDITIONS FOR EACH VALUE THAT CAN BE WRITED IN THE "FONTE" VARIABLE
if fonte == '1':
    ibram_function()
if fonte == '4':
    aprosoja_function()
if fonte == '2':
    amcham_function()
if fonte == '3':
    cna_function()
if fonte == '5':
    desenvolvimento_function()
if fonte == '6':
    alesp_function()
if fonte == '7':
    fiemg_function()
if fonte == '9':
    meioambiente_function()
if fonte == '10':
        governo_sampa_function()