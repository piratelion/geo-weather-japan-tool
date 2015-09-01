# geo-weather-japan-tool
##switch from TokyoDatum to World Geodetic System(WGS 84)
In [1]: a = locSys(26.205367,127.676513,'TokyoDatum')
        print a-b
Out[1]: 0.4814924944754633
##calculate distantance
Example:
In [1]: a = locSys(26.205367,127.676513,'TokyoDatum')
        b = locSys(26.205367,127.676513,'WGS84')
        print self.lat_w, self.lon_w
 
 
##pandas function for calculate distance from TokyoDatum or World Geodetic System(WGS 84)
Example:
    here is a  pandas function for calculate distance:
    ( TokyoDatum )
    7	        8	        9	        10
    26.205367	127.676513	26.207467	127.676925
    26.207425	127.677063	26.205342	127.676663
    26.214200	127.682700	26.211875	127.680450
In [1]:  get_dist(df, col_list=[7, 8, 9, 10], geotype='TokyoDatum')
##download Japan's weather/holiday data
Please download jholiday here:    http://www.h3.dion.ne.jp/~sakatsu/index.htm
This code help you to download Japan's weather/holiday data.
pyquery, jholiday, datetime, numpy is needed.
Example:
In [1]: title = datetime.date(2013, 1, 1)
        sendai = sendaiWeather(title)
        dayT, dayP = dayType(title)

**************************************************************
### 日本測地系(lat_t, lon_t)を世界測地系(lat_w,lon_w)に変換
    lat_w = lat_t -lat_t*0.00010695 +lon_t*0.000017464 +0.0046017
    lon_w = lon_t -lat_t*0.000046038 -lon_t*0.000083043+0.010040
**************************************************************
