import json
import math

def cartesian_plane(origin):
	with open('./coordinates.json') as data_file:    
		coordinates_data = json.load(data_file)

	index_distances = []
	
	for index in coordinates_data:
		d = index['value'].split(',')
		dest = (int(d[0]), int(d[1]))
		distance = get_distance(origin, dest)
		index.update({'distance':distance})
		index_distances.append(index)
	
	return index_distances
	
def display_indexes(index_distances):
	for index in sorted(index_distances, key=lambda k: k['distance']):
		print("id : %s, coordinates value : (%s), distance from origin : %s" % (index['id'], index['value'], index['distance']))

def get_distance(origin, dest):
	return math.sqrt((origin[0] - dest[0]) * (origin[0] - dest[0]) + (dest[1] - origin[1]) * (dest[1] - origin[1]))	

if __name__ == "__main__":
	x = int(input("Enter origin coordinates x: "))
	y = int(input("y: "))

	display_indexes(cartesian_plane((x,y)))
