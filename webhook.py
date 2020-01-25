import json
import os
import requests

from flask import Flask
from flask import request
from flask import make_response

from datetime import datetime


# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    print(json.dumps(req, indent=4))

    res = makeResponse(req)

    res = json.dumps(res, indent=4)
    # print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r


def makeResponse(req):
    # if req.get("result").get("action") != "fetchWeatherForecast":
    #     return {}
    result = req.get("queryResult")
    parameters = result.get("parameters")
    city = parameters.get("geo-city")
    date = parameters.get("date")
    # if city is None:
    #     return None
    # date = 'default_date'
    # city = 'default_city'
    # condition = 'default_condition'
    # r = requests.get(
    #     'http://api.openweathermap.org/data/2.5/forecast?q=' + city + '&appid=2160ae9f1b52eb8e94ff08940fccac75')
    # json_object = r.json()
    # weather = json_object['list']
    # date = date.strftime('%Y-%m-%d')
    condition = 'default condition'
    # for i in range(0, 30):
    #     if date in weather[i]['dt_txt']:
    #         condition = weather[i]['weather'][0]['description']
    #         break
    speech = "The forecast for" + city + "for " + date + " is " + condition
    return {
        "fulfillmentText": speech,
        "displayText": speech,
        "source": "apiai-weather-webhook"
    }


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    print("Starting app on port %d" % port)
    app.run(debug=False, port=port, host='0.0.0.0')

















