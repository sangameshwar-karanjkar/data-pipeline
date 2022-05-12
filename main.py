import re
from bs4 import BeautifulSoup
import xml

with open("output00.xml", "r", encoding="utf8",errors='ignore') as f:
    txt = f.read();
    f.close()

with open("_output1.xml", "w", encoding="utf8") as fa:
    datas = re.sub(r'\s+(?=[^\&]*\;)|\s+(?=[^\<]*\>)|[^\x1F-\x7F]','',txt)
    #datas = re.sub(r'\s+(?=[^\<]*\>)','',datas)
    #datas = re.sub(r'[^\x1F-\x7F]','',datas)
    datas = re.sub(r'[&]',',',datas)
    datas = re.sub(r'<+(?=[^\>]*\<)',' less than ',datas)
    #data=BeautifulSoup(datas,'xml')
    fa.write(str(datas))
    fa.close()
    
print("done")
