from flask import Flask, request, render_template, redirect, url_for
import requests

app= Flask('app', template_folder='templates')

url = requests.get('https://translate.ge/api/georgia').json()

for item in url['rows']:
    if item['id'] == "6178a2f3562366c5df304612a12bfa61":
        d ={item['value']['Text']:item['value']['Word']}

@app.route('/', methods = ['POST','GET'])
def translate():
    if request.method == 'POST':
        word = request.form['words']
        if word.lower() == 'georgia':
            with open('/home/kokoi/Desktop/translate.txt', 'w') as f:
                f.write(word + ' - ' + str(d))
            return str(d)
        else:
            return "You Entered different word"
            
    return render_template('index.html')

app.run('localhost', 8080)


'''ააწყვეთ სერვისი flask ის გამოყენებით რომელიც თარგმნის ინგლისურ სიტყვებს ქართულად და
 შეინახეთ .txt ფაილში, მნიშვნელობების მოსაძიებლად გამოიყენეთ translate.ge ს *url. (თუ 
 sqlite ის გამოყენებით დაწერთ დაგეწერებათ ბონუს ქულა) ასევე აუცილებელია შექმნათ ცალკე კლასი 
 flask ისთვის და ცალკე კლასი FileManager
 რომელსაც ექნება მეთოდი ფაილში/db ში შენახვის. *url: https://translate.ge/word/georgia *'''