from flask import Flask
from flask import request
import datetime

app = Flask(__name__)


import model
import logic

_event_logic = logic.EventLogic()

class ApiException(Exception):
    pass

def check_data(data: dict, _id = None, change_date: bool = False, change_body: bool = False) -> model.Event:
    year = int(data.get('year'))
    month = int(data.get('month'))
    day = int(data.get('day'))
    try:
        date = datetime.date(year=year, month=month, day=day)
    except:
        raise ApiException('Invalid date format')
    event = model.Event()
    events = _event_logic.list()

    if ((change_date == False and change_body == False) or
            (change_date == True and change_body == True) or
            (change_date == True and change_body == False)):
        for item in events:
            if item.date == date:
                raise ApiException('An event has already been scheduled for the specified date')
    elif change_body == True and change_date == False:
        pass


    if _id == None:
        event.id = None
    else:
        event.id = _id
    event.date = date
    event.title = data.get('title')
    event.text = data.get('text')
    return event

def dict_data(data):
    try:
        dict_data = {}
        dict_data['id'] = data.id
        dict_data['date'] = data.date
        dict_data['title'] =data.title
        dict_data['text'] = data.text
        return dict_data
    except:
        raise ApiException('Invalid date format')

API_ROOT = "/api/v1"
EVENT_API_ROOT = API_ROOT + "/event"


@app.route(EVENT_API_ROOT + "/", methods=["POST"])
def create():
    try:
        year = request.form.get('year')
        month = request.form.get("month")
        day = request.form.get("day")
        title = request.form.get('title')
        text = request.form.get('text')
        data = {'year': year,
                 'month': month,
                 'day': day,
                 'title': title,
                 'text': text}
        validate_data = check_data(data)
        event = _event_logic.create(validate_data)
        return f"new id: {event}", 201
    except Exception as ex:
        return f"failed to CREATE with: {ex}", 404


@app.route(EVENT_API_ROOT + "/", methods=["GET"])
def list():
    try:
        events = _event_logic.list()
        for i in range(len(events)):
            events[i] = dict_data(events[i])
        return events, 200
    except Exception as ex:
        return f"failed to LIST with: {ex}", 404


@app.route(EVENT_API_ROOT + "/<_id>/", methods=["GET"])
def read(_id: str):
    try:
        event = _event_logic.read(_id)
        event = dict_data(event)
        return event, 200
    except Exception as ex:
        return f"failed to READ with: {ex}", 404


@app.route(EVENT_API_ROOT + "/<_id>/", methods=["PUT"])
def update(_id: str):
    try:
        data = {'year': request.form.get("year"),
                 'month': request.form.get("month"),
                 'day': request.form.get("day"),
                 'title': request.form.get("title"),
                 'text': request.form.get("text")}
        change_date = False
        change_body = False
        old_evnt = _event_logic.read(_id)
        # проверка на смену даты ивента
        if data['year'] == None and data['month'] == None and data['day'] == None:
            data['year'] = old_evnt['year']
            data['month'] = old_evnt['month']
            data['day'] = old_evnt['day']
            change_date = False
        elif data['year'] == None and data['month'] == None:
            data['year'] = old_evnt['year']
            data['month'] = old_evnt['month']
            change_date = True
        elif data['year'] == None:
            data['year'] = old_evnt['year']
            change_date = True
        else:
            pass

        # проверка на смену содержимого ивента
        if data['title'] == None and data['text'] == None:
            data['title'] = old_evnt['title']
            data['text'] = old_evnt['text']
            change_body = False
        elif data['title'] == None:
            data['title'] = old_evnt['title']
            change_body = True
        elif data['text'] == None:
            data['text'] = old_evnt['text']
            change_body = True
        else:
            pass
        validate_data = check_data(data, _id, change_date, change_body)
        _event_logic.update(_id, validate_data)
        return "updated", 200
    except Exception as ex:
        return f"failed to UPDATE with: {ex}", 404


@app.route(EVENT_API_ROOT + "/<_id>/", methods=["DELETE"])
def delete(_id: str):
    try:
        _event_logic.delete(_id)
        return "deleted", 200
    except Exception as ex:
        return f"failed to DELETE with: {ex}", 404
