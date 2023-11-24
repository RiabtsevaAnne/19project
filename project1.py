import pandas as pd

input_file = 'list.txt'  
with open(input_file, 'r') as file:
    input_list = file.read().splitlines()

print("Початковий список:")
print(input_list)

unique_values = pd.Series(list(set(input_list)))

output_file = 'result.txt'  
unique_values.to_csv(output_file, index=False, header=False)

print("\nУнікальні значення:")
print(unique_values)
print(f"\nМасив Series був збережений у файл {output_file}")
