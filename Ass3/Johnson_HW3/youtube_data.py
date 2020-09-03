# Author:  Alex Johnson

#  youtube_data.py searches YouTube for videos matching a search term
#  program sorts and displays different anylsises on the results

#  to run type python3 youtube_data.py then hit type your search term, hit enter, then max results and hit enter again.


from apiclient.discovery import build      # use build function to create a service object

import unidecode   #  need for processing text fields in the search results

import csv # needed for ouput of search result

# put your API key into the API_KEY field below, in quotes
API_KEY = "AIzaSyDOcjLiX6pl74848tOumyAztNfTOZT43v0"

API_NAME = "youtube"
API_VERSION = "v3"       # this should be the latest version

search_max = 20

#  function youtube_search retrieves the YouTube records

def youtube_search(s_term, s_max):
    youtube = build(API_NAME, API_VERSION, developerKey=API_KEY)   

    search_response = youtube.search().list(q=s_term, part="id,snippet", maxResults=s_max).execute()
    
    # search for videos matching search term;
    with open('youtube_results.csv', mode='w') as youtube_results:
        youtube_results = csv.writer(youtube_results, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        search_res = search_response.get("items", [])
        count = 1
        for search_result in search_res:
            if search_result["id"]["kind"] == "youtube#video":
                title = search_result["snippet"]["title"]
                title = unidecode.unidecode(title)  
                videoId = search_result["id"]["videoId"]
                video_response = youtube.videos().list(id=videoId,part="statistics").execute()
                for video_results in video_response.get("items",[]):
                    viewCount = video_results["statistics"]["viewCount"]
                    if 'likeCount' not in video_results["statistics"]:
                        likeCount = 0
                    else:
                        likeCount = video_results["statistics"]["likeCount"]
                    if 'dislikeCount' not in video_results["statistics"]:
                        dislikeCount = 0
                    else:
                        dislikeCount = video_results["statistics"]["dislikeCount"]
                    if 'commentCount' not in video_results["statistics"]:
                        commentCount = 0
                    else:
                        commentCount = video_results["statistics"]["commentCount"]
                
                    youtube_results.writerow([title, videoId, viewCount, likeCount, dislikeCount, commentCount])

        print("")
        print("")
        print("===================================================")
        print("Highest Views")
        print("===================================================")  # printing the header and spacing it correctly
        already_found = []  # used to store the ids of the videos that were already found to be the highest ranking
        highest = 0         # used to keep track of the highest view count
        highest_data = ""   # used to keep the data of the highest view count found so far
        high_id = ""        # used to keep the id of the highest view count video found so far
        count = 1           # used to keep track of how many videos have been ranked so far
        for i in range(5):                                                                                              # run the program 5 times to find top 5
            for search_result in search_res:                                                                            # parse through the results from the query
                if search_result["id"]["kind"] == "youtube#video":                                                      # check if the video is of type youtube video
                    title = search_result["snippet"]["title"]                                                           # get the title
                    title = unidecode.unidecode(title)                                                                  # decode the title
                    videoId = search_result["id"]["videoId"]                                                            # get the video id
                    video_response = youtube.videos().list(id=videoId,part="statistics").execute()                      # get all the videos from the search results
                    for video_results in video_response.get("items",[]):                                                
                        viewCount = int(video_results["statistics"]["viewCount"])                                       # get the view count of the video
                        if(viewCount > highest):                                                                        # check if that view vount is greater than the highest so far
                            if(videoId not in already_found):                                                           # if it is higher, make sure it hasn't been used as a top 5 in previous iterations
                                highest = viewCount                                                                     
                                highest_data = str(count) + ". " + title + " " + str(videoId) + " " + str(viewCount)
                                high_id = videoId                                                                       # set all the data to the current highest
            already_found.append(high_id)                                                                               # append the id of the highest video to check in future iterations if found
            print(highest_data)                                                                                         # print the data of the highets found in this iteration
            highest = 0
            count = count + 1

        already_found = []                                                                                              # reset the data

        print("")
        print("")
        print("===================================================")
        print("Highest Like Percentage")
        print("===================================================")                                                    # the next block of code is the same as above however this time it
        count = 1                                                                                                       # finds the like count as well and calculates the percent of likes / views
        for i in range(5):                                                                                              # and ranks from that
            for search_result in search_res:
                if search_result["id"]["kind"] == "youtube#video":
                    title = search_result["snippet"]["title"]
                    title = unidecode.unidecode(title)  
                    videoId = search_result["id"]["videoId"]
                    video_response = youtube.videos().list(id=videoId,part="statistics").execute()
                    for video_results in video_response.get("items",[]):
                        viewCount = int(video_results["statistics"]["viewCount"])
                        likeCount = int(video_results["statistics"]["likeCount"])
                        if((likeCount / viewCount) > highest):
                            if(videoId not in already_found):
                                highest = (likeCount / viewCount)
                                highest_data = str(count) + ". " + title + " " + str(videoId) + " " + str(likeCount / viewCount * 100)
                                high_id = videoId
            already_found.append(high_id)
            print(highest_data)
            highest = 0
            count = count + 1

        already_found = []

        print("")
        print("")
        print("===================================================")
        print("Highest Dislike Percentage")
        print("===================================================")                                                    # this block does the same as above but with dislikes
        count = 1
        for i in range(5):
            for search_result in search_res:
                if search_result["id"]["kind"] == "youtube#video":
                    title = search_result["snippet"]["title"]
                    title = unidecode.unidecode(title)  
                    videoId = search_result["id"]["videoId"]
                    video_response = youtube.videos().list(id=videoId,part="statistics").execute()
                    for video_results in video_response.get("items",[]):
                        viewCount = int(video_results["statistics"]["viewCount"])
                        Dislikes = int(video_results["statistics"]["dislikeCount"])
                        if((Dislikes / viewCount) > highest):
                            if(videoId not in already_found):
                                highest = (Dislikes / viewCount)
                                highest_data = str(count) + ". " + title + " " + str(videoId) + " " + str(Dislikes / viewCount * 100)
                                high_id = videoId
            already_found.append(high_id)
            print(highest_data)
            highest = 0
            count = count + 1

search_term = input("Search Term: ")                # gets the user input for search term
while True:                                         # infinite loop till broken
    try:                                               
        search_max = int(input("Max Results: "))    # try and compute the input to a number
    except:
        print("Please enter a integer valuer")      # if fails then print error and re prompt
        continue
    else:
        break                                       # if it works, break

print("")
print("")
print("Searching for "+ str(search_max) + " results on the term " + search_term + "...")    # print loading message
    
youtube_search(search_term, search_max + 1)     # call function to retrieve data
