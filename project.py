import pandas as pd

input_file = 'data.csv' 
df = pd.read_csv(input_file)

print("Початковий DataFrame:")
print(df)

df['Листопад'] = ['200;300;400;700']
df['Грудень'] = ['400;200;450;500']

output_file = 'updata.csv'  
df.to_csv(output_file, index=False)

print("\nОновлений DataFrame:")
print(df)

