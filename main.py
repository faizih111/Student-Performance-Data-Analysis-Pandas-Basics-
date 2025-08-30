import pandas as pd

data = {"Math": 55, "Science": 70, "English": 80}
student = pd.Series(data)
print(student, "\n")

datas = {
    "Student01": {
        "Name:": "Faizan",
        "Age:": 17,
        "Math:": 45,
        "Science": 78,
        "English": 86,
    },
    "Student02": {
        "Name:": "Ali",
        "Age:": 18,
        "Math:": 70,
        "Science": 72,
        "English": 99,
    },
    "Student03": {
        "Name:": "Kazim",
        "Age:": 20,
        "Math:": 80,
        "Science": 50,
        "English": 56,
    },
}

data_store01 = pd.DataFrame(datas)
data_store01.to_csv("students.csv")

data_read01 = pd.read_csv("students.csv")
print(data_read01, "\n")

print(f"Display the first few rows: \n {data_read01.head(2)}\n")
print(f"Display summary statistics: \n {data_read01.describe()}\n")

data_store02 = pd.DataFrame(datas)
data_store02.to_json("students.json")

data_read02 = pd.read_json("students.json")
print(data_read02, "\n")

print(f"Display the first few rows: \n {data_read02.head(2)}\n")
print(f"Display summary statistics: \n {data_read02.describe()}\n")
