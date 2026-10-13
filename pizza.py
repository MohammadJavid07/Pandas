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
