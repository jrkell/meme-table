#### SETTINGS ####
url = 'https://www.reddit.com/r/dankmemes/.json'
allow_nsfw = False
##################


#### CODE ####
import requests, random, json

def main():
    response = requests.get(url)
    ## if error ...
    data = json.loads(response.text)

    found = False
    while not found:
        choice = random.choice(response["data"]["children"])
        if not allow_nsfw and choice["over_18"] == 'true':
            # also check if jpg/png/webm
            
            continue
        break

    print(choice["url"])


if __name__ == '__main__':
    main()
##############