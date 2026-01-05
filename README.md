# AtmosQuery-weather-dashboard
Self host your own weather application, without the ads, and junk. Customize it to get the info you want, when you want.
____
## ABOUT

API service provided by [WeatherAPI.com](https://www.WeatherAPI.com)

Icons Provided by [erikflowers-weather-icons](https://erikflowers.github.io/weather-icons/)

## How to set up on your device.

1. Aqquire a personal API key from WeatherAPI
if you are running this locally, you can simply copy and paste your api key, in the following line in "app.py"

```python

from dotenv import load_dotenv # <- DELETE THIS 
load_dotenv() #<- DELETE THIS

#CHANGE THIS LINE
API_KEY = os.getenv("API_KEY")

#TO THIS
API_KEY = "paste your key here"
```

2. Ensure you have the requirements

you may like to copy and paste the following into your terminal

