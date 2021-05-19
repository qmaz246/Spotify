import requests, sys, json, pprint

client_id = "e380193f04fc477ab9e81210b29b60fe"
client_secret = "9d6b5d1d850f454fbd3e98cedaf214a0"

def get_profile(auth_token):
    url = "https://api.spotify.com/v1/me"
    headers = { "Accept": "application/json",
                "Content-Type": "application/json",
                "Authorization": ("Bearer " + auth_token)
            }
    return requests.get(url, headers=headers)

def get_authorized():

    print("Go to this specific address")
    link = "https://accounts.spotify.com/authorize?client_id={:s}&redirect_uri=http:%2F%2Fexample.com%2Fcallback%2F&scope=user-read-private%20user-read-email&response_type=token&state=123".format(client_id)
    print(link)
    auth_token = input("Enter the authorization token:")
    return auth_token

def choose_playlist(auth_token, user_id):
    url = "https://api.spotify.com/v1/users/{:s}/playlists".format(user_id)
    headers = { "Accept": "application/json",
                "Content-Type": "application/json",
                "Authorization": ("Bearer " + auth_token)
            }
    
    res = requests.get(url, headers=headers)
    for list in res.json()["items"]:
        pprint.pprint(list["name"])

    playlist = input("Choose a playlist to check for duplications: ")
    for list in res.json()["items"]:
        if playlist == list["name"]:
            print(list["id"])
            return list["id"]

def find_duplicates(auth_token, playlist_id):
    
    # Obtain list of songs within the playlist
    url = "https://api.spotify.com/v1/playlists/{:s}/tracks?market=ES&fields=items(track(name))&limit=100".format(playlist_id)
    headers = { "Accept": "application/json",
                "Content-Type": "application/json",
                "Authorization": ("Bearer " + auth_token)
            }    
    track_list = requests.get(url, headers=headers).json()["items"]
        
    url = "https://api.spotify.com/v1/playlists/{:s}/tracks?market=ES&fields=items(track(name))&limit=100&offset=100".format(playlist_id)
    track_list.extend(requests.get(url, headers=headers).json()["items"])

    url = "https://api.spotify.com/v1/playlists/{:s}/tracks?market=ES&fields=items(track(name))&limit=100&offset=200".format(playlist_id)
    track_list.extend(requests.get(url, headers=headers).json()["items"])

    url = "https://api.spotify.com/v1/playlists/{:s}/tracks?market=ES&fields=items(track(name))&limit=100&offset=300".format(playlist_id)
    track_list.extend(requests.get(url, headers=headers).json()["items"])

    url = "https://api.spotify.com/v1/playlists/{:s}/tracks?market=ES&fields=items(track(name))&limit=100&offset=400".format(playlist_id)
    track_list.extend(requests.get(url, headers=headers).json()["items"])
    print(track_list)
    duplicate_list = []
    print("track_list len = %i"%(len(track_list)))
    for i in range(len(track_list)):
        for j in range(i+1, len(track_list)):
            # print("{:s} -> {:s}".format(track_list[i]["track"]["name"], track_list[j]["track"]["name"]))
            try:
                if track_list[i]["track"]["name"] == track_list[j]["track"]["name"]:
                # print("Found")
                    duplicate_list.append([{"name": track_list[i]["track"]["name"], "artist": "", "index": i}, {"name": track_list[j]["track"]["name"], "artist": "", "index": j}])
            except:
                pass
    
    pprint.pprint(duplicate_list)
    

if __name__== "__main__":
    auth_token = get_authorized()
    profile = get_profile(auth_token).json()
    
    pprint.pprint(profile)
    print("")
    
    playlist_id = choose_playlist(auth_token, profile["id"])
    print("")

    find_duplicates(auth_token, playlist_id)


