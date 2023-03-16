import random
x=0
while x<1:
	first_names = ["Albert", "Charles", "Nicolas", "Michael", "Anders", "Isaac", "Stephen", "Marie", "Richard"]
	last_names = ["Einstein", "Darwin", "Copernicus", "Faraday", "Celsius", "Newton", "Hawking", "Curie","Dawkins"]
	new_name = random.choice(first_names)+" "+ random.choice(last_names)
	print(new_name)
	new_names = []
	new_names.append(new_name)
	if new_name == "Albert Einstein":
		break		

