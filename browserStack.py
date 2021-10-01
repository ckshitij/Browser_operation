from flask import Flask, request
import os

app = Flask(__name__)

def is_supported_browser(browser_type):
    browser_type = browser_type.lower()
    if(browser_type == 'chrome' or browser_type == 'firefox'):
        return True
    return False

def get_browser_path(browser_type):
    if(browser_type == 'chrome'):
        return "google-chrome"
    elif(browser_type == 'firefox'):
        return "firefox"

def get_cache_path(browser_type):
    if(browser_type == 'chrome'):
        return "/home/ckshitij/.config/google-chrome"
    elif(browser_type == 'firefox'):
        return "/home/ckshitij/.mozilla/firefox"
        

@app.route("/start", methods = ['GET'])
def get_browser_instance():

    browser_type = request.args.get('browser')
    url = request.args.get('url')

    if(browser_type == None or url == None):
        return "Bad Request! Browser or URL information is missing", 400

    if(is_supported_browser(browser_type) == False):
        return "Not Supported! only firefox and chrome are supported", 403

    cmd_open = get_browser_path(browser_type) + " " + url
    os.system(cmd_open)
        
    return f'{browser_type} Browser instanse is opened', 200

@app.route("/stop", methods = ['GET'])
def close_browser_instance():
    browser_type = request.args.get('browser')

    if(browser_type == None):
        return "Bad Request! Browser information is missing", 400 

    if(is_supported_browser(browser_type) == False):
        return "Not Supported! only firefox and chrome are supported", 403

    os.system("pkill " + browser_type) 
    return f'{browser_type} Browser instanse is closed', 200

@app.route("/cleanup", methods = ['GET'])
def clear_browser():
    browser_type = request.args.get('browser')

    if(browser_type == None):
        return "Bad Request! Browser information is missing", 400 

    if(is_supported_browser(browser_type) == False):
        return "Not Supported! only firefox and chrome are supported", 403

    remove_cmd = "rm -rfv " + get_cache_path(browser_type)
    os.system(remove_cmd); 
    return f'{browser_type} Browser chached information is cleared', 200


# @app.route("/geturl", methods = ['GET'])
# def clear_browser():
#     browser_type = request.args.get('browser')

#     if(browser_type == None):
#         return "Bad Request! Browser information is missing", 400 

#     if(is_supported_browser(browser_type) == False):
#         return "Not Supported! only firefox and chrome are supported", 403

#     remove_cmd = "rm -rfv " + get_cache_path(browser_type)
#     os.system(remove_cmd); 
#     return f'{browser_type} Browser chached information is cleared', 200

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=6123)