import argparse
import requests

def main():
	Argumentos()
	BruteForce()

def Argumentos():
	global args
	parser = argparse.ArgumentParser()
	parser.add_argument("-s", dest="host", action="store", help="define o site que você ira usar!", required=False)
	parser.add_argument("-i", dest="first", action="store", help="define um ponto inicial ex: 1", required=False)
	parser.add_argument("-f", dest="end", action="store", help="define um ponto final ex: 999", required=False)
	parser.add_argument("-a", dest="filtrar", action="store", help="define o que quer filtrar!", required=False)
	parser.add_argument("-x", dest="hexa", action="store_true", help="define se quer transformar em hex!", required=False)
	args = parser.parse_args()

def BruteForce():
	for i in range(int(args.first),int(args.end)):
		if args.hexa == True:
			i = hex(i).split('x')[1]
		r = requests.get(args.host+str(i))
		read = (r.text)
		if str(args.filtrar) in str(read):
			print ("Filtrado: ",read)
			quit()
		else:
			print (read)
main()
