import pandas as pd
from urllib.request import urlopen
import json
import io
import requests

import csv
from collections import defaultdict

def checkArcticCircle():
	validity = true
	return (validity)

def runForSunData(main_url, time_frame, sundata):
	data = {}
	page_source = urlopen(main_url + '/' + time_frame + '/' + sundata + '/' + sundata + '_InfoMetadata%20.txt').read().decode('utf_8')
	lines = page_source.splitlines()
	
	#validity = checkForArctic(page_source)

	for word in lines:
		if(word.startswith("occultation_name =")):
			occultation_name = word[19:]
			# print(word[19:])
		if(word.startswith("event_type =")):
			event_type = word[13:]
			# print(word[13:])
		if(word.startswith("date =")):
			date = word[7:]			
			# print(word[7:])
		if(word.startswith("date_MJD2000 =")):
			date_MJD2000 = word[15:]
			# print(word[15:])
		if(word.startswith("latitude =")):
			latitude = word[11:]
			# print(word[11:])
		if(word.startswith("longitude =")):
			longitude = word[12:]
			# print(word[12:])
		if(word.startswith("beta_angle =")):
			beta_angle = word[13:]
			# print(word[13:])
		if(word.startswith("start_timetag =")):
			start_timetag = word[16:]
			# print(word[16:])
		if(word.startswith("end_timetag =")):
			end_timetag = word[14:]
			# print(word[14:])
		if(word.startswith("start_time =")):
			start_time = word[13:]
			# print(word[13:])
		if(word.startswith("end_time =")):
			end_time = word[11:]
	# occultation_name, event_type, date, date_MJD2000, latitude, longitude, beta_angle, start_timetag, end_timetag, start_time, end_time = getMetaData(lines)
	molecule_range = "5-95"
	molecule_name = "O3"
	molecule_csv = pd.read_csv(main_url + '/' + time_frame + '/' + sundata + '/' + '/Data-L2_retreival_grid/' + 'O3.csv',  header=None)
	z_csv = pd.read_csv(main_url + '/' + time_frame + '/' + sundata + '/' + '/Data-L2_retreival_grid/' + 'z.csv',  header=None)

	# Export = molecule_csv.to_json()

	# with open('data1.txt', 'w') as outfile:
	# 	json.dump(Export, outfile)
	df_new = pd.concat([molecule_csv, z_csv], axis =1)
	# df_new1 = df_new.iloc[1:, 1:]
	# df_new1 = df_new.iloc[0, 0]
	df_new.to_csv("df_new.csv")
	molecule_csv.to_csv("molecule_csv.csv")
	z_csv.to_csv("z_csv.csv")

	# with open('temp.json', 'w') as f:
	# 	f.write(molecule_csv.to_json(orient='records', lines=True))

	data[sundata] = []
	data[sundata].append({
		'occultation_name' : occultation_name,
		'event_type' : event_type,
		'date' : date,
		'date_MJD2000' : date_MJD2000,
		'latitude' : latitude,
		'longitude' : longitude,
		'beta_angle ' : beta_angle,
		'start_timetag' : start_timetag,
		'end_timetag' : end_timetag,
		'start_time' : start_time,
		'end_time' : end_time,
		'molecule_range' : molecule_range,
		'molecule_name' : molecule_name,
		# 'lol' : dictionaryToDump
		# 'molecule_csv' : molecule_csv,
		# 'z_csv' : z_csv
	})

	with open('data.txt', 'w') as outfile:
		json.dump(data, outfile)

	# data = urlopen('ftp://ftp.asc-csa.gc.ca/users/OpenData_DonneesOuvertes/pub/SCISAT/Data_format%20CSV/2005-02/sr7929/Data-L2_1km_grid/C2H2.csv').read().decode('utf_8')
	# print(data)
	# f = open('htmlcode.txt','w')
	# f.write(page_source)
	# f.close()

def main():
	main_url = 'ftp://ftp.asc-csa.gc.ca/users/OpenData_DonneesOuvertes/pub/SCISAT/Data_format%20CSV'
	runForSunData(main_url, '2004-04', 'sr3725')

if __name__ == "__main__":
	main()