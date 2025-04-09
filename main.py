import pyautogui
import time
import pandas as pd
# First Step: Sync the Company’s Server
#https://dlp.hashtagtreinamentos.com/python/intensivao/login
#Open the browser
pyautogui.PAUSE = 2
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.press("tab")
#Open Company Site
pyautogui.press("enter")
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')
time.sleep(3) #Give some delay secs
#Registration 
pyautogui.press('tab')
pyautogui.write('dev')
pyautogui.press('tab')
pyautogui.write('gs12')
pyautogui.press('tab')
pyautogui.press('enter')
#Import DataBase
pd.read_csv("products.csv")
table = pd.read_csv("products.csv")

#Regist each product inside the for loop
for row in table.index: 
  pyautogui.click(x=653, y=310)
  codigo = table.loc[row, "codigo"]
  pyautogui.write(str(codigo))
  pyautogui.press('tab')
  marca = table.loc[row, "marca"]
  pyautogui.write(str(marca))
  pyautogui.press('tab')
  tipo = table.loc[row, "tipo"]
  pyautogui.write(str(tipo))
  pyautogui.press('tab')
  categoria = table.loc[row, "categoria"]
  pyautogui.write(str(categoria))
  pyautogui.press('tab')
  preco_unitario = table.loc[row, "preco_unitario"]
  pyautogui.write(str(preco_unitario))
  pyautogui.press('tab')
  custo = table.loc[row, "custo"]
  pyautogui.write(str(custo))
  pyautogui.press('tab')
  obs = table.loc[row, "obs"] 
  if not pd.isna(obs):
    pyautogui.write(str(table.loc[row, "obs"]))
  pyautogui.press("tab")
  pyautogui.press("enter")
  pyautogui.press("home")