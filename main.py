import requests
from ms_graph import generate_access_token, GRAPH_API_ENDPOINT

APP_ID = '2a0af66b-8482-4e97-86b3-23c7bfda0014'
SCOPES = ['Files.ReadWrite']
#folder_id = '%2Fpersonal%2Fdavid_bonilla_cfe_mx%2FDocuments%2Fprueba_csv'

access_token = generate_access_token(APP_ID, SCOPES)
headers = {
    'Authorization': 'Bearer ' + access_token['access_token']
}

#Step 2 Upload

download_link = 'https://query1.finance.yahoo.com/v7/finance/download/META?period1=1644494641&period2=1676030641&interval=1d&events=history&includeAdjustedClose=true'
folder_id = '71C251BC9BB804E0%21165'
headers['Prefer'] = 'respond-async'
request_body = {
    '@microsoft.graph.sourceUrl': download_link,
    'name':'Hola Yei Cruz.csv',
    'file': {}
}

response = requests.post(
    GRAPH_API_ENDPOINT + f'/me/drive/items/{folder_id}/children',
    headers=headers,
    json=request_body
)

if response.status_code == 202:
    print(response.reason)
else:
    print(response.json())

#------------------------SELENIUM------------------------------
#import time
#from selenium import webdriver
from selenium.webdriver.common.by import By #Libreria para referenciar el elemento dentro de la web
from selenium.webdriver.common.keys import Keys

#driver = webdriver.Chrome()

#-------------------------GOOGLE------------------------------
#driver.get("https://www.google.com/")
#web_element = driver.find_element(By.NAME, 'q')
#web_element.send_keys("Imagenes de gatitos" + Keys.ENTER)

#--------------------------MOODLE-----------------------------
#driver.get("https://moodle2.cucei.udg.mx/login/index.php")
#driver.find_element(By.NAME, 'username').send_keys("214791647")
#driver.find_element(By.NAME, 'password').send_keys("Sonrics1999,")
#driver.find_element(By.ID, 'loginbtn').click()
#Tambien es valido en moodle...
#driver.find_element(By.NAME, 'password').send_keys("Sonrics1999," + Keys.ENTER)

#-------------------------ONEDRIVE-------------------------


#time.sleep(2)
