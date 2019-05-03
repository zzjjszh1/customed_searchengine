
# coding: utf-8

# In[149]:


import sys
from lxml import etree
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET


# In[150]:


urls=["52pojie.cn",
"iplaysoft.com",
"sspai.com",
"runningcheese.com",
"laomoit.com",
"dayanzai.me",
"appinn.com",
"appcgn.com",
"th-sjy.com",
"zuimeia.com",
"coolapk.com",
"greasyfork.org",
"openuserjs.org",
"userscripts-mirror.org",
"extfans.com"]
node_annotations = ET.Element('Annotations')
for url in urls:
    node=ET.SubElement(node_annotations, 'Annotation')
    node.set("about","*."+url+"/*")
    nodelabel = ET.SubElement(node,"Label")
    nodelabel.set("name","_cse_5sagvkts2oq")
    node_additional=ET.SubElement(node,"AdditionalData")
    node_additional.set("attribute","original_url")
    node_additional.set("value",url)
tree=ET.ElementTree(node_annotations)
tree.write(sys.stdout)


# In[151]:


urls=["zhihu.com",
"jianshu.com",
"quora.com",
"bilibili.com",
"youtube.com"]
node_annotations = ET.Element('Annotations')
for url in urls:
    node=ET.SubElement(node_annotations, 'Annotation')
    node.set("about","*."+url+"/*")
    nodelabel = ET.SubElement(node,"Label")
    nodelabel.set("name","_cse_r8r0h_2rqie")
    node_additional=ET.SubElement(node,"AdditionalData")
    node_additional.set("attribute","original_url")
    node_additional.set("value",url)
tree=ET.ElementTree(node_annotations)
tree.write(sys.stdout)


# In[153]:


urls=["btbtt08.com",
"wuhaozhan.net",
"baike789.com",
"btba.cc",
"2tu.cc",
"piaov.com",
"loldytt.org",
"dy2018.com",
"dytt8.net",
"mp4ba.com",
"cupfox.com",
"ygdy8.com",
"91mjw.com",
"zxzjs.com",
"meijutt.com",
"zmz2019.com"]
node_annotations = ET.Element('Annotations')
for url in urls:
    node=ET.SubElement(node_annotations, 'Annotation')
    node.set("about","*."+url+"/*")
    nodelabel = ET.SubElement(node,"Label")
    nodelabel.set("name","_cse_rekrhjbzzci")
    node_additional=ET.SubElement(node,"AdditionalData")
    node_additional.set("attribute","original_url")
    node_additional.set("value",url)
tree=ET.ElementTree(node_annotations)
tree.write(sys.stdout)


# In[154]:


urls=["bbc.com",
"jlpcn.net",
"topdocumentaryfilms.com",
"onehourlife.com",
"laojilu.com",
"bilibili.com",
"85lou.com",
"acfun.cn"]
node_annotations = ET.Element('Annotations')
for url in urls:
    node=ET.SubElement(node_annotations, 'Annotation')
    node.set("about","*."+url+"/*")
    nodelabel = ET.SubElement(node,"Label")
    nodelabel.set("name","_cse_rekrhjbzzci")
    node_additional=ET.SubElement(node,"AdditionalData")
    node_additional.set("attribute","original_url")
    node_additional.set("value",url)
tree=ET.ElementTree(node_annotations)
tree.write(sys.stdout)

