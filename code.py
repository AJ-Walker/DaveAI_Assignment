import csv

# Converting the csv file to a list of dictionaries
def csv_into_dict(filename: str):
    with open(filename, 'r') as file:
        csvreader = csv.DictReader(file)
        data = [row for row in csvreader]

    return data

# Customer Data One in a list of dictionaries
customer_data_one = csv_into_dict('customer_data_one.csv')

# Customer Data Two in a list of dictionaries
customer_data_two = csv_into_dict('customer_data_two.csv')

customer_data = customer_data_one

for d1 in customer_data_two:
    for d2 in customer_data:
        if d1['mobile_number'] == d2['mobile_number']:

            # Getting the index d2 in the customer data list
            idx = customer_data.index(d2)

            # Deleting the old value from customer data list
            del customer_data[idx]
            break

    # Appending the values to customer data list
    customer_data.append(d1)

# Print the length of the customer data list
print(len(customer_data))

# for c in customer_data:
#     print(c['first_name'], c['last_name'], c['mobile_number'])

# Sorting the customer data list by first name
customer_data.sort(key=lambda x: x['first_name'])

# Printing the customer data list
for c in customer_data:
    print(c['first_name'], c['last_name'], c['mobile_number'])



        



