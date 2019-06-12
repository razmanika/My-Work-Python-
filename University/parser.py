from bs4 import BeautifulSoup
import requests

class saparsi: 
    def __init__(self,url):
        self.url = url

    def parsing(self):
        source = requests.get("{}".format(self.url)).text
        soup = BeautifulSoup(source, "html.parser")


        items = soup.find_all(class_=("stie_title", "row_id"))
        myList = []
        string = ""
        for i in items:
            myList.append(i.contents)
        
        for i in range(len(myList)):
            string += "{}{}\n".format(myList[i][0] if i % 2 != 0 else"", myList[i][2][15:17] if i % 2 == 0 else"")

        print(string)

obj = saparsi('https://top.ge/')
obj.parsing()