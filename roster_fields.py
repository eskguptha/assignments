import re

def valiate_email(email):
	match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)
	return match

def do_process(**kwargs):
	webadvisor_lines = []
	try:
		with open(kwargs['input_file']) as f:
			webadvisor_lines = f.readlines()
	except IOError as e:
		print (e)
		pass
	webadvisor_result_data = []
	user_data = []
	for line in webadvisor_lines:
		try:
			if line == '\n':
				if user_data:
					del user_data[-1]
					webadvisor_result_data.append(user_data)
				user_data = []
			else:
				if valiate_email(line) == None:
					user_data.append(line.strip())
		except AttributeError as e:
			print (e)
			pass
	if webadvisor_result_data:
		with open(kwargs['output_file'], 'w') as f:
			f.writelines("%s\n" % ",".join(l) for l in webadvisor_result_data)
	pass


if __name__ == "__main__":
	input_file = "cs176roster.webadvisor.txt"
	output_file = "output_cs176roster.webadvisor.txt"	
	do_process(input_file=input_file, output_file=output_file)