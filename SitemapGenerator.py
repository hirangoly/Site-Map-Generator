from xml.dom import minidom
import xml.etree.cElementTree as ET

xmldoc = minidom.parse('NEWfeed.xml')
itemlist = xmldoc.getElementsByTagName('link') 
print len(itemlist)
print itemlist[0].attributes['href'].value
data = ET.Element("data")
url = ET.SubElement(data, "url")
loc = ET.SubElement(url, "loc")
freq = ET.SubElement(url, "changefreq")
priority = ET.SubElement(url, "priority")
test = ET.SubElement(url, "test")

for s in itemlist:
	loc.text = s.attributes['href'].value
	if loc.text.find('product.jsp'):
		freq.text = "weekly"
		priority.text = "0.7"
		test.text = "test"
	else:
		freq.text = "weekly"
		priority.text = "1.0"
		test.text = "test"

data.append(url)

tree = ET.ElementTree(data)
tree.write("sitemap.xml")
