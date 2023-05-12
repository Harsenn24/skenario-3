import pandas as pd

# Step 1: Open CSV file using Pandas
data = pd.read_csv('transaksi.csv', delimiter=';')
# print(data)

# total transaksi
income_total = data['pendapatan'].sum()
print(income_total)

# total transaksi tertinggi
highest_sale = data[data['pendapatan'] == data['pendapatan'].max()]
print(highest_sale)

# total transaki atau baris
total_transaction = len(data)
print(total_transaction)

# produk yang terjual
product_sold = data[data['terjual'] > 0]
product_name = product_sold['produk'].tolist()
print(product_name)
