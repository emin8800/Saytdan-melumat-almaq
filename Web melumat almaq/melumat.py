from bs4 import BeautifulSoup
import requests
import time


def maliyoxla():
    URL = "https://kontakt.az/az/noutbuk-apple-macbook-pro-13-mly33ru-a-midnight"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
    }
    sehife = requests.get(URL, headers=headers)
    melumat = BeautifulSoup(sehife.content, 'html.parser')

    page_title_wrapper = melumat.find(attrs={"data-ui-id": "page-title-wrapper"})
    malin_adi = page_title_wrapper.get_text().strip()

    qiymet_text = melumat.find(id="product-price-31963").get_text()
    qiymet = ''.join(filter(str.isdigit, qiymet_text))

    if qiymet and int(qiymet) < 2000:
        print(f"{qiymet} ₼ {malin_adi} Qitmet düşdü")
    elif qiymet:
        print(f"{qiymet} ₼ {malin_adi} Qitmet 2000-dən yuxarıdır")
    else:
        print("Qiymet tapılmadı veya düzgün formatda deyil")

while(True):
    maliyoxla()
    time.sleep(10)