# International Space Station Tracker 

This project file containes scripts and containerization files that will run a program that can be used to track the international
space station. This project uses concepts of flask, flask applicaitons, and docker to run.

---

## iss_tracker.py script

This is the main script in the project. It runs a flask app with different routes that will return different information 
specified by the user. The various routes are specified below:

| Route | Method | Description |
| ----- | ----- | ----- |
| `/help` | GET | help menu with all available routes |
| `/` | GET | returns entire data set |
| `/epochs` | GET | returns list of all epochs in data set |
| `/epochs?limit=int&offset=int` | GET | returns list of epochs with given query parameters |
| `/epochs/<epoch>` | GET | returns all state vectors for a specified epoch |
| `/epochs/<epoch>/speed` | GET | returns the speed of the iss for a specified epoch |
| `/epochs/<epoch>/location` | GET | returns the location of the iss for a specified epoch |
| `/now` | GET | returns the logitude, latitude, altitude, and geopositon of the iss at the current time |
| `/comment` | GET | returns all of the comments in the data set |
| `/header` | GET | returns all of the headers in the data set |
| `/metadata` | GET | returns all of the metadata in the data set |
| `/delete-data` | DELETE | deletes all of the data set |
| `/post-data` | POST | reloads the data set with data from the web |

To run the flask app, run the following command in one terminal in the same folder as the iss_tracker script:
`flask --app iss_tracker --debug run`. The command is successful and the app is running when terminal displays 'Debugger is active!'.
This window will show the behind the scenes of the commands that you run and will show error codes in the event that the program
fails. In another terminal window, run the following command in the same folder as the script to interact with the flask app:
`curl localhost:5000`. This is the base command. You can interact with the app more closely by adding any of the routes specified
in the table above. If at any point you would like to see all of the routes in the terminal or while running the app, run the 
following command: `curl localhost:5000/help`. 


## Dockerfile script

The Dockerfile script is a containerization tool that is used for the project in order to make it easier to package and release
this project. 


## docker-compose.yml script

This script will automate the launch of the dockerfile and the flask app.  




