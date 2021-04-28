import collections, importlib, subprocess, time, random, threading, os
from pathlib import Path
from flask import Flask, redirect

with open("Dockerfile", "w") as dockerfile:
    dockerfile.write("FROM spysravan/codeserver \nRUN apt update && apt install unzip -y\n")

techs = []
for i, f in enumerate(Path('catalog').glob('**/*.py')):
    techs.append(str(f)[:-3])
    print(str(i) + ": " + f.name[:-3])

tech_inps = input('Enter the technologies: ')

process_output = ''
def get_output(process):
    global process_output
    term_wid = int(os.popen('stty size', 'r').read().split()[1]) - 20
    while process.poll() is None:
        process_output = process.stdout.readline().decode("utf-8")[:term_wid].strip().replace('\n','').replace('\\','')
        time.sleep(0.1) 

def build_docker(n = 6):
    global process_output
    txt_colors = ['\033[95m','\033[94m','\033[96m','\033[92m','\033[93m','\033[91m','\033[0m']
    process = subprocess.Popen(['bash', '-c', 'docker build -t custom .'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    threading.Thread(target=get_output, args=(process,)).start()
    while process.poll() is None:
        points = list(range(1,n)) + list(range(1,n-1)[::-1]) + list(range(2,n)) + list(range(1,n-1)[::-1])
        spaces = [0]*(n-1) + list(range(1,n-1)) + list(range(n-2)[::-1]) + [0] * (n-2)
        e_spaces = list(range(1,n-1)[::-1]) + [0] * (n+3) + list(range(1,n-1))
        for s,p,e in zip(spaces,points,e_spaces):
            print('Installing ' + random.choice(txt_colors) + ' '*s + '.'*p + ' '*e + '\033[0m  ' + process_output, end='\r')
            time.sleep(0.1)
    return process.returncode, process.communicate()

for i in tech_inps.split(','):
    try:
        importlib.import_module(techs[int(i)].replace('/', '.'))
        res_code, stdouterr = build_docker()
        if res_code == 0:
            print('\033[1m \033[92m Successfully installed \033[0m')
        else:
            print(stdouterr[0][-200:])
            print(stdouterr[0][-200:])
    except:
        pass



qstns = []
for i, f in enumerate(Path('qstns').glob('**/*.zip')):
    qstns.append(str(f))
    print(str(i) + ": " + f.name[:-4])

qstn_no = int(input('Enter question number: ') or 0)
with open("Dockerfile", "a") as dockerfile:
    dockerfile.write("ADD " + qstns[qstn_no] + " /root/challenge.zip \n")
    dockerfile.write("RUN cd /root && unzip challenge.zip && rm challenge.zip \n")
build_docker()

# inp_run = input("\nDo you want to run the docker image (y/n): ") or 'n'
# if inp_run == 'y':
#     process = subprocess.Popen(['bash', '-c', 'docker run -d -p 80:80 custom'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     print("docker running at http://0.0.0.0:80")




app = Flask(__name__)

@app.route('/<id>')
@app.route('/', defaults={'id': 0})
def hello_world(id):
    id += 8000 
    process = subprocess.Popen(['bash', '-c', 'docker run -d -p ' + str(id) + ':80 custom'],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return redirect("http://localhost:" + str(id), code=302)

if __name__ == '__main__':
   app.run(debug=True)
