# -*- coding: utf-8 -*-
"""
=============================================================
Created on Mar 15 2015
@author: c
--------------------------------------------------------------
The first pre-job you should make sure that you have the loc in
World Geodetic System(Version: WGS 84 (aka WGS 1984, EPSG:4326)).
or TokyoDatum(日本測地系)
**************************************************************
# 日本測地系(lat_t, lon_t)を世界測地系(lat_w,lon_w)に変換
    lat_w = lat_t -lat_t*0.00010695 +lon_t*0.000017464 +0.0046017
    lon_w = lon_t -lat_t*0.000046038 -lon_t*0.000083043+0.010040
**************************************************************
**************************************************************
Now suppose you have done that, we intro some choices here.
[1] Haversine formula: commonly used (error < 0,5%)
[2] what...
**************************************************************
Example:
In [1]: a = locSys(26.205367,127.676513,'TokyoDatum')
        b = locSys(26.205367,127.676513,'WGS84')
        print a-b
Out[1]: 0.4814924944754633
( measured by km )
You can see the huge difference between WGS and TokyoDatum.
=============================================================
"""
import math  # radians, cos, sin, asin, sqrt
df

class locSys:
    """
    This have only two type now 'WGS84', 'TokyoDatum'
    a = locSys(26.205367,127.676513,'WGS84')
    """
    def __init__(self, lat0, lon0, type0):
        """
        This have only two type now 'WGS84', 'TokyoDatum'
        a = locSys(26.205367,127.676513,'TokyoDatum')
        """
        assert type(lat0) == float
        assert type(lon0) == float
        assert type(type0) == str
        assert type0 in [
            'WGS84',
            'TokyoDatum',
            ]
        self.geotype = type0
        if self.geotype == 'TokyoDatum':
            self.lat_t = lat0
            self.lon_t = lon0
            # print "now change it to WGS84..."
            self.lat_w = self.lat_t - self.lat_t * 0.00010695\
                + self.lon_t * 0.000017464 + 0.0046017
            self.lon_w = self.lon_t - self.lat_t * 0.000046038\
                - self.lon_t * 0.000083043 + 0.010040
        if self.geotype == 'WGS84':
            self.lat_w = lat0
            self.lon_w = lon0

    def getLoc(self):
        print self.lat_w, self.lon_w, 'WGS84'

    def __str__(self):
        return "%s: lat %s; lon %s" % (self.geotype, self.lat_w, self.lon_w)

    def __sub__(self, other):
        """
        This have calculate distance of 'WGS84' by Haversine method.
        Result is measured by km
        """
        lat1, lng1, lat2, lng2 = list(map(math.radians, [
            self.lat_w,
            self.lon_w,
            other.lat_w,
            other.lon_w,
            ]
            ))
        lat = lat2 - lat1
        lng = lng2 - lng1
        a = math.sin(lat / 2) ** 2 +\
            math.cos(lat1) * math.cos(lat2) * math.sin(lng / 2) ** 2
        b = 2 * 6371 * math.asin(math.sqrt(a))  # 6371 is radius of Earth
        return b
