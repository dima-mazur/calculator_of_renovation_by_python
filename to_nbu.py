import requests


def get_rate(date: str):
    # date = '20220912'
    valcode = 'USD'
    base_link = f'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchangenew?valcode={valcode}&date={date}&json'

    resp = requests.get(base_link)
    data = resp.json()
    # print(data)
    usd_rate = data[0]['rate']
    # print(usd_rate)
    return usd_rate
