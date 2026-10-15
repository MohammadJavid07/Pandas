import pandas as pd

pizza_data = pd.Series(["Margherita", "Pepperoni", "Hawaiian", "Veggie", "BBQ Chicken   Pizza"])
print(pizza_data)

print(pizza_data.index)

print(pizza_data.values)

#To give names to indexes, we can use the index parameter of the Series constructor. For example, we can create a Series with custom index names like this:
pizza_data_with_index = pd.Series(["Margherita", "Pepperoni", "Hawaiian", "Veggie", "BBQ Chicken Pizza"], index=["A", "B", "C", "D", "E"])
print(pizza_data_with_index)

#to access the elements of the Series using the custom index names, we can use the .loc[] accessor. For example, to access the element with index "C", we can do:
print(pizza_data_with_index.loc["C"])  # Output: Hawaiian

#to access the elements with the first character of name
print(pizza_data[pizza_data.str.startswith("M")])

#to make my pizza_data Series just like a dictionary, we can use the to_dict() method. For example:
pizza_dict = pizza_data.to_dict()
print(pizza_dict)

# how to create a DataFrame in the form of a dictionary, we can use the pd.DataFrame() constructor. For example, we can create a DataFrame with pizza names and their prices like this:
df = pd.DataFrame({"Pizza Name": ["Margherita", "Pepperoni", "Hawaiian", "Veggie", "BBQ Chicken Pizza"], 
                   "Price": [8.99, 9.99, 10.99, 7.99, 11.99],
                   "Size": ["Small", "Medium", "Large", "Medium", "Large"],
                   "colors": ["Red", "Red", "Yellow", "Green", "Brown"]})
print(df.head())  # This will display the first 5 rows of the DataFrame
#to show the last 5 rows of the DataFrame, we can use the tail() method. For example:
print(df.tail())  # This will display the last 5 rows of the DataFrame

#to access the elements of the DataFrame using the column names, we can use the .loc[] accessor. For example, to access the "Pizza Name" column, we can do:
print(df.loc[:, "Pizza Name"])  # Output: Series with pizza names

#or we can use the column name directly to access the column. For example:
print(df["Price"])  # Output: Series with pizza names

#to show columns of the DataFrame, we can use the columns attribute. For example:
print(df.columns)  # Output: Index(['Pizza Name', 'Price', 'Size',

#to name indexes of the DataFrame with the first two letters of the country names, we can use the index parameter of the DataFrame constructor. For example:
student_data = pd.DataFrame({"Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
                             "Age": [20, 21, 22, 23, 24],
                             "Country": ["USA", "Canada", "UK", "Australia", "Germany"],
                                "GPA": [3.5, 3.7, 3.8, 3.9, 4.0]},
                            index=["US", "CA", "UK", "AU", "DE"])
print(student_data)

#to name indexes of the DataFrame
student_data.index.name = "Country Code"
print(student_data)

#to read a CSV file into a DataFrame, we can use the pd.read_csv() function. For example, if we have a CSV file named "students.csv" with the following content:
pizza_df = pd.read_csv(r"D:\\Python Codes and Project\\Pandas Projects\\Pandas\\Enhanced_pizza_sell_data_2024-25.csv", encoding='cp1252')  # Replace with the actual path to your CSV file 
print(pizza_df.head())  # This will display the first 5 rows of the DataFrame

#to print our current working directory, we can use the os module. For example:
import os   
print(os.getcwd())  # This will display the current working directory

#to show dataFrame as  a shape means to show the dimensions or number of rows and columns, we can use the shape attribute. For example:
print(pizza_df.shape)  # Output: (number of rows, number of columns)

#to show the last 5 rows of the DataFrame, we can use the tail() method. For example:
print(pizza_df.tail())  # This will display the last 5 rows of the DataFrame    

#to show information about the DataFrame, we can use the info() method. For example:
print(pizza_df.info())  # This will display information about the DataFrame, including the

#to print the data of required columns using usecols parameter of the read_csv() function, we can do:
pizza_df_selected_columns = pd.read_csv(r"D:\\Python Codes and Project\\Pandas Projects\\Pandas\\Enhanced_pizza_sell_data_2024-25.csv", usecols=["Restaurant Name", "Location", "Distance (km)"], encoding='cp1252')  # Replace with the actual path to your CSV file
print(pizza_df_selected_columns)  # This will display the selected columns of the DataFrame

#to change the column names to uppercase, we can use the str.upper() method. For example:
pizza_df.columns = pizza_df.columns.str.upper()
print(pizza_df.head())  # This will display the first 5 rows of the DataFrame

#to select specific columns from the DataFrame, we can use the double square brackets. For example, to select the "RESTAURANT NAME" and "LOCATION" columns, we can do:
selected_columns_df = pizza_df[["RESTAURANT NAME", "LOCATION"]]
print(selected_columns_df)  # This will display the selected columns of the DataFrame

#to filter the DataFrame based on rows and columns numbers, we can use the iloc[] accessor. For example, to select the first 5 rows and the first 2 columns, we can do:
filtered_df = pizza_df.iloc[:3, :1]  # This will select the first 3 rows and the first column of the DataFrame
print(filtered_df)  # This will display the filtered DataFrame

"""#to add a new column to the DataFrame, we can simply assign a new Series or list to a new column name. For example, to add a new column called "RATING" with some sample ratings, we can do:
pizza_df["RATING"] = [4.5, 4.0, 3.5]  # Sample ratings for each restaurant
print(pizza_df.head())"""  # This will display the first 5 rows of the Data

"""#to drop a column from the DataFrame, we can use the drop() method. For example, to drop the "RATING" column, we can do:
pizza_df = pizza_df.drop(columns=["Is Delayed"])  # This will drop the "RATING" column from the DataFrame
print(pizza_df.head())  # This will display the first 5 rows of the DataFrame"""

#to concatenate two columns into a new column, we can use the + operator. For example, to concatenate the "RESTAURANT NAME" and "LOCATION" columns into a new column called "RESTAURANT LOCATION", we can do:
pizza_df["RESTAURANT LOCATION"] = pizza_df["RESTAURANT NAME"] + " - " + pizza_df["LOCATION"]
print(pizza_df.head())  # This will display the first 5 rows of the Data

#to show the length of the DataFrame, we can use the len() function. For example:
print(len(pizza_df))  # This will display the number of rows in the DataFrame   

#to rename the columns of the DataFrame, we can use the rename() method. For example, to rename the "RESTAURANT NAME" column to "NAME" and the "LOCATION" column to "CITY", we can do:
pizza_df = pizza_df.rename(columns={ "LOCATION": "CITY"})
print(pizza_df.head())  # This will display the first 5 rows of the Data

#filtering the pizza_df for duplicate CITY
duplicate_pizza_city = pizza_df[pizza_df.duplicated(subset=["CITY"])]
print(duplicate_pizza_city["CITY"].value_counts())