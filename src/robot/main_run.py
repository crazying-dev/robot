import json
import requests
import dotenv
import os

dotenv.load_dotenv()
session = requests.Session()
session.trust_env = False

def main(data):
	if not isinstance(data, dict):
		return "401 Error"
	
	code = data.get("code", None)
	
	if code is None:
		return "401 Error"
	
	if code == "h":
		return json.dumps([{"code":1, "meaasge":"get weather"}])
	
	if code == "1":
		return requests.get(f"https://restapi.amap.com/v3/weather/weatherInfo?key={os.getenv('GAODE')}&city=100000").text
	
	return "401 Error"
