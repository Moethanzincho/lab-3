# CIS-117 Lab3
# This program reads a CSV file containing country data, groups the data by region, and writes each group to a separate CSV file named after the region.
# Anastasiia Golubtsova, Moe Cho
# Group 10

import csv

def read_file(file_name):
    with open(file_name) as file:
        reader = csv.reader(file)
        rows = [r for r in reader]

    return rows[0], rows[1:]

def write_file(header, rows, file_name):
    with open(file_name, "w") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(rows)

def main():
    header, rows = read_file("country_full.csv")
    name_index = header.index("name")
    region_index = header.index("region")
    if region_index == -1:
        print("The 'region' column was not found in the header.")
        return

    groups = {}
    for row in rows:
        region = row[region_index]
        region = region if region else "Unknown"
        if region not in groups:
            groups[region] = []
        groups[region].append(country)

    for region, group_rows in groups.items():
        output_file_name = f"{region}.csv"
        write_file(header, group_rows, output_file_name)
        print(f"Data for region '{region}' has been written to '{output_file_name}'.")

if __name__ == "__main__":
    try:
        main()
    except FileNotFoundError as e:
        print("The file 'country_full.csv' was not found.", e)
    except IOError as e:
        print("An I/O error occurred while reading or writing the file.", e)
