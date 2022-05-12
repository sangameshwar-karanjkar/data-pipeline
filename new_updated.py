import re
import codecs
import csv
import time

def conversion_to_csv(XML_path):
    
    number_record = 0
    
    source = open(XML_path,'rb')
    with codecs.open("New_bcpdump.csv", "w", ENCODING) as csvfile:
        csvfile1 = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
        csvfile1.writerow(['ID', 'J_ID','FLC','PRODUCT_ID','PRODUCT_TITLE','MS_DOC_ID','MS_ID','MS_ID_GLOBAL','MS_ARTICLE_TYPE',
                      'MS_TITLE','MS_ABSTRACT','MS_FIRST_RECEIPT_DATE','MS_FINAL_DECISION_DATE','MS_FINAL_DECISION_TERM',
                      'MS_FINAL_DECISION_FAMILY','MS_FINAL_DISPOSITION_DATE','MS_FINAL_DISPOSITION_TERM','MS_TRANSFER_OFFER_TARGET',
                      'AU_TYPE','AU_TITLE','AU_FIRST_NAME','AU_LAST_NAME','AU_EMAIL','AU_COUNTRY','AU_INSTITUTE','LAST_UPDATE_TIMESTAMP'])
        
        while True:
            
            source_data = source.read(1600 * 1600)
            source_data = re.sub(r'|\s+(?=[^\<]*\>)|[^\x1F-\x7F]','',str(source_data))
            records = re.findall(r"<Record>[\s\S]*?<\/Record>",str(source_data))
            
            if len(records) == 0:
                break
            else:
                number_record=number_record+len(records)
                for record in records:
                    
                    try:
                        ID = re.findall(r"(?:<ID>)([\s\S]*)(?:<\/ID>)",record)[0]
                    except:
                        ID =''
                    
                    try:
                        J_ID = re.findall(r"(?:<J_ID>)([\s\S]*)(?:<\/J_ID>)",record)[0]
                    except:
                        J_ID =''
                        
                    try:
                        FLC = re.findall(r"(?:<FLC>)([\s\S]*)(?:<\/FLC>)",record)[0]
                    except:
                        FLC =''
                        
                    try:
                        PRODUCT_ID = re.findall(r"(?:<PRODUCT_ID>)([\s\S]*)(?:<\/PRODUCT_ID>)",record)[0]
                    except:
                        PRODUCT_ID =''
                    
                    try:
                        PRODUCT_TITLE = re.findall(r"(?:<PRODUCT_TITLE>)([\s\S]*)(?:<\/PRODUCT_TITLE>)",record)[0]
                    except:
                        PRODUCT_TITLE =''
                        
                    try:
                        MS_DOC_ID = re.findall(r"(?:<MS_DOC_ID>)([\s\S]*)(?:<\/MS_DOC_ID>)",record)[0]
                    except:
                        MS_DOC_ID =''
                    
                    try:
                        MS_ID = re.findall(r"(?:<MS_ID>)([\s\S]*)(?:<\/MS_ID>)",record)[0]
                    except:
                        MS_ID =''
                        
                    try:
                        MS_ID_GLOBAL = re.findall(r"(?:<MS_ID_GLOBAL>)([\s\S]*)(?:<\/MS_ID_GLOBAL>)",record)[0]
                    except:
                        MS_ID_GLOBAL =''
                        
                    try:
                        MS_ARTICLE_TYPE = re.findall(r"(?:<MS_ARTICLE_TYPE>)([\s\S]*)(?:<\/MS_ARTICLE_TYPE>)",record)[0]
                    except:
                        MS_ARTICLE_TYPE =''
                        
                    try:
                        MS_TITLE = re.findall(r"(?:<MS_TITLE>)([\s\S]*)(?:<\/MS_TITLE>)",record)[0]
                    except:
                        MS_TITLE =''
                        
                    try:
                        MS_ABSTRACT = re.findall(r"(?:<MS_ABSTRACT>)([\s\S]*)(?:<\/MS_ABSTRACT>)",record)[0]
                    except:
                        MS_ABSTRACT =''
                        
                    try:
                        MS_FIRST_RECEIPT_DATE = re.findall(r"(?:<MS_FIRST_RECEIPT_DATE>)([\s\S]*)(?:<\/MS_FIRST_RECEIPT_DATE>)",record)[0]
                    except:
                        MS_FIRST_RECEIPT_DATE =''
                        
                    try:
                        MS_FINAL_DECISION_DATE = re.findall(r"(?:<MS_FINAL_DECISION_DATE>)([\s\S]*)(?:<\/MS_FINAL_DECISION_DATE>)",record)[0]
                    except:
                        MS_FINAL_DECISION_DATE =''
                        
                    try:
                        MS_FINAL_DECISION_TERM = re.findall(r"(?:<MS_FINAL_DECISION_TERM>)([\s\S]*)(?:<\/MS_FINAL_DECISION_TERM>)",record)[0]
                    except:
                        MS_FINAL_DECISION_TERM =''
                        
                    try:
                        MS_FINAL_DECISION_FAMILY = re.findall(r"(?:<MS_FINAL_DECISION_FAMILY>)([\s\S]*)(?:<\/MS_FINAL_DECISION_FAMILY>)",record)[0]
                    except:
                        MS_FINAL_DECISION_FAMILY =''
                    
                    try:
                        MS_FINAL_DISPOSITION_DATE = re.findall(r"(?:<MS_FINAL_DISPOSITION_DATE>)([\s\S]*)(?:<\/MS_FINAL_DISPOSITION_DATE>)",record)[0]
                    except:
                        MS_FINAL_DISPOSITION_DATE =''
                        
                    try:
                        MS_FINAL_DISPOSITION_TERM = re.findall(r"(?:<MS_FINAL_DISPOSITION_TERM>)([\s\S]*)(?:<\/MS_FINAL_DISPOSITION_TERM>)",record)[0]
                    except:
                        MS_FINAL_DISPOSITION_TERM =''
                        
                    try:
                        MS_TRANSFER_OFFER_TARGET = re.findall(r"(?:<MS_TRANSFER_OFFER_TARGET>)([\s\S]*)(?:<\/MS_TRANSFER_OFFER_TARGET>)",record)[0]
                    except:
                        MS_TRANSFER_OFFER_TARGET =''
                    
                    try:
                        AU_TYPE = re.findall(r"(?:<AU_TYPE>)([\s\S]*)(?:<\/AU_TYPE>)",record)[0]
                    except:
                        AU_TYPE =''
                        
                    try:
                        AU_TITLE = re.findall(r"(?:<AU_TITLE>)([\s\S]*)(?:<\/AU_TITLE>)",record)[0]
                    except:
                        AU_TITLE =''
                        
                    try:
                        AU_FIRST_NAME = re.findall(r"(?:<AU_FIRST_NAME>)([\s\S]*)(?:<\/AU_FIRST_NAME>)",record)[0]
                    except:
                        AU_FIRST_NAME =''
                        
                    try:
                        AU_LAST_NAME = re.findall(r"(?:<AU_LAST_NAME>)([\s\S]*)(?:<\/AU_LAST_NAME>)",record)[0]
                    except:
                        AU_LAST_NAME =''
                        
                    try:
                        AU_EMAIL = re.findall(r"(?:<AU_EMAIL>)([\s\S]*)(?:<\/AU_EMAIL>)",record)[0]
                    except:
                        AU_EMAIL =''
                        
                    try:
                        AU_COUNTRY = re.findall(r"(?:<AU_COUNTRY>)([\s\S]*)(?:<\/AU_COUNTRY>)",record)[0]
                    except:
                        AU_COUNTRY =''
                        
                    try:
                        AU_INSTITUTE = re.findall(r"(?:<AU_INSTITUTE>)([\s\S]*)(?:<\/AU_INSTITUTE>)",record)[0]
                    except:
                        AU_INSTITUTE =''
                        
                    try:
                        LAST_UPDATE_TIMESTAMP = re.findall(r"(?:<LAST_UPDATE_TIMESTAMP>)([\s\S]*)(?:<\/LAST_UPDATE_TIMESTAMP>)",record)[0]
                    except:
                        LAST_UPDATE_TIMESTAMP =''
                        
                    
                    csvfile1.writerow([ID,J_ID,FLC,PRODUCT_ID,PRODUCT_TITLE,MS_DOC_ID,MS_ID,MS_ID_GLOBAL,MS_ARTICLE_TYPE,
                                       MS_TITLE,MS_ABSTRACT,MS_FIRST_RECEIPT_DATE,MS_FINAL_DECISION_DATE,MS_FINAL_DECISION_TERM,
                                       MS_FINAL_DECISION_FAMILY,MS_FINAL_DISPOSITION_DATE,MS_FINAL_DISPOSITION_TERM,MS_TRANSFER_OFFER_TARGET,
                                       AU_TYPE,AU_TITLE,AU_FIRST_NAME,AU_LAST_NAME,AU_EMAIL,AU_COUNTRY,AU_INSTITUTE,LAST_UPDATE_TIMESTAMP])
                    #time.sleep(0.05)
                    
            
    print("number_record : ",number_record)

if __name__=="__main__":
    
    XML_path="bcpdump.xml"
    ENCODING = "utf-8"
    conversion_to_csv(XML_path)