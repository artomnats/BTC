#!/usr/bin/env python3.5
try:
    from bs4 import BeautifulSoup
    import requests
except ImportError as exc:
        print(exc)
        exit(0)

crypto_info={}

def scrap_yahoo_finance(url):
    min_max = {}
    source=requests.get(url).text
    soup = BeautifulSoup(source,'html.parser')
    all_info=soup.find('tr' ,attrs={'data-reactid':'53'})
    info=all_info.text.split('e')[1].split()
    min_max["min"]=info[0]
    min_max["max"]=info[2]
    crypto_info["Yahoo Finance"]=min_max
    return crypto_info
#def scrap_daily_fx(url):
#    min_max = {}
#    source=requests.get(url).text
#    soup = BeautifulSoup(source,'html.parser')
#    all_info=soup.find('div' ,attrs={'class':'dfx-lowHighFigures__low mr-1'})
    #info=all_info.text.split('e')[1].split()
#    return all_info
    #min_max["min"]=info[0]
    #min_max["max"]=info[2]
    #crypto_info["Yahoo Finance"]=min_max
    #return crypto_info
def scrap_wallet_investor(url):
    min_max = {}
    source=requests.get(url).text
    soup = BeautifulSoup(source,'html.parser')
    all_info=soup.find('tr' ,attrs={'data-key':'0'})
    min_=all_info.find('td',attrs={'data-col-seq':'2'}).text.split()[1]
    max_=all_info.find('td',attrs={'data-col-seq':'3'}).text.split()[1]
    min_max["min"]=min_
    min_max["max"]=max_
    crypto_info["Wallet Investor"]=min_max
    return crypto_info

def scrap_crowd_wisdom(url):
    min_max = {}
    source=requests.get(url).text
    soup = BeautifulSoup(source,'html.parser')
    all_info=soup.find('strong').text.split('between')[1].split('and')
    min_max["min"]=all_info[0].replace("$",'').replace('.','').replace(" ",'')
    min_max["max"]=all_info[1].replace("$",'').replace('.','').replace(" ",'')
    crypto_info["Crowd Wisdom"]=min_max
    return crypto_info

#def scrap_etoro(url):
    #bitcoin_live_price = {}
#    source=requests.get(url,timeout=(5,40)).text
#    soup = BeautifulSoup(source,'html.parser')
#    all_info=soup.find('div') #,attrs={'automation-id':'buy-sell-button-rate-value'})
    #all_info=soup.find('span')
    #min_max["min"]=all_info[0].replace("$",'').replace('.','').replace(" ",'')
    #min_max["max"]=all_info[1].replace("$",'').replace('.','').replace(" ",'')
    #crypto_info["Live Price"]=min_max
#    return all_info
    #aa=all_info.find_all('strong')
    #min_=all_info.find('td',attrs={'data-col-seq':'2'}).text.split()[1]
    #max_=all_info.find('td',attrs={'data-col-seq':'3'}).text.split()[1]
    #min_max["min"]=min_
    #min_max["max"]=max_
    #crypto_info["Wallet Investor"]=min_max
page_url_1 = 'https://finance.yahoo.com/quote/BTC-USD?p=BTC-USD&.tsrc=fin-srch&guce_referrer=aHR0cHM6Ly9maW5hbmNlLXlhaG9vLWNvbS5jZG4uYW1wcHJvamVjdC5vcmcvdi9zL2ZpbmFuY2UueWFob28uY29tL2FtcGh0bWwvbmV3cy9iaXRjb2luLXByaWNlLXByZWRpY3Rpb24tYnVsbHMtYmFjay0xMTU3MzkzMDguaHRtbA&guce_referrer_sig=AQAAAARyPncQi0dmHLO1R7VSr7JW1gJd2TsVDtZXtZHLQEPtbXJEveHTS7n9jeE9SKpShqTAj8-HH8flRcf5dk_dMKy9Ry7GCHFWPv9BER3HfIwFXMqqJW2HVEJpF8nE6nJFowIAhoRbesWl8aGU8eZGCCRqJY5_OXRHQvUuomSoNpYT&guccounter=2'
scrap_yahoo_finance(page_url_1)
page_url_3='https://walletinvestor.com/forecast/bitcoin-prediction'
scrap_wallet_investor(page_url_3)
page_url_4='https://crowdwisdom.live/us-stocks/bitcoin-price-prediction/'
scrap_crowd_wisdom(page_url_4)
print(crypto_info)
