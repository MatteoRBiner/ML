import pandas as pd
import matplotlib.pyplot as plt


def read_dataset(path, sheet):
    return pd.read_excel(path, sheet_name=sheet, header=None)


def clean_data(data, rows, columns):
    data = data.drop(index=rows)
    data = data.drop(columns=columns, axis=1)
    return data


def get_ratio(total_data, target_data):
    return target_data.divide(total_data)


def plot_dataframe(df1, df1_label, df2, df2_label, df3, df3_label):
    plt.figure()
    plt.ylim(0, 0.5)
    plt.plot(df1, label=df1_label)
    plt.plot(df2, label=df2_label)
    plt.plot(df3, label=df3_label)
    plt.title("Female Workers")
    plt.ylabel("Female Percentage")
    plt.xlabel("Time")
    plt.legend()
    plt.show()


""" Does not help right now but might be useful at some point"""
def clean_plot_index(plot_length):
    current_value = 1991
    index = []
    for i in range(plot_length-3):
        index.append(current_value)
        if (i+3) % 4 == 0:
            current_value += 1
    return pd.DataFrame(index)


total_data = read_dataset("Total_workers.xlsx", "Full time - Total")
female_data = read_dataset("Total_workers.xlsx", "Full time - Women")
rows_to_delete = [0, 1, 2, 3, 4, 5, 6, 7, 9, 11, 31, 33, 72, 73, 74, 75, 76, 77]
columns_to_delete = range(3)
#plot_index = total_data.loc[5]
#plot_index = clean_plot_index(len(plot_index))
total_data = clean_data(total_data, rows_to_delete, columns_to_delete)
female_data = clean_data(female_data, rows_to_delete, columns_to_delete)
female_ratio = get_ratio(total_data, female_data)
total_plot = female_ratio.loc[8]
it_plot = female_ratio.loc[46]
science_plot = female_ratio.loc[55]
plot_dataframe(total_plot, "Total Female Workers", it_plot, "Female Workers in IT",
               science_plot, "Female Workers in Science")
