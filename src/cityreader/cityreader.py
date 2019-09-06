import csv

class City:
    def __init__(self, name, lat, lon):
      self.name = name
      self.lat = lat
      self.lon = lon

    def __str__(self):
        return f"{self.name}, {self.lat}, {self.lon}"

cities = []

def cityreader(cities=[]):
  with open('cities.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
     cities.append(City(row['city'], float(row['lat']), float(row['lng'])))

    return cities

cityreader(cities)
# Print the list of cities (name, lat, lon), 1 record per line.
for c in cities:
    print(c)



def cityreader_stretch(lat1, lon1, lat2, lon2, cities=[]):
  # within will hold the cities that fall within the specified region


  if lat2 < lat1:
    lat1, lat2 = lat2, lat1

  if lon2 < lon1:
    lon1, lon2 = lon2, lon1

  within = [c for c in cities if c.lon >= lon1 and c.lon <= lon2 and c.lat >= lat1 and c.lat <= lat2]

  return within
              #lat      #lon
#Albuquerque: (35.1055,-106.6476)

lat1 = float(input("latitude 1: "))
lat2 = float(input("latitude 2: "))
lon1 = float(input("longitude 1: "))
lon2 = float(input("longitude 2: "))

print(cityreader_stretch(lat1, lon1, lat2, lon2, cities))



