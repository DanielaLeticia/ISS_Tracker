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
this project. It is a plain text file that when working on conjunction with the docker-compose, will execute the iss tracker file 
and will be able to be interacted with. The Dockerfile will pip install all of the non-standard python libraries included in this
project. Some of them include, geopy, requests, xmltodict, and Flask. These are located at the top of the script. The next thing
included in the Dockerfile is the CMD command. This acts as the command line and will execute the string of commands in the CMD
line. In this case, to run the flask app, all we need to write in `python3 iss_tracker.py` so the CMD command in this script is
just that but in string form. The final command in the Dockerfile is the COPY command. This is another way of "importing" the
file/script that we are going to be using, in this case, the iss tracker script. This command is usually found after the RUN 
command and before the CMD command. It is important to note that the sequence of these commands is not by accident. The file is
executed in order from top to bottom, so the order of the commands matters. First, we use python, then pip install all the 
nesseccary libraries, then copy the file to be executed, and finally, execute the file. 


## docker-compose.yml script

This script will automate the launch of the dockerfile and the flask app. Since our program is not too complicated and does not
have a lot of moving peices, the docker-compose file is pretty simple. It is building the docker image by using the context
in the DOckerfile. This is what the ./Dockerfile command is. It also takes in the ports that docker-compose will use to build
the image. In this case, we are using a local port in our personal virtual machines so the port will simply be 5000. The 
command in the docker-compose file is -5000:5000. Lastly, it will create the image and its name. The script has the unsername
associated with DockerHub and the name of the file/image, which is iss_tracker.py. Since our program is only running one
container, there is no need for a docker-config file which is why the volume section and the config file is commented out. If
users of the program add to it and make it will more moving pieces, it would be customary to add a config.yml file to the 
program folder.  




