from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

driver = webdriver.Chrome()

driver.get("https://www.timeanddate.com/weather/malaysia/penang/hourly")

driver.implicitly_wait(0.5)

weather = driver.find_elements(By.XPATH, '//tbody/tr')

time = []   
temp = []
desc = []
feel = []
wind = []
humidity = []
p_chance = []
p_amount = []

print(weather)

for i in weather:
    time.append(i.find_element(By.XPATH, "./th").text)
    temp.append(i.find_element(By.XPATH, "./td[2]").text)
    desc.append(i.find_element(By.XPATH, "./td[3]").text)
    feel.append(i.find_element(By.XPATH, "./td[4]").text)
    wind.append(i.find_element(By.XPATH, "./td[5]").text)
    humidity.append(i.find_element(By.XPATH, "./td[7]").text)
    p_chance.append(i.find_element(By.XPATH, "./td[8]").text)
    p_amount.append(i.find_element(By.XPATH, "./td[9]").text)
    
df = pd.DataFrame({'Time': time, 'Temperature': temp, 'Description': desc, 'Feels like': feel, 'Wind': wind, 
'Wind': wind, 'Humidity': humidity, 'Percipitation Chance': p_chance, "Percipitation Amount": p_amount})
df.to_csv('weather_forecast_penang.csv', index=False)
print(df)
print("\nData is successfully exported to csv.")

