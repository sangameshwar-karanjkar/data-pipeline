import xml.etree.ElementTree as etree
import codecs
import csv


ENCODING = "utf-8"

def conversion_to_csv(XML_file):
    
    with codecs.open("sample.csv", "w", ENCODING) as csvfile:
        csvfile1 = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
        csvfile1.writerow(['id','title','redirect'])
        
        for event, elem in etree.iterparse(XML_file, events=('start', 'end')):
            tag = str(elem.tag).replace('{http://www.mediawiki.org/xml/export-0.10/}','')
            if event == 'start':
                if tag == 'page':
                    ID = ''
                    Title = ''
                    Redirect = ''
                elif tag == 'id' and ID == '':
                    ID=elem.text
                elif tag == 'title':
                    Title=elem.text
                elif tag == 'redirect':
                    Redirect=str(elem.attrib).replace("'title': ",'').replace("}",'').replace("{",'').replace("'",'')
                
            if event=='end':
                if tag == 'page':
                    if Redirect != '':
                        csvfile1.writerow([ID,Title,Redirect])
            
            elem.clear()
                
                    
                    
if __name__=="__main__":
    
    XML_path="enwiki-20220501-pages-articles-multistream.xml"
    conversion_to_csv(XML_path)