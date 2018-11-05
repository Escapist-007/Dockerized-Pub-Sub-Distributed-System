######  `MyWayPoints_v2` 
![](https://drive.google.com/uc?id=1Mlun5Opq_dVCkoU-1rNBYYeYUUS6oyiY)![](https://drive.google.com/uc?id=1zL0v6AUdw3YbLz7Mw8f0VNaH348_3xIg)



MyWayPoints is a distributed web application that provides users the weather information of cities along a route. This enhanced information will help them to prepare for their trip. When a user inputs 'Origin' and 'Destination' locations on this web app, they will get the optimized route along with some markers on the route. Every marker will represent a city on the route and show the real time weather information of that city. 

This is the version `02` of  MyWayPoints web application. In this version, I use a `database`, so all the repeated requests (same 'Origin' and 'Destination') are served from database. But the initial request is served by accessing the APIs. I use 2 API : [Google Map API](https://cloud.google.com/maps-platform/) for showing the route and [OpenWeather API](https://openweathermap.org/api) for showing the real time weather information of a city.


### Prerequisites

What things you need to run `MyWayPoints` from your pc/localhost.

```
 python 3.5.5
 Django 2.1.1
 googlemaps 3.0.2
 reverse_geocoder 1.5.1
 SQLite
```

Use [`pip`](https://pypi.org/project/pip/) to install these modules.
```
pip install django
pip install googlemap
pip install reverse_geocoder
```

### Installing
How you can run this django project `MyWayPoints_v2` is described below with necessary screenshots.

```
cd MyWayPoints
python manage.py runserver
```
The server will start in a few seconds with a **default url** : `http://127.0.0.1:8000`

A screenshot of these steps :
![](https://drive.google.com/uc?id=12Fma226Hl4rCUwwHlmDZ1JV3nfiVDmYt)

Next,
  - Go to the url : `http://127.0.0.1:8000/map/input`
  - Type `Origin` and `Destination` 
  - Press `Submit` button
  - See the `Route`
  - You will get two `buttons` on the left side of the screen.
  - Press `Show Way Poins` to see the markers
  - You will see all the `markers` along the route
  - Click a marker to show the weather information of that city
  - You will get the information in a window with a yellow marker


#### Screenshots of running MyWayPoints_v2:


**UI for taking inputs**

![](https://drive.google.com/uc?id=1ODL_M28QUog8h2phM6ODSqun6aQzgsN0)

**Initial Output with route**

The input was `buffalo`  to `rochester`.
![](https://drive.google.com/uc?id=13ZILjM3zn8NhGhFjxJIeq7Gokqnv3M5p)

The input was `buffalo`  to `nyc`.
![](https://drive.google.com/uc?id=13K-On_zUuhQC4H-437F9GS-dJMtKYrnd)

After pressing the button `Show Way Points`

![](https://drive.google.com/uc?id=1_m7VRtmWKBhfIijzn-5tr0CiobM6cVpY)

### Built With

* [Django](https://www.djangoproject.com/) - The web framework used
* [SQLite](https://www.sqlite.org/index.html) - Database 

### Authors

* **Md Moniruzzaman Monir**  
