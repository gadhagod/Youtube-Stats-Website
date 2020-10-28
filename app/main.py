import flask
import google_auth_oauthlib
import googleapiclient.errors
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

app = flask.Flask(__name__)

@app.route('/', methods=['get'])
def index():
    return(flask.render_template('index.html'))

@app.route('/channel-id/<channel>', methods=['GET'])
def id_index(channel):
    SCOPES = ['https://www.googleapis.com/auth/youtube.readonly']
    creds = None

    with open('token.pickle', 'rb') as token:
        creds = pickle.load(token)

    with open('token.pickle', 'wb') as token:
        pickle.dump(creds, token)

    request = googleapiclient.discovery.build(
        'youtube', 'v3', credentials=creds
    ).channels().list(
        id=channel,
        part='snippet,statistics'
    ).execute()

    print(request)
    
    items = request['items'][0]
    image = items['snippet']['thumbnails']['default']['url']
    title = items['snippet']['title']
    description = items['snippet']['description']
    subs = items['statistics']['subscriberCount']
    views = items['statistics']['viewCount']
    videos = items['statistics']['videoCount']

    return(flask.render_template('channel.html', image=image, title=title, description=description, subs=subs, views=views, videos=videos, button_type='channelid', channel=channel))

@app.route('/channel-name/<channel>', methods=['GET'])
def name_index(channel):
    channel = channel.replace('%20', ' ')
    SCOPES = ['https://www.googleapis.com/auth/youtube.readonly']
    creds = None

    with open('token.pickle', 'rb') as token:
        creds = pickle.load(token)

    with open('token.pickle', 'wb') as token:
        pickle.dump(creds, token)

    request = googleapiclient.discovery.build(
        'youtube', 'v3', credentials=creds
    ).channels().list(
        forUsername=channel,
        part='snippet,statistics'
    ).execute()

    print(request)
    
    items = request['items'][0]
    image = items['snippet']['thumbnails']['default']['url']
    title = items['snippet']['title']
    description = items['snippet']['description']
    subs = items['statistics']['subscriberCount']
    views = items['statistics']['viewCount']
    videos = items['statistics']['videoCount']

    return(flask.render_template('channel.html', image=image, title=title, description=description, subs=subs, views=views, videos=videos, button_type='channel', channel=channel))
    
@app.errorhandler(500)
def five_hundred(err):
    return(flask.render_template('no_results.html'))

@app.errorhandler(404)
def four_zero_four(err):
    return(flask.render_template('no_results.html'))