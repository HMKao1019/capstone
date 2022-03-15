# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 11:39:19 2022

@author: hmkao

#--Ref: https://ci.taiwan.gov.tw/dsp/ (民生公共物聯網資料服務平台)
        
"""

import requests
import emoji

headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
          }


#-- 感測資料-水利署_淹水感測器
url= 'https://sta.ci.taiwan.gov.tw/STA_WaterResource_v2/v1.0/Datastreams?$expand=Thing,Thing/Locations,Observations($orderby=phenomenonTime%20desc;$top=1)%20&$filter=Thing/properties/authority_type%20eq%20%27%E6%B0%B4%E5%88%A9%E7%BD%B2%27%20%20and%20substringof(%27Datastream_Category_type=%E6%B7%B9%E6%B0%B4%E6%84%9F%E6%B8%AC%E5%99%A8%27,Datastreams/description)%20and%20substringof(%27Datastream_Category=%E6%B7%B9%E6%B0%B4%E6%B7%B1%E5%BA%A6%27,Datastreams/description)%20&$count=true'


r= requests.get(url, headers= headers, verify= False)
data= r.json()
value= data['value']

for i in range(len(value)):
    
    properties= value[i]['Thing']['properties']
    authority= properties['authority']
    stationName= properties['stationName']
    
    #-- 目標觀測站
    if stationName == '田中八堡圳淹水監控站':
        
        Locations= value[i]['Thing']['Locations']
        lon= Locations[0]['location']['coordinates'][0]
        lat= Locations[0]['location']['coordinates'][1]
            
        Observations= value[i]['Observations']
            
        phenomenonTime= Observations[0]['phenomenonTime']
        phenomenonTime= phenomenonTime[0:10] + ' ' + phenomenonTime[11:16]
            
        waterDepth= Observations[0]['result']  #-- unit: cm
        if float(waterDepth) < 0: waterDepth= 0.0
        waterDepth= round(float(waterDepth), 1)
    
        msg =  ':ocean:' + authority + '\n' 
        msg += stationName + '的觀測水深為{:.1f}公分'.format( float(waterDepth) ) + '\n'
        msg += ':watch:' + '觀測時間: ' +  phenomenonTime
        msg= emoji.emojize(msg, use_aliases=True)        

        print(msg)
    