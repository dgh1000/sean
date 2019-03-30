import csv

with open('testcsv.csv', newline='') as csvfile:
  spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
  for row in spamreader:
    print(', '.join(row))


#import mysql.connector

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="",
#   passwd=""
# )
#
# print(mydb)

d = { "foo": 356.7,
     "bar": "malarky"
     36 : 25 ,
     bar: 25.0 }

js = { foo: 356.7,
      bar: "malarky"};

jsl = [ 3, 6, {food: "avacado", meat: 3560.0}]

# change to this
t = { "id": 3,
     "lat": 3,
     "lon": -118,
     "date": 3}

# datetime class: search for Python date time.
#  take in the csv string: "3/26/19 10:03:01" --> datetime()
#
#
# represent as seconds past an epoch. 1900. seconds past 1900.

sampleCsv = ["3", "3", "-118", "3/26/19"]
t = { "id": int(sampleCsv[0]),
     "lat": float(sampleCsv[1]),
     "lon": float(sampleCsv[2]),
     "date", datetime }
