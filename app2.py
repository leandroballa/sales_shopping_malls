import pandas as pd

# Importing an excel with more then one sheet
#vendas_df = pd.read_excel("datasets/Vendas_together.xlsx", sheet_name=None)
sales_jan_df = pd.read_excel("datasets/Vendas_together.xlsx", sheet_name="Jan")
sales_dez_df = pd.read_excel("datasets/Vendas_together.xlsx", sheet_name="Dez")

# Contating January Sales with Dezember Sales Dezember Sales
sales_df = pd.concat([sales_jan_df, sales_dez_df])


# Total by Product Sale by Story
sales_prod_store_df = sales_df[["ID Loja", "Produto", "Valor Final"]].groupby(["ID Loja", "Produto"]).sum().reset_index()

# Total of Sales by Story
sales_store_df = sales_prod_store_df[["ID Loja","Valor Final"]].groupby("ID Loja").sum().reset_index()

# Adding Managers to Sales Store
sales_store_df = sales_store_df.merge(managers_df)

print(sales_df)
print(sales_prod_store_df)
print(sales_store_df)