def do_process(**kwargs):
	roster_lines = []
	try:
		with open(kwargs['input_file']) as f:
			roster_lines = f.readlines()
	except IOError as e:
		print (e)
		pass

	roster_data = []
	for line in roster_lines:
		try:
			res_map_chages = lambda i: [i[1].strip(),i[0].strip(),i[2].strip()]
			user_data = res_map_chages(line.split(','))
			if user_data:
				roster_data.append(user_data)
		except AttributeError as e:
			print (e)
			pass
	if roster_data:
		with open(kwargs['output_file'], 'w') as f:
			f.writelines("%s\n" % ",".join(l) for l in roster_data)
	pass


if __name__ == "__main__":	
	input_file = "cs371598roster.txt"
	output_file = "output_cs371598roster.txt"	
	do_process(input_file=input_file, output_file=output_file)