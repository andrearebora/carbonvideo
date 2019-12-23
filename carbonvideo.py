'''
carbonvideo
Created by Andrea Rebora (@AndreaRebora01)
'''

import webbrowser, requests
from bs4 import BeautifulSoup

print("""     
                                   ___.                       .__    .___            
                  ____    __  _____\_ |__    ____   _______  _|__| __| _/____  ___  
                _/ ___/  /__\ \_  __ \ __ \ /    \ /    \  \/ /  |/ __ |/ __ \/   \ 
                \  \___ / __ \ |  | \/ \_\ (  <>  )   |  \   /|  / /_/ \  ___(  <> )
                 \_____/_/  \_\|__|  |_____/\____/|___|__/\_/ |__\_____|\_____\___/ 
                                                                
 """)

input_func = None
try:
    input_func = raw_input('What video, user, or YouTube channel are you looking for? ')
except NameError:
    input_func = input('What video, user, or YouTube channel are you looking for? ')
query = input_func.replace(' ', '+')
url = 'https://www.youtube.com/results?search_query=' + query
source_code = requests.get(url, timeout=20)
plain_text = source_code.text
soup = BeautifulSoup(plain_text, "html.parser")
videos = soup.findAll('div', {'class': 'yt-lockup-video'})
video = videos[0].contents[0].contents[0].contents[0]
try:
    link = video['href']
    webbrowser.open('https://www.youtube.com/user/' + query) + webbrowser.open('https://www.youtube.com/' + link) + webbrowser.open('https://www.youtube.com/channel/' + query)
except KeyError:
    print("No results found")
