import requests
import string
from bs4 import BeautifulSoup
from datetime import date

### entering starsign
### if people don't know their sign, have them enter their date of birth to be given it

HEADERS = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
PAGE = requests.get("https://www.elle.com/horoscopes/daily/a104/scorpio-daily-horoscope/", headers=HEADERS)
SOUP = BeautifulSoup(PAGE.text, "html.parser")
content = SOUP.find_all(class_="css-1wfsl5s et3p2gv0")

def main():
    starsign = get_starsign()
    get_date(starsign)
    # get_horoscope(starsign)
    
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


def get_horoscope(starsign):
    headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
    if starsign == "aquarius":
        url = "https://www.elle.com/horoscopes/daily/a107/aquarius-daily-horoscope/"
        return (url)
        
    page = requests.get(f"https://www.elle.com/horoscopes/daily/a104/{starsign}-daily-horoscope/", headers=headers)
    soup = BeautifulSoup(page.text, "html.parser")
    content_elements = soup.find_all(class_="css-1nd4gv7 et3p2gv0")
    for content in content_elements:
        horoscope_text = content.text.strip()
        if "See All Signs" not in horoscope_text:
            print (horoscope_text)
    
    print ("---------------------------------------------------------------------------------------------------------------------------------")
    





main()