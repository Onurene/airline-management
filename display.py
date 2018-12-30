from flask import *
import urllib.request
import pickle

app = Flask(__name__)

@app.route("/")
def home():
    from bs4 import BeautifulSoup

    r = urllib.request.Request('http://bengaluruairport.com/bial/faces/pages/flightInformation/arrivals.jspx?_adf.ctrl-state=fahiczlgy_89&_afrLoop=11153584609016128')
    with urllib.request.urlopen(r) as response:
        html_content = response.read()

    soup = BeautifulSoup(html_content,"html.parser")
    table = soup.find('table',{'class':'x7b'})
    th = table.find_all('th')

    k = " ".join(str(x) for x in th)

    a = k.split('<th class="x7w" scope="col">')
    b =  " ".join(str(x) for x in a)


    c = b.split('<th class="x7w xbb" scope="col">')
    d =  " ".join(str(x) for x in c)
    e = d.split('</th>')
    f =  " ".join(str(x) for x in e)
    print(f)
    print('\n')

    td = table.find_all('td')
    g = "".join(str(x) for x in td)

    h = g.split('<td class="x7m xbp">')
    i =  "".join(str(x) for x in h)

    j = i.split('</td>')
    c = 0
    l = []
    t = []
    for i in j:
        t.append(i)
        c+=1
        if(c==6):
            c = 0
            l.append(t)
            t = []
    listofall = l
    tree = {"names":{}}
    for i in l:
        if(i[0] in tree["names"]):
            tree["names"][i[0]].append(i[1])
        else:
            tree["names"][i[0]] = [i[1]]

    print(tree)
    return render_template('Home.html',l=listofall)

@app.route("/board")
def board():        
    q = {"First Class":1,"Business":2,"Economy":3}
    fp = open("database.dat","rb")
    queue = pickle.load(fp)
    fp.close()
    pq = []
    for i in queue:
        if(pq == []): pq = [i]
        else:
            j = 0
            while(j<len(pq) and q[pq[j][1]] < q[i[1]]):
                j+=1
            pq = pq[:j] + [i] + pq[j:]
    return render_template('Board.html',l=pq)               
    
if __name__ == '__main__':
   app.run(debug = True, port=5000)
