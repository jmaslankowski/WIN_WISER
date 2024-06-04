# 1st
pip install pymongo

#!/usr/bin/env python
# coding: utf-8
import sys
import json
import requests
import re
import os

elasticsearch_url = ""

def get_result(query):
    payload={}
    headers = {}
    response = requests.request("GET", elasticsearch_url + query, headers=headers, data=payload)    
    return response.text


query = "/_cat/indices?v"
index1 = "*_606855" #we use the acquisition ID to get the list of related index
index2= "*_606855"
query1 = "/_cat/indices/{}?v=true&s=index".format(index1)

print(get_result(query1))


query_content_doc = "/content_/_search?pretty=true"
print(get_result(query_content_doc)[:1980])



#query_metrics_doc = "/metrics_/_search?pretty=true"
query_content_doc = "/content_/_search?pretty=true"
#print(get_result(query_content_doc)[:198000])


import WPCStarterKit as wp2

import pandas as pd
import json

smp=wp2.SocialMediaPresence()
res = json.loads(get_result(query_content_doc))
#print(res['took'])
#print("The converted dictionary : " + str(res)[:200])
for i in range(0,50):
    try:        
        url=res['hits']['hits'][i]['_source']['fetched_url']
        htmlfile=res['hits']['hits'][i]['_source']['html']        
        print(i,url)
        print("*"*100)
        smp.searchSocialMediaLinks(url,htmlfile)
        print("*"*100)
    except:
        break



