# 1#
#
# import pandas as pd
#
# file_path = 'titanic'
# titanic_data = pd.read_csv(file_path)
#
# survived_data = titanic_data[titanic_data['Survived'] == 1]
#
# survived_file_path = 'survived.csv'
# survived_data.to_csv(survived_file_path, index=False)
#
# survived_file_path

#2
#
# import pandas as pd
#
# file_path = 'organisations-100.csv'
# data = pd.read_csv(file_path)
#
# sorted_data = data.sort_values(by='Number of employees', ascending=True)
#
# sorted_data.to_csv('sorted_csv.csv', index=False)
#
# print(sorted_data.head())

#3
import pandas as pd


def filter_ssl_companies(input_file, output_file):
    data = pd.read_csv(input_file)

    ssl_companies = data[data["Website"].str.startswith("https://")]

    ssl_companies_filtered = ssl_companies[
        ["Organization Id", "Name", "Website", "Industry", "Number of employees"]
    ]

    ssl_companies_filtered.to_csv(output_file, index=False)
    print(f"SSL Companies successfully saved in {output_file}")

input_file = "organisations-100.csv"
output_file = "ssl_companies.csv"

filter_ssl_companies(input_file, output_file)
