"""
task:
1. Read the data from the spreadsheet
2. Collect all of the sales from each month into a single list
3. output the total sales across all months

Extending features:
1. output a summary of the results to a spreadsheet
2. calculate:
    - monthly changes as a percentage
    - average
    - months with the highest and lowest sales
3. use data source from a different spreadsheet

"""

import csv
import matplotlib.pyplot as plt
import numpy as np


def display_all_sales(data) -> list:
    """
    Collect all of the sales from each month into a single list
    Args:
        data: List of dictionaries

    Returns:
    list of numbers representing all the sales
    """
    result = []
    for d in data:
        result.append(int(d["sales"]))
    print(f"All sales from each month: {result} \n")
    return result


def total_sales(all_sales) -> int:
    """
    output the total sales across all months
    Args:
        data: list of number representing all sales

    Returns:
        int
    """
    result = sum(all_sales)
    print(f"Total sales of year: {result}\n")
    return result


def highest_sales_month(data, all_sales):
    """
    output the month(s) with the highest sales value
    Args:
        all_sales:

    Returns:

    """
    max_sale = max(all_sales)
    index = [index for index, item in enumerate(all_sales) if item == max_sale]
    # print(index)
    result = []
    for i in index:
        result.append( data[i]["month"] )
    print(f"The month(s) with highest sales: {''.join(result)} \n")


def lowest_sales_month(data, all_sales):
    min_sale = min(all_sales)
    index = [index for index, item in enumerate(all_sales) if item == min_sale]
    result = []
    for i in index:
        result.append(data[i]["month"])
    print(f"The month(s) with lowest sales: {' '.join(result)} \n")


def average_sale(all_sales) -> float:
    avg = sum(all_sales)/len(all_sales)
    print(f"The average sales of year: {avg} \n")
    return avg


def monthly_changes(all_sales):
    changes = []
    month = {1: "JAN", 2: "FEB", 3: 'MAR',
             4: 'APR', 5: 'MAY', 6: 'JUN',
             7: 'JUL', 8: 'AUG', 9: 'SEP',
             10: 'OCT', 11: 'NOV', 12: 'DEC'}
    for i in range(0,len(all_sales)-1):
        change = round((all_sales[i+1] - all_sales[i])/all_sales[i] * 100, 2)
        # changes.append(change)
        print(f"The sales changes {change}% from {month[i+1]} to {month[i+2]}")


def line_chart(data):
    x_axis = []
    sales = []
    expenditure = []
    for d in data:
        x_axis.append(d["month"])
        sales.append(int(d["sales"]))
        expenditure.append(int(d["expenditure"]))

    # fig object is used to modify the figure,
    # ax object is subplot which is used to add texts to plot
    fig, ax = plt.subplots(figsize=(12,8))
    plt.plot(x_axis, sales, label = "Sales")
    plt.plot(x_axis, expenditure, label = "Expenditure")
    plt.title("Sales and Expenditure Change of 2018")
    plt.xlabel('Month')
    plt.ylabel("Value ($)")

    for index in range(len(x_axis)):
        ax.text(x_axis[index], sales[index], sales[index], size=9)

    plt.legend()
    plt.show()


def sales_vs_expenditure(data):
    # extract data into different list
    labels = []
    sales = []
    expenditure = []
    for d in data:
        labels.append(d["month"])
        sales.append(int(d["sales"]))
        expenditure.append(int(d["expenditure"]))
    width = 0.3

    # x-axis label
    plt.xticks(range(len(labels)), labels)

    plt.bar(np.arange(len(sales)), sales, width = width)
    plt.bar(np.arange(len(expenditure))+width, expenditure, width=width)
    plt.title("Sales vs Expenditure")
    plt.legend(["sales", "expenditure"], loc=2) # loc=2: quadrant 2
    plt.show()


if __name__ == "__main__":
    # task1: open the csv file and read data from spreadsheet
    data = []
    with open("sales.csv", "r") as sales_csv:
        spreadsheet = csv.DictReader(sales_csv)
        for row in spreadsheet:
            data.append(row)
            print(row)
    # print(data)
    # task 2
    all_sales_data = display_all_sales(data)
    # task 3
    total_sales(all_sales_data)

    # extend
    average_sale(all_sales_data)
    highest_sales_month(data, all_sales_data)
    lowest_sales_month(data, all_sales_data)
    monthly_changes(all_sales_data)
    # graph
    line_chart(data)
    sales_vs_expenditure(data)



