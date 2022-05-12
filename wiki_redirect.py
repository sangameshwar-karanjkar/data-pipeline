import xml.etree.ElementTree as etree
from google.cloud import pubsub_v1
from  concurrent.futures import ThreadPoolExecutor
import json



def publish_message(record):
    publisher.publish(topic_path,data=json.dumps(record).encode('utf-8'))

def Pub_Sub(XML_file):
    datal=[]
    for event, elem in etree.iterparse(XML_file, events=('start', 'end')):
        tag = str(elem.tag).replace('{http://www.mediawiki.org/xml/export-0.10/}','')
        if event == 'start':
            
            if tag == 'page':
                dic={'ID':'','Title':'','Redirect':''}
                
            elif tag == 'id' and dic['ID'] == '':
                dic['ID']=elem.text
                
            elif tag == 'title':
                dic['Title']=elem.text
                
            elif tag == 'redirect':
                dic['Redirect']=str(elem.attrib).replace("'title': ",'').replace("}",'').replace("{",'').replace("'",'')
                
        if event=='end':
            if tag == 'page':
                if dic['Redirect'] != '':
                    datal.append(dic)
        
        if(len(datal)==1000):
            with ThreadPoolExecutor(max_workers=1000) as executor:
                future = executor.map(publish_message, datal)
                #print(future.result())
            datal=[]
                    
                    
        elem.clear()
    with ThreadPoolExecutor(max_workers=1000) as executor:
        future = executor.map(publish_message, datal)
        
                    
if __name__=="__main__":
    
    XML_path="enwiki-20220501-pages-articles-multistream.xml"
    topic = 'wikiredirect'
    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path("springer-nature-analytics",topic)
    Pub_Sub(XML_path)