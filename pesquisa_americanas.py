import lib_americanas

busca = input()
df = lib_americanas.scrapy_attributes_to_pandas(busca)
df = df.sort_values(by='valor')
lib_americanas.add_pandas_to_xlsx(df)