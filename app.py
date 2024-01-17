import pandas as pd

# Import data frames
sales_df = pd.read_excel("datasets/Vendas.xlsx")
sales_dez_df = pd.read_excel("datasets/Vendas - Dez.xlsx")
managers_df = pd.read_excel("datasets/Gerentes.xlsx")

# Adding Dezember Sales to Sales
#sales_df = sales_df.append(sales_dez_df, ignore_index=True)
sales_df = pd.concat([sales_df, sales_dez_df])

# Total by Product Sale by Story
sales_prod_store_df = sales_df[["ID Loja", "Produto", "Valor Final"]].groupby(["ID Loja", "Produto"]).sum().reset_index()

# Total of Sales by Story
sales_store_df = sales_prod_store_df[["ID Loja","Valor Final"]].groupby("ID Loja").sum().reset_index()

# Adding Managers to Sales Store
sales_store_df = sales_store_df.merge(managers_df)

print(sales_df)
print(sales_prod_store_df)
print(sales_store_df)