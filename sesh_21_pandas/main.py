# Consider the dataset of monthly sales data, with columns like
# Date, Product, Region, Sales, and Quantity.
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib

def exercise_01():
    #1 Use pandas to read the CSV file.
    sales_data = pd.read_csv("Sales_Data.csv")
    #2 Display the first five rows to understand the data structure.
    # print(sales_data.head())
    #3 Find the total sales amount for each product.
    total_sales_per_product = sales_data.groupby("Product")["Sales"].sum()
    print(total_sales_per_product)
    #4 Identify the product with the highest total sales
    top_rated_prod = total_sales_per_product.idxmax()
    print(top_rated_prod)

# Consider the dataset containing customer demographics with columns like
# CustomerID, Age, Gender, Annual Income, and Spending Score.
def exercise_02():
    #1 Use pandas to read the CSV file.
    demographic_data = pd.read_csv("Customer_Demographics_Data.csv")
    #2 Read the first 5 rows from the dataframe
    # print(demographic_data.head())
    #3 Calculate the average Annual Income grouped by Gender.
    avrg_annual_income = demographic_data.groupby("Gender")["Annual Income"].mean()
    # print(avrg_annual_income)
    #4 Create an age distribution histogram
    demographic_data["Age"].plot(kind="hist", title="Age Distribution")
    # plt.show()
    plt.savefig("Age Distribution.png")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    exercise_02()