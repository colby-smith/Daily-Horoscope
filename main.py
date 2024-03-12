import requests
import string
from bs4 import BeautifulSoup
from datetime import date

def main():
    starsign = get_starsign()
    get_date(starsign)
    content = get_horoscope_content(starsign)
             
    for c in content:
        horoscope_text = content.text.strip()
        if "See All Signs" not in horoscope_text:
            print (horoscope_text)
    print ("---------------------------------------------------------------------------------------------------------------------------------")
    
def get_starsign():
    get_starsign = input("Please enter your starsign to recieve your daily horoscope: ").strip().lower()
    starsign_list = ["scorpio", "aries", "cancer", "capricorn", "gemini", "libra", "taurus", "virgo", "aquarius", "pisces", "leo", "sagittarius"]
    if get_starsign in starsign_list:
        return (get_starsign)
    else:
        raise Exception ("Input must be one of the twelve starsigns")
    
def get_date(starsign):
    today = date.today()
    formated_date = today.strftime("%B %d")
    display_date = (f"Your daily horoscope for {formated_date}th is:")
    print (f"-------------------------------------------{display_date}-------------------------------------------")

def get_horoscope_content(starsign):
    headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
    if starsign == "aquarius":
        page = requests.get("https://www.elle.com/horoscopes/daily/a107/aquarius-daily-horoscope/", headers=headers)
        soup = BeautifulSoup(page.text, "html.parser")
        content = soup.find(class_="css-1nd4gv7 et3p2gv0") 
        return (content)
    if starsign == "libra":
        page = requests.get("https://www.elle.com/horoscopes/daily/a103/libra-daily-horoscope/", headers=headers)
        soup = BeautifulSoup(page.text, "html.parser")
        content = soup.find(class_="css-1nd4gv7 et3p2gv0")
        return (content)
    if starsign == "capricorn":
        page = requests.get("https://www.elle.com/horoscopes/daily/a106/capricorn-daily-horoscope/", headers=headers)
        soup = BeautifulSoup(page.text, "html.parser")
        content = soup.find(class_="css-1nd4gv7 et3p2gv0")
        return (content)
    if starsign == "virgo":
        page = requests.get("https://www.elle.com/horoscopes/daily/a102/virgo-daily-horoscope/", headers=headers)
        soup = BeautifulSoup(page.text, "html.parser")
        content = soup.find(class_="css-1nd4gv7 et3p2gv0")
        return (content)
    if starsign == "pisces":
        page = requests.get("https://www.elle.com/horoscopes/daily/a108/pisces-daily-horoscope/", headers=headers)
        soup = BeautifulSoup(page.text, "html.parser")
        content = soup.find(class_="css-1nd4gv7 et3p2gv0")
        return (content)
    if starsign == "sagittarius":
        page = requests.get("https://www.elle.com/horoscopes/daily/a105/sagittarius-daily-horoscope/", headers=headers)
        soup = BeautifulSoup(page.text, "html.parser")
        content = soup.find(class_="css-1nd4gv7 et3p2gv0")
        return (content)
    if starsign == "leo":
        page = requests.get("https://www.elle.com/horoscopes/daily/a101/leo-daily-horoscope/", headers=headers)
        soup = BeautifulSoup(page.text, "html.parser")
        content = soup.find(class_="css-1nd4gv7 et3p2gv0")        
        return (content)
    if starsign == "scorpio":
        page = requests.get("https://www.elle.com/horoscopes/daily/a104/scorpio-daily-horoscope/", headers=headers)
        soup = BeautifulSoup(page.text, "html.parser")
        content = soup.find(class_="css-1nd4gv7 et3p2gv0")         
        return (content)
    if starsign == "cancer":
        page = requests.get("https://www.elle.com/horoscopes/daily/a100/cancer-daily-horoscope/", headers=headers)
        soup = BeautifulSoup(page.text, "html.parser")
        content = soup.find(class_="css-1nd4gv7 et3p2gv0")
        return (content)
    if starsign == "gemini":
        page = requests.get("https://www.elle.com/horoscopes/daily/a99/gemini-daily-horoscope/", headers=headers)
        soup = BeautifulSoup(page.text, "html.parser")
        content = soup.find(class_="css-1nd4gv7 et3p2gv0")
        return (content)
    if starsign == "taurus":
        page = requests.get("https://www.elle.com/horoscopes/daily/a98/taurus-daily-horoscope/", headers=headers)
        soup = BeautifulSoup(page.text, "html.parser")
        content = soup.find(class_="css-1nd4gv7 et3p2gv0")
        return (content)
    if starsign == "aries":
        page = requests.get("https://www.elle.com/horoscopes/daily/a60/aries-daily-horoscope/", headers=headers)
        soup = BeautifulSoup(page.text, "html.parser")
        content = soup.find(class_="css-1nd4gv7 et3p2gv0")
        return (content)
    else:
        raise Exception ("Please enter one of the valid twelve starsigns")
    
main()