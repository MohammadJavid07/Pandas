import pandas as pd
#to read a CSV file into a DataFrame, we can use the pd.read_csv() function. For example, if we have a CSV file named "students.csv" with the following content:
pizza_data = pd.read_csv(r"D:\\Python Codes and Project\\Pandas Projects\\Pandas\\Enhanced_pizza_sell_data_2024-25.csv", encoding='cp1252')  # Replace with the actual path to your CSV file
print(pizza_data.head())  # This will display the first 5 rows of the DataFrame

#to change the column names to uppercase, we can use the str.upper() method. For example:
pizza_data.columns = pizza_data.columns.str.upper()
print(pizza_data.columns)  # This will display the updated column names

#Now to change the column names to uppercase, we can use the loop and the str.upper() method. For example:
for col in pizza_data.columns:
    pizza_data.rename(columns={col: col.upper()}, inplace=True)
print(pizza_data.columns)  # This will display the updated column names

#to combine two columns into a new column, we can use the + operator. For example, to combine the "RESTAURANT NAME" and "LOCATION" columns into a new column called "RESTAURANT LOCATION", we can do:
pizza_data['Delivery Time'] = pizza_data['DELIVERY TIME'] + '-' + pizza_data['ORDER MONTH']
print(pizza_data.head())  # This will display the first 5 rows of the DataFrame with the new column

#to make the column of DELAY (MIN) as DELAY (HOURS), we can divide the values in the "DELAY (MIN)" column by 60. For example:
pizza_data['DELAY (HOURS)'] = pizza_data['DELAY (MIN)']/60  # This will create a new column "DELAY (HOURS)" with the values in hours
pizza_data['DELAY (HOURS)'] = pizza_data['DELAY (HOURS)'].round(2)  # This will round the values in the "DELAY (HOURS)" column to 2 decimal places  
print(pizza_data.head())  # This will display the first 5 rows of the DataFrame with the new column

# to show the dataframe as a shape means to show the dimensions or number of rows and columns, we can use the shape attribute. For example:
print(pizza_data.shape)  # Output: (number of rows, number of columns)  

#to show the fist 5 rows of the DataFrame, we can use the head() method. For example:
print(pizza_data.head())  # This will display the first 5 rows of the Data

#to show the data of Delay (HOURS) column, we can use the following code:
print(pizza_data['DELAY (HOURS)'])  # This will display the values in the "DELAY (HOURS)" column of the DataFrame

#to categorize the data of Delay (HOURS) column into 3 categories, we can use the pd.cut() function. For example:
op_labels = ['On Time', 'Slightly Delayed', 'Highly Delayed']
category = [0, 0.3, 0.4, float('inf')]
pizza_data['Delay Category'] = pd.cut(pizza_data['DELAY (HOURS)'] , bins=category, labels=op_labels)
print(pizza_data.iloc[100:150])  # This will display rows 100 to 149 of the DataFrame with the new column

