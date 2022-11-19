#Türkçe sözlük
import requests as req
from bs4 import BeautifulSoup
from os  import system


while True:
    system("cls||clear")
    kelime= input("********************\nKelimeyi giriniz :")
    kelime_ara=req.get(f"http://www.birsozluk.com/{kelime}")
    if len(kelime)<=1:
        input("Daha uzun bi kelime giriniz! Tekrar denemek için boşluk tuşuna basınız!")
        continue

    kaynak = BeautifulSoup(kelime_ara.content,"html.parser")
    span = kaynak.find("table")
    sonuc = list(span.stripped_strings)
    
    if sonuc[3] == "Bilgi yarışması":
        print("\nAradığınız kelime kayıtlarımızda mevcut değil yada hatalı bir kelime girdiniz!")
    else:
        print(f"""\n************* Kelime anlamı *************\n
{"-"*40}\nArama yapılan kelime : {kelime}
Anlam : {sonuc[3][:-1]}\n{"-"*40}
""")
        
    input("\nYeni kelime aramak için boşluk tuşuna basın...")
