import csv

with open('s'/Users//Users/marcellaferreira/Downloads/top_50_canadian_stocks_data_since_2010.csv'', newline='') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv)
    for linha in leitor_csv:
        print(linha)
