import requests
import json
from tasks import getprofbycategory

categories = [
    {
        "id_matiere":4,
        "matiere":"Refor%C3%A7o%20escolar"

    },
    {
        "id_matiere":224,
        "matiere":"Ingl%C3%AAs"
    }
]
for category in categories:
    response = requests.get(f"https://www.superprof.com.br/ajax/ajax-AW.php?action=getResults&type=1&lat=-10.9472468&lng=-37.0730823&adress=Aracaju%2C%20SE%2C%20Brasil&id_matiere={category['id_matiere']}&matiere={category['matiere']}&place%5B%5D=at_my_place&place%5B%5D=i_move&distance=25&webcam_from=in_pays&order_by=pertinence_DESC&price=all&first_lesson=all&response_time=all&is_mobile=2&pmin=1&pmax=801&url=https%3A%2F%2Fwww.superprof.com.br%2Fs%2Freforco-escolar%2CItabaina--SE--Brasil%2C-10.9472468%2C-37.0730823.html&page=1")
    result = json.loads(response.content)
    for x in range(1,result["nbPagesTotal"]+1):
        getprofbycategory.delay(category['matiere'], category['id_matiere'], x)
    