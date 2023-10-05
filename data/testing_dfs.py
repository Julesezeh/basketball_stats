import pandas as pd

df = pd.DataFrame(
    {
        "Name": [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss. Elizabeth",
        ],
        "Age": [22, 35, 58],
        "Sex": ["male", "male", "female"],
    }
)

df2 = pd.DataFrame(
    {
        "Name": ["Jamel Temetrius Morant", "Jaren Jackson Jr.", "Jeffrey Williams"],
        "Age": [24, 25, 30],
        "Occupation": ["Hooper", "Hooper", "Rapper"],
    }
)

series1 = pd.Series([12, 34, 56], name="Age")

# print("works")

# print(df["Age"].describe())

print(df2.describe())
# still taking course on ds
