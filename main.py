import requests
import sys
import urllib.parse as u
import webbrowser

# Function to search for a movie using the YTS api

def search_movie(movie_name):
    url = "https://yts.am/api/v2/list_movies.json"
    parameters = {'query_term' : movie_name,'sort_by' : 'rating'}
    
    try:
        r = requests.get(url, params=parameters)
        data = r.json()
    except Exception as e:
        print("Failed to fetch data:", e)
        return
    
    # Check to see if the title is available or not
    if (data['data']['movie_count'] == 0):
        print("Couldn't find the title. Please double-check the spelling or try a different title.")
        return 
    
    movies = data["data"]["movies"]
    selected_movie = None
    
    for m in movies:
        if (m["title"].lower() == movie_name.lower()):
            selected_movie = m
            break
    if not selected_movie:
        selected_movie = movies[0]
        
    torrents = selected_movie["torrents"]
    
    print("\nTitle: "+selected_movie['title'])
    
    selected_torrent = pickQuality(torrents)
    magnet(selected_torrent, selected_movie['title'])
    
# Function to list out the available qualities and let the user choose one 
def pickQuality(torrents):
    
    print("\nAvailable Qualities: ")
    
    for i in range(len(torrents)):
        print(f"{i+1}) {torrents[i]['quality']} {torrents[i]['type']}")
    
    while True:
        try:
            n = int(input("\nPlease select the desired quality: "))
            if n > 0 and n <= len(torrents):
                return torrents[n - 1]  
            else:
                raise ValueError
        except ValueError:
            print("Please type a valid number.")

# function to generate and open the magnet link
def magnet(torrent, movie_name):
    hash = torrent['hash']
    name = u.quote(movie_name)
    
    trackers = [
        'udp://open.demonii.com:1337/announce',
        'udp://tracker.openbittorrent.com:80',
        'udp://tracker.coppersurfer.tk:6969',
        'udp://glotorrents.pw:6969/announce',
        'udp://tracker.opentrackr.org:1337/announce',
        'udp://torrent.gresille.org:80/announce',
        'udp://p4p.arenabg.com:1337',
        'udp://tracker.leechers-paradise.org:6969'
    ]
    
    tracker_string = ''.join(f"&tr={u.quote(tr)}" for tr in trackers)
    magnet = f"magnet:?xt=urn:btih:{hash}&dn={name}{tracker_string}"
    success = webbrowser.open(magnet)
    if success:
        print("Successfully opened the magnet link!")
    else:
        print("Failed to open magnet link.")
        print(magnet)

# main
def main():
    
    if len(sys.argv) < 2:
        print("Not enough arguments")
        exit()
    movie_name = ' '.join(sys.argv[1:])
    search_movie(movie_name)
    

if __name__ == '__main__':
    main()