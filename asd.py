import requests

from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings

disable_warnings(InsecureRequestWarning)

def search_Ara_Book_11(word ,stemming=True, proximity=10):
    cookies = {
        '_ga': 'GA1.3.1755588720.1661443352',
        'appstore': '%7B%7D',
        'MISESSID': 'jb0aobtu6fv8b3c7798q3v3290',
        '_pk_id.3.035b': '975552cbbfa24b67.1661590743.',
        '_gid': 'GA1.3.26534669.1661590743',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.5',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'X-Requested-With': 'XMLHttpRequest',
        'Authorization': 'Bearer jb0aobtu6fv8b3c7798q3v3290',
        'Content-Type': 'application/json;charset=utf-8',
        'Origin': 'https://manahej.moe.gov.jo',
        'Connection': 'keep-alive',
        'Referer': 'https://manahej.moe.gov.jo/zoom/208/view?page=202&p=separate&search=%D8%A7%D9%85&hlid=625307&tool=search&view=0,2588,1665,143',
        # Requests sorts cookies= alphabetically
        # 'Cookie': '_ga=GA1.3.1755588720.1661443352; appstore=%7B%7D; MISESSID=jb0aobtu6fv8b3c7798q3v3290; _pk_id.3.035b=975552cbbfa24b67.1661590743.; _gid=GA1.3.26534669.1661590743',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
    }

    json_data = {
        'text': word,
        'stemming': stemming,
        'proximity': proximity,
    }

    response = requests.post('https://manahej.moe.gov.jo/api/search/highlight/208', cookies=cookies, headers=headers, json=json_data, verify=False)
    import json
    y = json.loads(response.content)
    return y['count']

print(search_Ara_Book_11("الام", False, -1))

word = str(input("اعطيني كلمة للبحث عنها ؟ "))
print(search_Ara_Book_11(word))

word = str(input("اعطيني كلمة للبحث عنها ؟ "))
print(search_Ara_Book_11(word, False, -1))
