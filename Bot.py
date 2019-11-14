from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://web.whatsapp.com")
host_name = input("Enter the Target Name: ")
message = input("Enter the Message to be send: ")
number = int(input("Enter the Number of message to be send: "))

input("Enter anything after Scanning QRcode...")

user = driver.find_element_by_xpath(f"//span[@title='{host_name}']")
user.click()

message_box = driver.find_elements_by_class_name('_3u328')[0]
# print("Message box")
# print(message_box)
for i in range(number):
    message_box.send_keys(message)
    button = driver.find_elements_by_class_name('_3M-N-')[0]
    # print("Button Details: ")
    # print(button)
    button.click()

driver.close()