
#Brandon Mefford    5/22/2020

#an attempt at controlling my spotify through discord commands

# I have removed my credentials for github purposes but it is possible to add
# prompts for infomation, for now they do not exist and are not needed

# this program was created to control our private spotify playlists
# from an online chatroom through the use of commands created in this program

# this program requires:
        #discord oauth token
        #spoitfy client ID
        #spotify Secret Client ID
        #spotify redirect url
        #spotify playlist id
        #spotify user id

# TODO: Need to clean up and reuse code properly
#       Need to rename variables for better practice
#       Add exceptional exceptions

# DOCS:
#  https://discord.com/developers/applications 
#  https://spotipy.readthedocs.io/en/2.12.0/

import discord
import spotipy
import spotipy.util as util
from discord.ext import commands


# client side <windows 10> environment variables if provided
# set SPOTIPY_CLIENT_ID='[my id]'
# set SPOTIPY_CLIENT_SECRET='[my secret]'
# set SPOTIPY_REDIRECT_URI='localhost:8888/callback'

#me
# CLIENT_ID = '<removed>'
# CLIENT_SECRET = '<removed>'
# CLIENT_REDIRECT = '<removed>'

#garrett
# CLIENT_ID = '<removed>'
# CLIENT_SECRET = '<removed>'
# CLIENT_REDIRECT = '<removed>'


# I set up my environmental variables to include my id but for individual users
# ... you can manually include the id as illistrated below
# NOTE: YOU MUST FIND YOUR OWN SPOTIFY PROVIDED tokens 

# util.prompt_for_user_token(username,
#                            scope,
#                            client_id='your-spotify-client-id',
#                            client_secret='your-spotify-client-secret',
#                            redirect_uri='your-app-redirect-url')


#future
# requires <spotify username>
# requires <spotify playlist id>

#me
# PLAYLIST_ID = "<removed>"
# username = "<removed>"

#garrett
PLAYLIST_ID = "<removed>"
username = "<removed>"


#scope
scope = 'user-read-private user-read-playback-state user-modify-playback-state playlist-modify-public playlist-modify-private'

#prefix
client = commands.Bot(command_prefix="'")


#startup event
@client.event
async def on_ready():
    print("simpBot is ready")


#async def simpQueue(ctx, uri):

#asyncronous timed function to queue our given song
#<ctx> is the context of the command
#<uri> is the spotify track uri to be queue

# token needs spotify developer ID's we have provided earlier, you must find
# your own credentials
# 1.   try to authenticate, otherwise failure
# 2.   create our spotify object given correct authentication
    # 2.1  scope is specific to give access rights authentication token
# 3.   the uri of this command is trimmed to read
# 4.   try add_to_queue(uri=uri_sent, device_id=None) otherwise failure
@client.command()
async def simpQueue(ctx, uri):
    try:
        token = util.prompt_for_user_token(username, scope)
    except:
        await ctx.send('something went wrong')

    spotify_obj = spotipy.Spotify(auth=token)


    USER = spotify_obj.current_user()
    devices = spotify_obj.devices()
    deviceID = devices['devices'][0]['id']


    uri_sent = uri
    uri_sent = uri.replace('spotify:track:', '')
    name_from_uri = spotify_obj.track(uri_sent)


    spotify_obj.trace = False
    try:
        spotify_obj.add_to_queue(uri=uri_sent, device_id=None)
        await ctx.send('Added \'' + name_from_uri['name'] + '\' to queue')
    except:
        await ctx.send('something went wrong')




#async def simpSkip(ctx):

#asyncronous timed function to skip current song
#<ctx> is the context of the command

# token needs spotify developer ID's we have provided earlier, you must find
# your own credentials
# 1.   try to authenticate, otherwise failure
# 2.   create our spotify object given correct authentication
    # 2.1  scope is specific to give access rights authentication token
# 3.   try spotify_obj.next_track(device_id=None) otherwise failure
@client.command()
async def simpSkip(ctx):
    try:
        token = util.prompt_for_user_token(username, scope)
    except:
        await ctx.send('something went wrong')

    spotify_obj = spotipy.Spotify(auth=token)


    USER = spotify_obj.current_user()
    devices = spotify_obj.devices()
    deviceID = devices['devices'][0]['id']

    current = str(spotify_obj.current_user_playing_track())


    spotify_obj.trace = False
    try:
        spotify_obj.next_track(device_id=None)
        await ctx.send('Skipped')
    except:
        await ctx.send('something went wrong')



#async def blub(ctx, uri):

#asyncronous timed function to skip current song
#<ctx> is the context of the command
#<uri> is the spotify track uri to be queue

# token needs spotify developer ID's we have provided earlier, you must find
# your own credentials
# 1.   try to authenticate, otherwise failure
# 2.   create our spotify object given correct authentication
    # 2.1  scope is specific to give access rights authentication token
# 3.   the uri of this command is trimmed to read
# 4.   try user_playlist_add_tracks(username, PLAYLIST_ID, [uri_sent])
#      otherwise failure
@client.command()
async def blub(ctx, uri):
    try:
        token = util.prompt_for_user_token(username, scope)
    except:
        await ctx.send('something went wrong')

    spotify_obj = spotipy.Spotify(auth=token)


    USER = spotify_obj.current_user()
    devices = spotify_obj.devices()
    deviceID = devices['devices'][0]['id']


    track_ids = str(uri)
    uri_sent = track_ids.replace('spotify:track:', '')

    name_from_uri = spotify_obj.track(uri_sent)

    spotify_obj.trace = False
    try:
        results = spotify_obj.user_playlist_add_tracks(username, PLAYLIST_ID, [uri_sent])
        await ctx.send('Added \'' + name_from_uri['name'] + '\' to playlist')
    except:
        await ctx.send('something went wrong')



# run the client given auth id
# see https://discord.com/developers/applications to get your own
client.run('<removed>')
