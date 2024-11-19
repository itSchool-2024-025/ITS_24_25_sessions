import pandas as pd
import matplotlib.pyplot as plt

def exercise_01():
    #1
    sales_df = pd.read_csv("pandas data/Sales_Data.csv")
    #2
    print(sales_df.head())
    #3
    total_sales_per_product = sales_df.groupby("Product")["Sales"].sum()
    print(total_sales_per_product)
    #4
    avg_monthly_sales_per_region = sales_df.groupby("Region")["Sales"].mean()
    print(avg_monthly_sales_per_region)
    #5
    top_product = total_sales_per_product.idxmax()
    print("#5", top_product)
    top_product_data = sales_df[sales_df["Product"] == top_product]
    print(top_product_data)

def exercise_02():
    #1
    customer_df = pd.read_csv("pandas data/Customer_Demographics_Data.csv")
    #2
    avg_income_by_gender = customer_df.groupby("Gender")["Annual Income"].mean()
    print("#2 ", avg_income_by_gender)
    #3
    print("#3")
    customer_df["Age"].plot(kind="hist", title="Age Distribution")
    plt.savefig("age_distribution.png")
    #4
    highest_spending_young = customer_df[
        (customer_df["Age"] >= 20) & (customer_df["Age"] <= 30)
    ]["Spending Score"].max()
    print("#4 ", highest_spending_young)
    #5
    correlation = customer_df["Annual Income"].corr(customer_df["Spending Score"])
    print("#5 ", correlation)

def exercise_03():
    #1
    customer_df = pd.read_csv("pandas data/Customer_Demographics_Data.csv")
    # 2
    avg_income_by_gender = customer_df.groupby("Gender")["Age"].mean()
    print("#2 ", avg_income_by_gender)

def exercise_11():
    sensor_df = pd.read_csv("pandas data/Vehicle_Sensor_Data.csv")
    #1
    # v001_data  = pd.to_datetime(sensor_df["Timestamp"])
    # print(v001_data )
    groupby_veh_id = sensor_df.groupby("VehicleID").describe()
    print(groupby_veh_id)
    unique_values = sensor_df["VehicleID"].unique()
    print(unique_values)
    #2
    v002_data  = sensor_df[sensor_df["VehicleID"] == "V001"]
    # print("#2", v002_data)
    #3
    avg_speed_v001 = v002_data["Speed"].mean()
    avg_speed_rpm_v001 = v002_data[["Speed", "RPM"]].mean()
    # print(avg_speed_v001)
    # print(avg_speed_rpm_v001)
    #4
    v002_data.plot(x="Timestamp", y="EngineTemp", title="Engine Temperature Over Time")
    plt.show()

def exercise_12():
    dtc_df = pd.read_csv("pandas data/DTC_Data.csv")
    #1
    top_dtc_codes = dtc_df["DTC_Code"].value_counts().head(5)
    # print(top_dtc_codes)
    #2
    high_severity_dtc = dtc_df[dtc_df["Severity"] == "High"].groupby("VehicleID")["DTC_Code"].count()
    # print(high_severity_dtc)
    #3
    dtc_df["Timestamp"] = pd.to_datetime(dtc_df["Timestamp"])
    print(dtc_df)
    avg_time_between_dtc = dtc_df.groupby(["VehicleID", "DTC_Code"])["Timestamp"].diff().mean()
    print(avg_time_between_dtc)


if __name__ == "__main__":
    exercise_12()