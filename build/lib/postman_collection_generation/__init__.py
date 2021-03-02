__version__ = "1.0.0"
import uuid,json
from datetime import datetime
from flask import jsonify
from urllib.parse import urlparse

def generate_collection(app,type='api',name='testname',url_domain='localhost',port=5000,output_path = '.'):
    collection_name = name + ' ' +datetime.now().strftime("%Y_%m_%d")

    collection_json = {}
    collection_json['info'] = {}
    collection_json['info']['_postman_id'] = str(uuid.uuid4())
    collection_json['info']['name'] = f'{collection_name}_{type}'
    collection_json['info']['schema'] = "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
    collection_json['item'] = []
    


    for r in app.url_map._rules:
        
        if r.endpoint == 'static':
            continue

        for method in list(r.methods):
            if method.upper() == 'HEAD' or method.upper() == 'OPTIONS':
                continue

            u = urlparse(url_domain)
            domain = u.netloc if len(u.netloc)>0 else u.path

            collection_json['item'].append({})
            collection_json['item'][-1]['name'] = r.endpoint
            collection_json['item'][-1]['request'] = {}
            collection_json['item'][-1]['response'] = []

    

            route_json = {}
            route_json['name'] = r.endpoint
            route_json['request'] = {}
            route_json['response'] = []
            

            route_json['request']['method'] = method.upper()
            route_json['request']['header'] = []

            route_json['request']['body'] = {}
            route_json['request']['body']['mode'] = 'raw'
            route_json['request']['body']['raw'] = '{\n    \n}'
            route_json['request']['body']['options'] = {}
            route_json['request']['body']['options']['raw'] = {}
            route_json['request']['body']['options']['raw']['language'] = 'json'


            url_json = {}
            url_json['raw'] = f'www.{domain}:{port}{r.rule}'
            url_json['host'] = ['www',domain]
            url_json['port'] = port
            url_json['path'] = r.rule.split('/')

            route_json['request']['url'] = url_json
            collection_json['item'][-1] = route_json

    with open(output_path + f'/{collection_name}.json', 'w', encoding='utf-8') as f:
        json.dump(collection_json, f, ensure_ascii=False, indent=4)

    return
