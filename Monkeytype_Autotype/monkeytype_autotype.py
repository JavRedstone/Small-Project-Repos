import pyautogui;
import time;

words = input("Enter your console log: ");

time.sleep(3);

pyautogui.write(words, interval = 0.01)