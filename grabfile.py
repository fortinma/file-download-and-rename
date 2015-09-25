import urllib2
import urllib
import datetime

#url = 'http://opendata.toronto.ca/gcc/address_points_wgs84.zip'
url = 'http://maps.library.utoronto.ca/dvhmp/data/2009_05_10/industry/animalprocessing_1892.zip'

#urllib.urlretrieve(url, "address_points.zip")
 #   return datetime.datetime.now().strftime(fmt).format(fname=fname)
#datestamp = datetime.now().strftime('%Y%m%d').format(fname=fname)

now = datetime.datetime.now()
day =  now.day
month = now.month
year = now.year
#print year 
#print month 
#print day
#for dates, this is helpful http://www.saltycrane.com/blog/2008/06/how-to-get-current-date-and-time-in/
urllib.urlretrieve(url, "dvhmp" + str(year) + "-" + str(month) + "-" + str(day) + ".zip")
