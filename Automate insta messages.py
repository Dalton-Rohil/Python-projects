# It is worth noting that automating Instagram in this way is against their terms of service and may result in
# your account being flagged or banned. Additionally, using this script could also be illegal in certain jurisdictions

from selenium import webdriver

# set up web driver
driver = webdriver.Chrome()
driver.get("https://www.instagram.com/")

# log in to Instagram
username_input = driver.find_element_by_xpath("//input[@name='username']")
password_input = driver.find_element_by_xpath("//input[@name='password']")
username_input.send_keys("your_username")
password_input.send_keys("your_password")
driver.find_element_by_xpath("//button[@type='submit']").click()

# navigate to the profile of the user you want to message
driver.get("https://www.instagram.com/username_of_person_you_want_to_message")

# click on the message button
driver.find_element_by_xpath("//button[contains(text(), 'Message')]").click()

# enter message
message_input = driver.find_element_by_xpath("//textarea[@placeholder='Message...']")
message_input.send_keys("Your message here.")

# click send button
driver.find_element_by_xpath("//button[contains(text(), 'Send')]").click()

# close driver
driver.close()
