import urllib.request
import pandas as pd
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt


url = 'http://iszz.azo.hr/iskzl/rs/podatak/export/xml?postaja=160&polutant=5&tipPodatka=0&vrijemeOd=01.01.2017&vrijemeDo=31.12.2017'


airQualityHR = urllib.request.urlopen(url).read()
root = ET.fromstring(airQualityHR)

df = pd.DataFrame(columns=['mjerenje', 'vrijeme'])


for i, child in enumerate(root):
    obj = list(child)
    row = {
        'mjerenje': float(obj[0].text),
        'vrijeme': obj[2].text
    }
    df.loc[i] = row

df['vrijeme'] = pd.to_datetime(df['vrijeme'], utc=True)

top3 = df.sort_values(by='mjerenje', ascending=False).head(3)


print("Tri datuma s najvećom koncentracijom PM10 u 2017. godini za Osijek:")

print(top3[['vrijeme', 'mjerenje']])


df.plot(x='vrijeme', y='mjerenje', title='PM10 koncentracija u Osijeku (2017.)', ylabel='PM10 (µg/m³)')
plt.show()
