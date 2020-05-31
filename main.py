from flask import Flask, render_template
import csv
app = Flask(__name__)

# homepage route that sends DUI and all incidents arrays to frontend
@app.route('/')
def hello_world():
    substance_data = read_drunk_driver_data()
    all_data = read_all_data()
    return render_template('./index.html', substance_data=substance_data, all_data=all_data)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)

# function that reads csv file for DUI incidents and returns an array
def read_drunk_driver_data():
    coordsDict = {}

    with open('data.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        substance_arr = []
        for row in csv_reader:
            if (row["DRUNK_DR"] == "1" and row["YEAR"] == "2013" and row["latitude"] != row["longitud"] and len(row["latitude"]) >= 10 and len(row["longitud"]) >= 10):
                substance_arr.append([row["latitude"], row["longitud"]])
    return substance_arr

# function that reads csv file for all incidents and returns an array
def read_all_data():
    coordsDict = {}

    with open('data.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        all_incidents_arr = []
        for row in csv_reader:
            if (row["YEAR"] == "2013" and row["latitude"] != row["longitud"] and len(row["latitude"]) >= 10 and len(row["longitud"]) >= 10):
                all_incidents_arr.append([row["latitude"], row["longitud"]])
    return all_incidents_arr