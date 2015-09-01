# -*- coding: utf-8 -*-
"""
=============================================================
Created on Mar 15 2015
@author: c
--------------------------------------------------------------
The first pre-job you should make sure that you have the loc in
World Geodetic System(Version: WGS 84 (aka WGS 1984, EPSG:4326)).
**************************************************************
# 日本測地系(lat_t, lon_t)を世界測地系(lat_w,lon_w)に変換
    lat_w = lat_t -lat_t*0.00010695 +lon_t*0.000017464 +0.0046017
    lon_w = lon_t -lat_t*0.000046038 -lon_t*0.000083043+0.010040
**************************************************************
**************************************************************
=============================================================
"""
import numpy as np


def get_dist(df, col_list=[7, 8, 9, 10], geotype='WGS84'):
    """
    here is a  pandas function for calculate distance:
    ( TokyoDatum )
    7	        8	        9	        10
    26.205367	127.676513	26.207467	127.676925
    26.207425	127.677063	26.205342	127.676663
    26.214200	127.682700	26.211875	127.680450
    """
    if geotype == 'TokyoDatum':
        dk = df[col_list]
        dk.rename(columns=dict(zip(col_list, [
            "lat1",
            "lon1",
            "lat2",
            "lon2",
            ])), inplace=True)
        dk.loc[:, 'lat_w1'] = dk.lat1 - dk.lat1 * 0.00010695\
            + dk.lon1 * 0.000017464 + 0.0046017
        dk.loc[:, 'lon_w1'] = dk.lon1 - dk.lat1 * 0.000046038\
            - dk.lon1 * 0.000083043 + 0.010040
        dk.loc[:, 'lat_w2'] = dk.lat2 - dk.lat2 * 0.00010695\
            + dk.lon2 * 0.000017464 + 0.0046017
        dk.loc[:, 'lon_w2'] = dk.lon2 - dk.lat2 * 0.000046038\
            - dk.lon2 * 0.000083043 + 0.010040
    if geotype == 'WGS84':
        dk = df[col_list]
        dk.rename(columns=dict(zip(col_list, [
            "lat_w1",
            "lon_w1",
            "lat_w2",
            "lon_w2",
            ])), inplace=True)
    dr = np.radians(dk[["lat_w1", "lon_w1", "lat_w2", "lon_w2"]])
    lat = dr.lat_w2-dr.lat_w1
    lon = dr.lon_w2-dr.lon_w1
    sinline = np.sqrt(
        np.sin((lat) / 2) ** 2 +
        np.cos(dr.lat_w1) *
        np.cos(dr.lat_w2) *
        np.sin((lon) / 2) ** 2
        )
    return 2 * 6371 * np.arcsin(sinline)
