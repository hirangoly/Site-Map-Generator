Site-Map-Generator
==================
The purpose of this script is to generate site-map for a website.

Basic Steps:
* Extract all the pages of a website and scrap all the tags associated and store in a file (file can be txt, xml, etc). I preferred xml file. i.e dataFeed.xml. I used to get this file over sftp from the client.
* Extract url from the file and store in a desired format. In my case I scraped url along with priority based on product/category page and frequency of the page. script used is sitemapgenerator.py and output file is sitemap.xml
* Validate xml file as a valid sitemap using this online tool:
http://freetools.webmasterworld.com/tools/site-validator/
you may need to add this line on top of the file:
<?xml version="1.0" encoding="UTF-8"?>

You can automate this process if you keep getting multiple datafeed files from the client and want to avoid duplicates. For that you need to store all the urls in the database and flag it once extracted so that you can validate that in your script if get duplicate url.
