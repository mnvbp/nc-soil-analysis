"""scrapes data from NC Agriculture Portal for Agronomic Laboratory Services website"""

import csv
from time import sleep
from request import conn, payload, headers

csv_file = '/Users/manavparikh/Desktop/output/test.csv'
output = '/Users/manavparikh/Desktop/output/test2.csv'

#named constants
CRITERIA = "REPORT#"
#start and end value for scraping
START = 1410058
END = 1439480


def main():
    iterative(START, END)
    csv_cleaner(csv_file, output)

#GETTING DATA AND DECODING (FROM cURL to PYTHON WEBSITE)
def get_data(parameter: int):
    conn.request("POST", f"/agronomi/PALS/Reports/downloadSoilReport.aspx?Param={parameter}%24%24SL000917%24%244", payload,headers)
    res = conn.getresponse()
    data = res.read()
    decoded_data = data.decode('utf8')
    print(decoded_data)
    return (decoded_data)

#iteratively counts through the start and end intergers and calls get_data
#afterwards, writes data to disk
def iterative(start: int, end: int):
    while start < end:
        data = get_data(start)
        cr = csv.reader(data.splitlines(), delimiter=',')
        my_list = list(cr)
        #Writing DATA to CSV from Request
        with open(csv_file, "a", newline="") as file:
            writer = csv.writer(file)
            # Write each row to the CSV file
            for row in my_list:
                writer.writerow(row)
        start += 1
        sleep(.00001)

#csv_cleaner cleans up the csv from artifacts (multiple headers) after the data is fetched from the website
def csv_cleaner(input, output, criteria, row_index=0):
    with open(input, "r") as infile, open(output, "w") as outfile:
        reader = csv.reader(infile)
        header = next(reader, None)  # skip the headers
        writer = csv.writer(outfile)
        counter = 0
    for row in reader:
        if counter == 0:
            writer.writerow(header)
            counter += 1
        if row[row_index] == criteria:
            next(reader, None)
        else:
             writer.writerow(row)


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()