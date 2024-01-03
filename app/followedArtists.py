import spotipy
import spotipy.util as util

REDIRECT_URI = 'http://localhost:8888/callback'
SCOPE = 'user-follow-read'

def followedArtists(client_id, client_secret, user):
    # Get authorization token
    token = util.prompt_for_user_token(
        username=user,
        scope=SCOPE,
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=REDIRECT_URI
    )

    # Create a Spotify API object using the obtained token
    sp = spotipy.Spotify(auth=token)    #spotipy object usage ready

    followed_artists = []
    
    pagi = sp.current_user_followed_artists()
    followed_artists.extend(pagi['artists']['items'])   #large list

    while pagi['artists']['next']:   #while there's a next item
        pagi = sp.next(pagi['artists']) #get the next pagination
        followed_artists.extend(pagi['artists']['items'])

    print(artistNames(followed_artists))

    return followed_artists

def artistNames(artist_list):
    artist_name = []
    for artist in artist_list:
        artist_name.append(artist['name'])
    return artist_name

    '''
    # Get and print the user's display name
    user_info = sp.current_user()
    display_name = user_info.get('display_name', 'N/A')
    print(f"Hello, {display_name}!")

    # If you need to make other API requests, you can do so using the 'sp' object
    # For example, getting the user's playlists:
    playlists = sp.current_user_playlists()
    print("\nYour playlists:")
    for playlist in playlists['items']:
        print(f"- {playlist['name']}")

    '''
