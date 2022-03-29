import time

arr = 0
def ded_inside():
	global arr 
	arr = 1000
	raa = 7
	for i in range(10000):
		rar = str(arr)
		rrr = str(raa)
		time.sleep(0)
		print(rar + " - " + rrr)
		arr = arr - raa		
		if arr < raa:
			return arr
def print_ded_inside():

	print(arr)

def main():
	print_ded_inside()
	ded_inside()
if __name__ == "__main__":	
	main()

	#while raa < arr: 
	#rar = str(arr)
	#rrr = str(raa)
	#print(rar + " - " + rrr)
	#arr = arr - raa
	#time.sleep(0)
	#if raa > arr:
	#	dedinside = str(arr)
	#	print(dedinside + " - " + rrr)
	
