import xml.etree.ElementTree as etree
import codecs
import csv


ENCODING = "utf-8"
def strip_tag_name(t):
    #t = elem.tag
    idx = k = t.rfind("}")
    if idx != -1:
        t = t[idx + 1:]
    return t


def conversion_to_csv(XML_file):
    
    with codecs.open("sample_csv.csv", "w", ENCODING) as csvfile:
        csvfile1 = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
        csvfile1.writerow(['ID', 'J_ID','FLC','PRODUCT_ID','PRODUCT_TITLE','MS_DOC_ID','MS_ID','MS_ID_GLOBAL','MS_ARTICLE_TYPE',
                      'MS_TITLE','MS_ABSTRACT','MS_FIRST_RECEIPT_DATE','MS_FINAL_DECISION_DATE','MS_FINAL_DECISION_TERM',
                      'MS_FINAL_DECISION_FAMILY','MS_FINAL_DISPOSITION_DATE','MS_FINAL_DISPOSITION_TERM','MS_TRANSFER_OFFER_TARGET',
                      'AU_TYPE','AU_TITLE','AU_FIRST_NAME','AU_LAST_NAME','AU_EMAIL','AU_COUNTRY','AU_INSTITUTE','LAST_UPDATE_TIMESTAMP'])
        
        
        for event, elem in etree.iterparse(XML_file, events=('start', 'end')):
            tname = strip_tag_name(elem.tag)
            if event == 'start':
                if tname == 'Record':
                    ID=''
                    J_ID=''
                    FLC=''
                    PRODUCT_ID=''
                    PRODUCT_TITLE=''
                    MS_DOC_ID=''
                    MS_ID=''
                    MS_ID_GLOBAL=''
                    MS_ARTICLE_TYPE=''
                    MS_TITLE=''
                    MS_ABSTRACT=''
                    MS_FIRST_RECEIPT_DATE=''
                    MS_FINAL_DECISION_DATE=''
                    MS_FINAL_DECISION_TERM=''
                    MS_FINAL_DECISION_FAMILY=''
                    MS_FINAL_DISPOSITION_DATE=''
                    MS_FINAL_DISPOSITION_TERM=''
                    MS_TRANSFER_OFFER_TARGET=''
                    AU_TYPE=''
                    AU_TITLE=''
                    AU_FIRST_NAME=''
                    AU_LAST_NAME=''
                    AU_EMAIL=''
                    AU_COUNTRY=''
                    AU_INSTITUTE=''
                    LAST_UPDATE_TIMESTAMP=''
                elif tname=='ID':
                    ID=elem.text
                elif tname=='J_ID':
                    J_ID=elem.text
                elif tname=='FLC':
                    FLC=elem.text
                elif tname=='PRODUCT_ID':
                    PRODUCT_ID=elem.text
                elif tname=='PRODUCT_TITLE':
                    PRODUCT_TITLE=elem.text
                elif tname=='MS_DOC_ID':
                    MS_DOC_ID=elem.text
                elif tname=='MS_ID':
                    MS_ID=elem.text
                elif tname=='MS_ID_GLOBAL':
                    MS_ID_GLOBAL=elem.text
                elif tname=='MS_ARTICLE_TYPE':
                    MS_ARTICLE_TYPE=elem.text
                elif tname=='MS_TITLE':
                    MS_TITLE=elem.text
                elif tname=='MS_ABSTRACT':
                    MS_ABSTRACT=elem.text
                elif tname=='MS_FIRST_RECEIPT_DATE':
                    MS_FIRST_RECEIPT_DATE=elem.text
                elif tname=='MS_FINAL_DECISION_DATE':
                    MS_FINAL_DECISION_DATE=elem.text
                elif tname=='MS_FINAL_DECISION_TERM':
                    MS_FINAL_DECISION_TERM=elem.text
                elif tname=='MS_FINAL_DECISION_FAMILY':
                    MS_FINAL_DECISION_FAMILY=elem.text
                elif tname=='MS_FINAL_DISPOSITION_DATE':
                    MS_FINAL_DISPOSITION_DATE=elem.text
                elif tname=='MS_FINAL_DISPOSITION_TERM':
                    MS_FINAL_DISPOSITION_TERM=elem.text
                elif tname=='MS_TRANSFER_OFFER_TARGET':
                    MS_TRANSFER_OFFER_TARGET=elem.text
                elif tname=='AU_TYPE':
                    AU_TYPE=elem.text
                elif tname=='AU_TITLE':
                    AU_TITLE=elem.text
                elif tname=='AU_FIRST_NAME':
                    AU_FIRST_NAME=elem.text
                elif tname=='AU_LAST_NAME':
                    AU_LAST_NAME=elem.text
                elif tname=='AU_EMAIL':
                    AU_EMAIL=elem.text
                elif tname=='AU_COUNTRY':
                    AU_COUNTRY=elem.text
                elif tname=='AU_INSTITUTE':
                    AU_INSTITUTE=elem.text
                elif tname=='LAST_UPDATE_TIMESTAMP':
                    LAST_UPDATE_TIMESTAMP=elem.text
                
            if event=='end':
                if tname == 'Record':
                    csvfile1.writerow([ID,J_ID,FLC,PRODUCT_ID,PRODUCT_TITLE,MS_DOC_ID,MS_ID,MS_ID_GLOBAL,MS_ARTICLE_TYPE,
                                       MS_TITLE,MS_ABSTRACT,MS_FIRST_RECEIPT_DATE,MS_FINAL_DECISION_DATE,MS_FINAL_DECISION_TERM,
                                       MS_FINAL_DECISION_FAMILY,MS_FINAL_DISPOSITION_DATE,MS_FINAL_DISPOSITION_TERM,MS_TRANSFER_OFFER_TARGET,
                                       AU_TYPE,AU_TITLE,AU_FIRST_NAME,AU_LAST_NAME,AU_EMAIL,AU_COUNTRY,AU_INSTITUTE,LAST_UPDATE_TIMESTAMP])
            
            elem.clear()
        


if __name__=="__main__":
    
    XML_path="_output1.xml"
    conversion_to_csv(XML_path)
    
