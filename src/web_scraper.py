import requests
from bs4 import BeautifulSoup

def get_bay_temps(url):
  response = requests.get(url)
  if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    temp_data = soup.find('td', class_='intd')
    if temp_data:
      temperature_text = temp_data.get_text(strip=True)
      top_bay_temp = temperature_text.split('Top Bay: ')[1].split('℃')[0]
      mid_bay_temp = temperature_text.split('Mid Bay: ')[1].split('℃')[0]
      bottom_bay_temp = temperature_text.split('Bottom Bay: ')[1].split('℃')[0]
      ocean_temp = temperature_text.split('Ocean: ')[1].split('℃')[0]
      return {
        'Top Bay': top_bay_temp,
        'Mid Bay': mid_bay_temp,
        'Bottom Bay': bottom_bay_temp,
        'Ocean': ocean_temp
      }
  return None
