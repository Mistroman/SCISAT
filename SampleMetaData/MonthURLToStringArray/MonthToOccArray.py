import pandas as pd
# data = pd.read_csv('ftp://ftp.asc-csa.gc.ca/users/OpenData_DonneesOuvertes/pub/SCISAT/Data_format%20CSV/2005-02/sr7929/Data-L2_1km_grid/C2H2.csv')
from urllib.request import urlopen
page_source = urlopen('ftp://ftp.asc-csa.gc.ca/users/OpenData_DonneesOuvertes/pub/SCISAT/Data_format%20CSV/2006-10/').read().decode('utf_8')
print(page_source)
print(isinstance(page_source, String))
# print(data)