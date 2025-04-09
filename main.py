import pyautogui
import pandas
# First Step: Sync the Company’s Server
# https://dlp.hashtagtreinamentos.com/python/intensivao/login
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
#Registration 
pyautogui.press('tab')
pyautogui.write('dev')
pyautogui.press('tab')
pyautogui.write('gs12')
pyautogui.press('tab')
pyautogui.press('enter')
#Import DataBase
pandas.read_csv("products.csv")
tabela = pandas.read_csv("products.csv")
print(tabela)