import pandas as pd


def read_dataset(path, sheet, rows_to_delete, columns_to_delete):
    intermediate_path = "./data/intermediate.xlsx"
    file = pd.ExcelFile(path)
    intermediate_file = pd.read_excel(file, sheet_name=sheet, header=None)
    clean_file = clean_data(intermediate_file, rows_to_delete, columns_to_delete)
    clean_file.to_excel(intermediate_path)
    return pd.read_excel(intermediate_path, header=None, index_col=1)


def clean_data(data, rows, columns):
    data = data.drop(index=rows)
    data = data.drop(columns=columns, axis=1)
    return data


def write_to_excel(dataframe):
    dataframe.to_excel("./data/relative_wages_communes.xlsx")


def get_ratio(female_data, male_data):
    return female_data / male_data


def transform_data(rows_to_delete, columns_to_delete, path, sheet, index_f, index_m):
    data_commune = read_dataset(path, sheet, rows_to_delete, columns_to_delete)
    ratio = get_ratio(data_commune[index_f].astype(float), data_commune[index_m].astype(float))
    return ratio


rows_to_delete = range(6)
columns_to_delete = [1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
path_2012 = "./data/base-2012.xls"
paths = ["./data/base-2013.xls", "./data/base-2014.xls", "./data/base-2015-geo-2019.xls", "./data/base-2016.xlsx",
         "./data/base-2017.xlsx", "./data/base-2018.xlsx", "./data/base-2019.xlsx", "./data/base-2020.xlsx",
         "./data/base-2021.xlsx"]
sheet = "COM"
index_f = 2
index_m = 3
data_by_year = transform_data(rows_to_delete, columns_to_delete, path_2012, sheet, index_f, index_m)
for path in paths:
    new_data = transform_data(rows_to_delete, columns_to_delete, path, sheet, index_f, index_m)
    data_by_year = pd.concat([data_by_year, new_data], axis=1)


data_by_year = data_by_year.dropna(how="any")
data_by_year = clean_data(data_by_year, [0], [])
write_to_excel(data_by_year)
