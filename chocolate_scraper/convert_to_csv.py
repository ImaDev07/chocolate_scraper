import json
import csv


input_file = r'C:\Users\Admin\PycharmProjects\pythonProject16\chocolate_scraper\products.json'
output_file = r'C:\Users\Admin\PycharmProjects\pythonProject16\chocolate_scraper\products.csv'

with open(input_file, 'r', encoding='utf-8') as f:
    content = f.read()

parts = content.split('][')

parts[0] += ']'
parts[1] = '[' + parts[1]

try:
    products1 = json.loads(parts[0])
    products2 = json.loads(parts[1])
except json.JSONDecodeError as e:
    print(f'Ошибка при разборе JSON: {e}')
    exit(1)

products = products1 + products2

if not products:
    print('Список товаров пуст.')
    exit(1)

fieldnames = products[0].keys()

with open(output_file, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(products)

print(f'CSV успешно создан: {output_file}')
