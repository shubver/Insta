from defines import getCreds, makeApiCall
import pandas as pd

def return_last_media(uploaded_username):
    def getUserMedia( params, ig_username, pagingUrl = '') :
        """ Get users media

        API Endpoint:
            https://graph.facebook.com/{graph-api-version}/{ig-user-id}/media?fields={fields}&access_token={access-token}

            GET graph.facebook.com/[YOUR-IG-BUSINESS-ACCOUNT-ID]?fields=business_discovery.username(USERNAME){media{caption,media_url,media_type,like_count,comments_count,id}}
        Returns:
            object: data from the endpoint
        """

        endpointParams = dict() # parameter to send to the endpoint
        endpointParams['fields'] = 'business_discovery.username(' + ig_username + '){media{timestamp,caption,media_url,media_type,like_count,comments_count,id}}' # string of fields to get back with the request for the account

        # endpointParams['fields'] = 'id,caption,media_type,media_url,permalink,thumbnail_url,timestamp,username,like_count,comments_count' # fields to get back
        endpointParams['access_token'] = params['access_token'] # access token

        if ( '' == pagingUrl ) : # get first page
            url = params['endpoint_base'] + params['instagram_account_id']
        else : # get specific page
            url = params['endpoint_base'] + params['instagram_account_id']
            endpointParams['after'] = pagingUrl
            # url = params['endpoint_base'] + params['instagram_account_id'] + pagingUrl  # endpoint url
            

        return makeApiCall( url, endpointParams, params['debug'] ) # make the api call

    params = getCreds() # get creds
    params['debug'] = 'no' # set debug
    params['ig_username'] = uploaded_username


    media_list = list() #To store last 50 posts
    list_one = [] #To store last post details


    for ig_username in params['ig_username']:
        like_count = 0
        comments_count = 0
        media_dict = {} #To store last 50 posts
        post_count = 0
        dict_one = {} #To store last post details

        media_dict['Username'] = ig_username
        dict_one['Username'] = ig_username
        response = getUserMedia( params, ig_username ) # get users media from the api

        print("\n\n\n\t\t\t >>>>>>>>>>>>>>>>>>>> {} <<<<<<<<<<<<<<<<<<<<\n".format(ig_username))

        # print("\n\n----------Last POST ----------\n") # post heading
        
        try:
            # print("\nID:") # label
            # print(response['json_data']['business_discovery']['media']['data'][0]['id']) # link to post
            dict_one['Last Post Media ID'] = response['json_data']['business_discovery']['media']['data'][0]['id']
        except:
            dict_one['Last Post Media ID'] = None

        
        try:
            # print("\nLink to post:") # label
            # print(response['json_data']['business_discovery']['media']['data'][0]['media_url']) # link to post
            dict_one['Link to Last Post'] = response['json_data']['business_discovery']['media']['data'][0]['media_url']
        except:
            dict_one['Link to Last Post'] = None

        try:
            # print("\nPost caption:") # label
            # print(response['json_data']['business_discovery']['media']['data'][0]['caption'])# post caption
            dict_one['Last Post Caption'] = response['json_data']['business_discovery']['media']['data'][0]['caption']
        except:
            dict_one['Last Post Caption'] = None

        try:    
            # print("\nMedia type:") # label
            # print(response['json_data']['business_discovery']['media']['data'][0]['media_type']) # type of media
            dict_one['Last Post Media Type'] = response['json_data']['business_discovery']['media']['data'][0]['media_type']
        except:
            dict_one['Last Post Media Type'] = None

        try:
            # print("\nLike Count:") # label
            # print(response['json_data']['business_discovery']['media']['data'][0]['like_count']) # type of media
            dict_one['Last Post Like Count'] = response['json_data']['business_discovery']['media']['data'][0]['like_count']
        except:
            dict_one['Last Post Like Count'] = None

        try:
            # print("\nComments Count:") # label
            # print(response['json_data']['business_discovery']['media']['data'][0]['comments_count']) # type of media
            dict_one['Last Post Comments Count'] = response['json_data']['business_discovery']['media']['data'][0]['comments_count']
        except:
            dict_one['Last Post Comments Count'] = None

        try:    
            # print("\nPosted at:") # label
            # print(response['json_data']['business_discovery']['media']['data'][0]['timestamp']) # when it was posted
            dict_one['Last Post Posted At'] = response['json_data']['business_discovery']['media']['data'][0]['timestamp']
        except:
            dict_one['Last Post Posted At'] = None

        list_one.append(dict_one)

        # print("\n\n\n\t\t\t >>>>>>>>>>>>>>>>>>>> PAGE 1 <<<<<<<<<<<<<<<<<<<<\n") # display page 1 of the posts

        try:    
            for post in response['json_data']['business_discovery']['media']['data'] :
                # print("\n\n---------- POST ----------\n") # post heading

                # print("\nID:") # label
                # print(post['id']) # link to post

                # print("\nLink to post:") # label
                # print(post['media_url']) # link to post

                # print("\nPost caption:") # label
                # print(post['caption'])# post caption

                # print("\nMedia type:") # label
                # print(post['media_type']) # type of media

                # print("\nLike Count:") # label
                # print(post['like_count']) # type of media
                like_count += int(post['like_count'])

                # print("\nComments Count:") # label
                # print(post['comments_count']) # type of media
                comments_count += int(post['comments_count'])

                # print("\nPosted at:") # label
                # print(post['timestamp']) # when it was posted

                post_count += 1
        except:
            like_count += 0
            comments_count += 0
            post_count += 0



        params['debug'] = 'no' # set debug
        response = getUserMedia( params, ig_username, response['json_data']['business_discovery']['media']['paging']['cursors']['after'] ) # get next page of posts from the api

        # print("\n\n\n\t\t\t >>>>>>>>>>>>>>>>>>>> PAGE 2 <<<<<<<<<<<<<<<<<<<<\n") # display page 2 of the posts

        try:
            for post in response['json_data']['business_discovery']['media']['data'] :
                # print("\n\n---------- POST ----------\n") # post heading
                # print("Link to post:") # label
                # print(post['media_url']) # link to post

                # print("\nPost caption:") # label
                # print(post['caption'])# post caption

                # print("\nMedia type:") # label
                # print(post['media_type']) # type of media

                # print("\nLike Count:") # label
                # print(post['like_count']) # type of media
                like_count += int(post['like_count'])

                # print("\nComments Count:") # label
                # print(post['comments_count']) # type of media
                comments_count += int(post['comments_count'])

                # print("\nPosted at:") # label
                # print(post['timestamp']) # when it was posted

                post_count += 1
                
        except:
            like_count += 0
            comments_count += 0
            post_count += 0    

        media_dict['Last 50 Posts Like Count'] = like_count
        media_dict['Last 50 Posts Comments Count'] = comments_count
        media_dict['Total Posts Count'] = post_count

        media_list.append(media_dict)

    media_df = pd.DataFrame(media_list)
    one_df = pd.DataFrame(list_one)

    return media_df, one_df