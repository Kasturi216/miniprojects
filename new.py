import requests
from bs4 import BeautifulSoup

def translator(target,lang):
    from deep_translator import GoogleTranslator
    translated = GoogleTranslator(source='auto', target=str(lang)).translate(target)
    return translated

def scraplator(url):
	page=requests.get(url).content
	soup=BeautifulSoup(page,"html.parser")
	story=''
	for ele in soup.find("div",class_="sqs-block-content"):
	#     print(translator(ele.text,"bn"))
	    story+=translator(ele.text,"bn")+str('\n')
	for ele in soup.find_all("p")[3:]:
	#     print(translator(ele.text,"bn"))
	    story+=translator(ele.text,"bn")+str('\n')
	return story

url=input(">")
print(scraplator(url))

