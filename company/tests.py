
# Create your tests here.
def read_region_data():
	with open('china_city.csv', 'r') as file:
		reader = csv.DictReader(file, delimiter=',')

		for row in reader:
			large = row.get('large')
			middle = row.get('middle')
			small = row.get('small')
			print(large, middle, small)

read_region_data()