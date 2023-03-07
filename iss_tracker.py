# Daniela Sanchez, dls4848

import requests
import math
import xmltodict

from flask import Flask, request

app = Flask(__name__)

# making data set a global variable
data = {}
information = {}

def get_data():
    '''
    This function will get the data set and make it a dictionary that will be called in other functions.
    '''
    global data
    global information
    data_url = "https://nasa-public-data.s3.amazonaws.com/iss-coords/current/ISS_OEM/ISS.OEM_J2K_EPH.xml"
    response = requests.get(data_url)
    information = xmltodict.parse(response.text)
    data = information['ndm']['oem']['body']['segment']['data']['stateVector']


@app.route('/', methods=['GET'])
def get_entire_data_set():
    '''
    This function will print the entire data set when the user simply uses a back slash '/'
    '''
    return data


@app.route('/epochs', methods=['GET'])
def get_all_epochs():
    '''
    This function will print a list of all of the epochs in the data set when the user types '/epochs' and will return a modified
    version of the list if the user uses query parameters.

    Returns:
        list_of_epochs (list): This is the list of all of the epochs in the data set
    '''
    maximum = len(data) 
    list_of_epochs = []
    lim = request.args.get('limit', maximum)
    if lim:
        try:
            lim = int(lim)
        except ValueError:
            return "Invalid limit paramter", 400

    offset = request.args.get('offset', 0)
    if offset:
        try:
            offset = int(offset)
        except ValueError:
            return "invalid offset parameter", 400

    count = lim
    for i in range(maximum):
        if len(list_of_epochs) == lim:
            break
        if i >= offset:
            list_of_epochs.append(data[i]['EPOCH'])
    return list_of_epochs



@app.route('/epochs/<epoch>', methods=['GET'])
def get_specif_epoch(epoch):
    '''
    This function will print a the info for a user specified epoch.
    Args:
        epoch: This is the specific epoch that is entered by the user. Will go after a back slash

    Returns:
        stateVector: This is the dict of info for a specific epoch.
    '''
    for stateVector in data:
        if epoch == stateVector["EPOCH"]:
            return stateVector



@app.route('/epochs/<epoch>/speed', methods=['GET'])
def get_speed_for_specif_epoch(epoch):
    '''
    This function will print the speed for the specific epoch specified. The units for the speed are calculated and printed as
    well. The formula to caluclate was provided by COE332 professors.

    Args:
        epoch: This is the specific epoch from the data set that will be used in this function

    Returns:
        speed(float): This is the speed for the specific epoch.
    '''
    for stateVector in data:
        if epoch == stateVector["EPOCH"]:


            # initializing _dot values
            x_dot = stateVector['X_DOT']['#text']
            y_dot = stateVector['Y_DOT']['#text']
            z_dot = stateVector['Z_DOT']['#text']

            # type casting the values into floats
            x_dot = float(x_dot)
            y_dot = float(y_dot)
            z_dot = float(z_dot)



            # using formula provided to calculate speed
            calculate = (x_dot*x_dot)+(y_dot*y_dot)+(z_dot*z_dot)
            speed = math.sqrt(calculate)
            units = stateVector['X_DOT']['@units']
            return (f'speed: {str(speed)} {units}')



@app.route('/epochs/<epoch>/location', methods=['GET'])
def get_epoch_location(epoch):
    '''
    This function/route takes a specific epoch from the user and returns the location of the iss during that interval.

    Args:
        epoch : the specific epoch input by the user

    Returns:
        location (string): the location of the iss during the epoch interval.
    '''
    for stateVector in data:
        if epoch == stateVector["EPOCH"]:

            # calcualate location of the specific epoch


            return location



@app.route('/now', methods=['GET'])
def get_now():
    '''
    This function/route will return the latitude, longitude, geoposition, and the altitude of the iss at the current moment.
    '''




@app.route('/help', methods=['GET'])
def help_message():
    '''
    This function will return a help menu with all available user options/routes and small descriptions.

    Returns:
        This function will return a help menu in string form.
    '''
    help_string = "Help Menu: Below are all of the possible commands/routes and a brief description:\n"
    string1 = ("/ : returns entire data set\n")
    string2 = ("/epochs : returns list of ALL epochs in data set\n")
    string3 = ("/epochs?limit=int&offset=int : returns list of epochs with user specified parameters\n")
    string4 = ("/epochs/<epoch> : returns user specified epoch\n")
    string5 = ("/epcohs/<epochs>/speed : returns speed of user specified epoch\n")
    string6 = ("/help : returns help menu\n")
    string7 = ("/delete-data : will delete entire data set\n")
    string8 = ("/post-data : will reload the dictionary object with data from the web\n")
    string9 = ("/comment : returns all the comments in the data set\n")
    string10 = ("/header : returns the headers in the data set\n")
    string11 = ("/metadata : returnd all of the metadata in the data set\n")
    string12 = ("/epochs/<epoch>/location : returns the location of the specified epoch\n")
    string13 = ("/now : returns the logitude, latitude, altitude, and geoposition of the specified epoch at the current time\n")

    return help_string + string1 + string2 + string3 + string4 + string5 + string6 + string7 + string8 + string9\
            + string10 + string11 + string12 + string13


@app.route('/comment', methods=['GET'])
def get_comment():
    '''
    This function/route returns the comments in the data set.
    '''
    comment = information['ndm']['oem']['body']['segment']['data']['COMMENT']
    return comment



@app.route('/header', methods=['GET'])
def get_header():
    '''
    This function/route prints the headers in the data set.
    '''
    header = information['ndm']['oem']['header']
    return header



@app.route('/metadata', methods=['GET'])
def get_metadata():
    '''
    This function/route will print all of the metadata in the data set.
    '''
    metadata = information['ndm']['oem']['body']['segment']['metadata']
    return metadata



@app.route('/delete-data', methods=['DELETE'])
def delete_all_data():
    '''
    This function uses the delete method to delete all of the data. It will return a delete message.
    '''
    global data
    data.clear()
    return 'The data has been successfully deleted!!\n'



@app.route('/post-data', methods=['POST'])
def post_data() -> str:
    '''
    This function will reload the dictionary with data from the web. It will return a message when the data is reloaded.

    Returns:
        data (dict): this is the entire updated data set
    '''
    global data
    get_data()
    return 'The data has been successfully reloaded!!\n'


# main function: this will load the data globally upon the initiation of the flask app and the then run the routes.
if __name__ == '__main__':
    get_data()
    app.run(debug=True, host='0.0.0.0') 



