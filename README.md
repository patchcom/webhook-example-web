## Sample App to save webhook data from PATCH SERVER (For Call Data)
- The objective of this app is to demonstrate a sample webhook capture request. 
- A webhook (also called a web callback or HTTP push API) is a way for an app to provide other applications with real-time information. A webhook delivers data to other applications as it happens, meaning you get data immediately.


## Running the application 
- Clone the repo on your system
- For e.g sake we are using `sqlite3` as the database but you can configure other db's also
- Once you've cloned the repo, activate your `virtualenv`
- Install `pip install -r requirements/requirements-dev.txt` file while you are in dev mode
- Once the setup is completed, run migration `python manage.py migrate`.
- Once this is done create superuser : `python manage.py createsuperuser`
- Run the app : `python manage.py runserver` 

## Sample Endpoint : 

- The app has a sample endpoint at 
```
/api/callback_url
```

### Type of Request : Only POST METHOD ALLOWED

### Sample DATA : 

```
{
 "startedAt": "2018-12-19T10:17:59.387Z",
 "endedAt": "2018-12-19T10:18:08.039Z",
 "duration": 9,
 "cost": 350,
 "context": "Test Call",
 "tags": [],
 "from": {
 "cc": "91",
 "phone": "1231231230",
 "name": "Smart"
 },
 "type": "mixed",
 "status": "over",
 "legs": [
 {
 "duration": 9,
 "startedAt": "2018-12-19T10:17:59.387Z",
 "endedAt": "2018-12-19T10:18:08.172Z",
 "type": "voip",
 "contact": {
 "name": "Smart",
 "cc": "91",
 "phone": "1231231230",
 "platform": "web"
 },
 "cost": 300
 },
 {
 "duration": 6,
 "startedAt": "2018-12-19T10:18:02.970Z",
 "endedAt": "2018-12-19T10:18:08.039Z",
 "type": "pstn",
 "contact": {
 "name": "Demo",
 "cc": "91",
 "phone": "2342342348",
 "platform": "web"
 },
 "cost": 50
 }
 ],
 "webhook": "https://abc.com",
 "to": {
 "name": "Demo",
 "cc": "91",
 "phone": "2342342348"
 },
 "var1": "Test",
 "var2": "Test2",
 "recording": "ffefe.wav"
}
```


### Response Code for Success : 201 Success OK
### Response Code for Failure : 400 BAD REQUEST
### For other methods : 405 [GET, PUT, PATCH, DELETE] not allowed


## Test Suite : 
- The app contains the test suite as well. 
- Contains sample test for the function and integration tests as well

## FOR PRODUCTION : In case you want to use this app in production make sure you have prod related dependencies installed and your keys and secrets are in an `.env` file. 


# GOLDEN RULE : ANYTHING IN MASTER SHOULD BE ALWAYS DEPLOYABLE
