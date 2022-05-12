from lxml import etree
from lxml.etree import XMLSyntaxError
import sys
import os
import json
import re



#def traverse(child):
 #                   show = True
  #                  for c in child.getchildren():
   #                     show = False
    #                    traverse(c)
     #               if show:
      #                  output_dic['title']=child.text
def remove_xmltag(data):
    p = re.compile(r'<.*?>')
    q = p.sub('', data)
    return q.replace('\n','')
    
                        
                        
source = '/home/jupyter/dblp_test.xml'
dtd = etree.DTD(file='/home/jupyter/dblp.dtd')#read DTD
count = 0
for event, element in etree.iterparse(source,tag='inproceedings', load_dtd=True):
    output_dic={'title':None,'booktitle':None,'year':None,'url':None,'ee':[],'author':[],'pages':None,'crossref':None,
                'conference_series':None,'conference_instance':None,'PaperID':None}


    
    for child in element:
        if child.tag=="title":
                xml_str = etree.tostring(child, encoding='unicode')
                output_dic['title'] = remove_xmltag(xml_str)
                
    
  
        if child.tag=="booktitle":
            output_dic['booktitle']=child.text
        if child.tag=="year":
            output_dic['year']=child.text
        if child.tag=="url":
            output_dic['url']=child.text
            try:
                conference_series_data=re.findall(r'conf\/[a-zA-Z]+\/', child.text)
                series_data=conference_series_data[0].replace('/',"").replace('conf','')
                output_dic['conference_series']=series_data
            except:
                pass
            
            try:
                conference_instance_data=re.findall(r'[a-zA-Z0-9-]+.html',child.text)
                instance_data=conference_instance_data[0].replace('.html','')
                output_dic['conference_instance']=instance_data
            except:
                pass
            
            try:
                paperid_data=re.findall(r'\#.*', child.text)
                paperid_data=paperid_data[0].replace('#','')
                output_dic['PaperID']=paperid_data
            except:
                pass
            
        if child.tag=="ee":
            ee_list=output_dic['ee']
            ee_list+=[child.text]
            output_dic['ee']=ee_list
        if child.tag=="author":
            author_list=output_dic['author']
            author_list+=[child.text]
            output_dic['author']=author_list
        if child.tag=='pages':
            output_dic['pages']=child.text
        if child.tag=="crossref":
            output_dic['crossref']=child.text
        
        #print(child.tag, child.text)
    
    count+=1
    
    with open("/home/jupyter/dblp_output_test7.jsonl","a") as f:
        f.write(json.dumps(output_dic)+"\n")
    element.clear()

print("Final Count :", count)

          
          
   
 #         
 #   bq load \
 #   --autodetect \
 #   --source_format=NEWLINE_DELIMITED_JSON \
 #   microsoft_academic_graph.test \
 #   /home/vikrant_ghadge/dblp_new/dblp_output.jsonl