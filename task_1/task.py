import pandas as pd

data_df = pd.read_csv('data.csv', sep='\t', skiprows=1, names=['part_number', 'manufacturer'])
prices_df = pd.read_csv('prices.csv', sep='\t', skiprows=1, names=['part_number', 'price'])
quantity_df = pd.read_csv('quantity.csv', sep='\t', names=['part_number', 'quantity'])

merged_df = pd.merge(data_df, prices_df, on='part_number')
merged_df = pd.merge(merged_df, quantity_df, on='part_number')

merged_df['quantity'] = pd.to_numeric(merged_df['quantity'], errors='coerce')
merged_df['price'] = pd.to_numeric(merged_df['price'], errors='coerce')

filtered_df = merged_df[(merged_df['quantity'] > 0) & (merged_df['price'] > 0)]

filtered_df = filtered_df.drop_duplicates()

filtered_df.to_csv('data_edit.csv', index=False)

manufacturer_counts = filtered_df['manufacturer'].value_counts()
for manufacturer, count in manufacturer_counts.items():
    print(f"{manufacturer} - {count} rows")
