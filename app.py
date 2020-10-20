from selenium import webdriver
import time
import urllib
import random
import os
from flask import Flask, jsonify, render_template


app = Flask(__name__)


@app.route("/")
def home():
	return render_template("index.html")

@app.route("/api/1")
def got():
	d = getData(0)
	return jsonify({"result":d})

@app.route("/api/2")
def got2():
	d = getData(12)
	return jsonify({"result":d})

@app.route("/api/3")
def got3():
	d = getData(24)
	return jsonify({"result":d})

@app.route("/api/4")
def got4():
	d = getData(36)
	return jsonify({"result":d})

@app.route("/api/5")
def got5():
	d = getData(48)
	return jsonify({"result":d})

@app.route("/api/6")
def got6():
	d = getData(60)
	return jsonify({"result":d})

@app.route("/api/7")
def got7():
	d = getData(72)
	return jsonify({"result":d})

@app.route("/api/8")
def got8():
	d = getData(84)
	return jsonify({"result":d})

@app.route("/api/9")
def got9():
	d = getData(96)
	return jsonify({"result":d})

@app.route("/api/10")
def got10():
	d = getData(108)
	return jsonify({"result":d})

@app.route("/api/11")
def got11():
	d = getData(120)
	return jsonify({"result":d})

@app.route("/api/12")
def got12():
	d = getData(132)
	return jsonify({"result":d})

@app.route("/api/13")
def got13():
	d = getData(144)
	return jsonify({"result":d})

@app.route("/api/14")
def got14():
	d = getData(156)
	return jsonify({"result":d})

@app.route("/api/15")
def got15():
	d = getData(168)
	return jsonify({"result":d})

@app.route("/api/16")
def got16():
	d = getData(180)
	return jsonify({"result":d})

@app.route("/api/17")
def got17():
	d = g1etData(192)
	return jsonify({"result":d})

@app.route("/api/18")
def got18():
	d = getData(204)
	return jsonify({"result":d})

@app.route("/api/19")
def got19():
	d = g1etData(216)
	return jsonify({"result":d})

@app.route("/api/20")
def got20():
	d = getData(228)
	return jsonify({"result":d})

def getData(page):
	chrome_options = webdriver.ChromeOptions()
	chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
	chrome_options.add_argument("--headless")
	chrome_options.add_argument("--disable-dev-shm-usage")
	chrome_options.add_argument("--no-sandbox")
	driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

	driver.get("https://mbasic.facebook.com/login/")
	time.sleep(3)
	username = driver.find_element_by_id('m_login_email')
	password = driver.find_element_by_xpath('//*[@name="pass"]')
	button = driver.find_element_by_xpath("//*[@name='login']")
	username.send_keys("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
	time.sleep(2)
	password.send_keys("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
	time.sleep(2)
	button.click()
	time.sleep(2)
	driver.get("https://mbasic.facebook.com/AizaKhanActress/photos")
	driver.find_elements_by_partial_link_text("See All")[0].click()
	link = driver.find_element_by_link_text("See more photos").get_attribute("href")
	data_links = []
	try:
	    print(f"Scrapping Links From Page.....")
	    link = link.replace("offset=12",f"offset={page}")
	    driver.get(link)
	    images = driver.find_elements_by_tag_name("a")
	    for i in images[2:-1]:
	    	data_links.append(i.get_attribute("href"))
	except:
		pass
	images = []
	count = 0
	for i in data_links:
	  try:
	    driver.get(i)
	    img = driver.find_element_by_partial_link_text("View full size").get_attribute("href")
	    count += 1
	    print("Scrapping Image Number {}".format(count))
	    images.append(img)
	  except:
	    pass
	number = 0
	data = []
	for im in images:
	  number += 1
	  data.append({
	      "id":number,
	      "photo": im
	  })
	return data

if __name__ == "__main__":
	app.run(debug=True)
