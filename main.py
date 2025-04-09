import pyautogui
# First Step: Sync the Company’s Server
# https://dlp.hashtagtreinamentos.com/python/intensivao/login
  #Open the browser
pyautogui.PAUSE = 3
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.press("tab")
pyautogui.press("enter")
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')
pyautogui.press('tab')
pyautogui.press('enter')
pyautogui.write('dev')
pyautogui.press('tab')
pyautogui.write('gs12')
pyautogui.press('tab')
pyautogui.press('enter')