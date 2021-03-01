from selenium import webdriver

chromeBrowser = webdriver.Chrome('./chromedriver.exe')

chromeBrowser.maximize_window()

chromeBrowser.get('https://www.jetpunk.com/quizzes/fast-typing-to-hundred-quiz')

pressButton = chromeBrowser.find_element_by_id('start-button')
pressButton.click()

messageWriting = chromeBrowser.find_element_by_id('txt-answer-box')
messageWriting.clear()

for num in range(1, 101):
    messageWriting.send_keys(str(num))