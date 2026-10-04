import json
import requests
import dotenv
import os

dotenv.load_dotenv()

def main(data):
	if not isinstance(data, dict):
		return "401 Error"
	
	code = data.get("code", None)
	
	if code is None:
		return "401 Error"
	
	if code == "h":
		return json.dumps([{"code":1, "meaasge":"get weather"}])
	
	if code == "1":
		requests.get(f"https://restapi.amap.com/v3/weather/weatherInfo?key={os.getenv('GAODE')}&city=100000")
	
	return "401 Eooror"
