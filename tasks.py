from celery import Celery
import requests
import json
app = Celery('hello', broker='amqp://guest@rabbit//')
import time

app.conf.update(
    task_routes = {
        'tasks.getProfByCategory': {'queue': 'superprof'},
        'tasks.saveProfByCategory' :{'queue':'save'}
    },
)
@app.task
def hello():
    time.sleep(10)
    return 'hello world'
@app.task
def getProfByCategory(category):
    response = requests.get(f"https://www.superprof.com.br/ajax/ajax-AW.php?action=getResults&matiere={category}&place%5B%5D=at_my_place&place%5B%5D=i_move&distance=25&webcam_from=in_pays&order_by=pertinence_DESC&price=all&first_lesson=all&response_time=all&is_mobile=2&pmin=1&pmax=801&url=https%3A%2F%2Fwww.superprof.com.br%2Fs%2Freforco-escolar%2CItabaina--SE--Brasil%2C-10.9472468%2C-37.0730823.html&page=1")
    result = json.loads(response.content)
    
    for x in range(1,result["nbPagesTotal"]):
        saveProfByCategory.delay(category, x) 

@app.task
def saveProfByCategory(category, page):
    with open(f'data/{category}-{page}.txt',"w") as myFile:
        response = requests.get(f"https://www.superprof.com.br/ajax/ajax-AW.php?action=getResults&matiere={category}&place%5B%5D=at_my_place&place%5B%5D=i_move&distance=25&webcam_from=in_pays&order_by=pertinence_DESC&price=all&first_lesson=all&response_time=all&is_mobile=2&pmin=1&pmax=801&url=https%3A%2F%2Fwww.superprof.com.br%2Fs%2Freforco-escolar%2CItabaina--SE--Brasil%2C-10.9472468%2C-37.0730823.html&page={page}")    
        result = json.loads(response.content)
        for x in result["mainResults"]:
            myFile.write(f"{x['teacherName']}-{x['teacherCity']}\n")
        print("Finalizado")
