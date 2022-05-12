import re
from bs4 import BeautifulSoup
import xml

with open("_output1.xml", "r", encoding="utf8",errors='ignore') as f:
    txt = f.read();
    f.close()

with open("_output2.xml", "w", encoding="utf8") as fa:
    datas = re.sub(r'<+(?=[^\>]*\<)',' less than ',txt)
    #datas = re.sub(r'\s+(?=[^\<]*\>)','',datas)
    #datas = re.sub(r'\s+(?=[^\&]*\;)','',datas)
    #datas = re.sub(r'[&]','-',datas)
    #data=BeautifulSoup(datas,'xml')
    fa.write(str(datas))
    fa.close()
    
print("done")
