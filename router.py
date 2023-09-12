# code using with request argument.
from flask import Flask, request, jsonify
from database_manager import get_query_data, get_query_devices,get_query_services, get_query_data_by_service
from flask_cors import CORS
import datetime

app = Flask(__name__)
CORS(app, resources={r"/data_devices": {"origins": "http://localhost:3000"},
                     r"/data_services": {"origins": "http://localhost:3000"},
                     r"/query_devices": {"origins": "http://localhost:3000"},
                     r"/query_services": {"origins": "http://localhost:3000"}})

@app.route('/data_devices')
def data_devices():
    deviceId = request.args.get('item')
    periodicity = request.args.get('periodicity')
    shift = request.args.get('shift')
    day = request.args.get('day')  # Extract 'day' query parameter
    week = request.args.get('week')  # Extract 'week' query parameter
    month = request.args.get('month')  # Extract 'month' query parameter
    year = request.args.get('year')  # Extract 'year' query parameter

    

    if deviceId is None or periodicity is None or shift is None or day is None or week is None or month is None or year is None:
        print("no complete query")
        return '<h1> incomplete query :( </h1>'
    else:
        day = int(day)
        week = int(week)
        month = int(month)
        year = int(year)

        week = datetime.date(year, month, day)
        week = week.isocalendar()[1]
        week = int(week)
        
        print('DEVICE QUERY PARAMS')
        print(deviceId, periodicity, shift, day, week, month, year)
        data = get_query_data(deviceId, periodicity, shift, day, week, month, year)
        # print(data)
        return jsonify(data)
    
@app.route('/data_services')
def data_services():
    service = request.args.get('item')
    periodicity = request.args.get('periodicity')
    shift = request.args.get('shift')
    day = request.args.get('day')  # Extract 'day' query parameter
    week = request.args.get('week')  # Extract 'week' query parameter
    month = request.args.get('month')  # Extract 'month' query parameter
    year = request.args.get('year')  # Extract 'year' query parameter
    

    if service is None or periodicity is None or shift is None or day is None or week is None or month is None or year is None:
        print("no complete query")
        return '<h1> incomplete query :( </h1>'
    else:
        day = int(day)
        week = int(week)
        month = int(month)
        year = int(year)
        
        week = datetime.date(year, month, day)
        week = week.isocalendar()[1]

        print('<<<<<<<<<<<<<<<<QUERY DATA>>>>>>>>>>>>>>><')
        print(service, periodicity, shift, day, week, month, year)
        
        data = get_query_data_by_service(service, periodicity, shift, day, week, month, year)
        # print(data)
        return jsonify(data)

# ////////////////////////////////////////////////////
@app.route('/query_devices')
def query_devices():
    print('on query devices')
    devices = get_query_devices(True)
    print(devices)
    return jsonify(devices)
# //////////////////////////////////////////

@app.route('/query_services')
def query_services():
    print('on query services')
    services = get_query_services(True)

    print(services)

    return jsonify(services)


if __name__ == '__main__':
    app.run(debug=True, port=5500)