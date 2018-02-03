netteBad = pd.read_csv('../../data/raw/nettebad_train_set.csv', sep=';')
weather_dwd = pd.read_csv('../../data/raw/weather_dwd_train_set.csv', sep=';')
weather_osnabrueck = pd.read_csv('../../data/raw/weather_uni_osnabrueck_train_set.csv', sep=';')


#Changement type date
from datetime import datetime
netteBad.date = pd.to_datetime(netteBad.date, format='%m/%d/%Y')
weather_dwd.date = pd.to_datetime(weather_dwd.date, format='%m/%d/%Y')
weather_osnabrueck.date = pd.to_datetime(weather_osnabrueck.date, format='%d/%m/%Y')


print(type(netteBad.sportbad_closed[0]))