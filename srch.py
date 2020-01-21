import pyautogui
import pyperclip
import time
import os

string = input("Enter the text you want to search : ")


def search():
	pyperclip.copy(string)
	os.startfile("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
	time.sleep(2)
	pyautogui.hotkey('ctrl','k')
	pyautogui.hotkey('ctrl','v')
	pyautogui.hotkey('enter')
	pyautogui.click()


search()
