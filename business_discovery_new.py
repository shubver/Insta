from defines import getCreds, makeApiCall
import get_user_media_new
import dtale
import pandas as pd
import time
import logging
import threading

def return_business_discovery(uploaded_username):
    def getAccountInfo( params ,ig_username) :
        """ Get info on a users account
        
        API Endpoint:
            https://graph.facebook.com/{graph-api-version}/{ig-user-id}?fields=business_discovery.username({ig-username}){username,website,name,ig_id,id,profile_picture_url,biography,follows_count,followers_count,media_count}&access_token={access-token}
        Returns:
            object: data from the endpoint
        """
        endpointParams = dict() # parameter to send to the endpoint
        endpointParams['fields'] = 'business_discovery.username(' + ig_username + '){username,website,name,ig_id,id,profile_picture_url,biography,follows_count,followers_count,media_count}' # string of fields to get back with the request for the account
        endpointParams['access_token'] = params['access_token'] # access token

        url = params['endpoint_base'] + params['instagram_account_id'] # endpoint url

        return makeApiCall( url, endpointParams, params['debug'] ) # make the api call

    params = getCreds() # get creds
    params['debug'] = 'no' # set debug
    # username_df = pd.read_csv(uploaded_username)
    params['ig_username'] = uploaded_username

    user_info_list = []
    for ig_username in params['ig_username']:
        user_info_dict = {}
        user_info_dict['Username'] = ig_username

        response = getAccountInfo( params,ig_username) # hit the api for some data!

        # print("\n---- ACCOUNT INFO -----\n") # display latest post info
        # print("username:") # label
        # print(response['json_data']['business_discovery']['username']) # display username

        try:
            # print("\nname:") # label
            # print(response['json_data']['business_discovery']['name'])
            user_info_dict['Name'] = response['json_data']['business_discovery']['name']
        except:
            user_info_dict['Name'] = None

        try:
            # print("\nID:") # label
            # print(response['json_data']['business_discovery']['id'])
            user_info_dict['User ID'] = response['json_data']['business_discovery']['id']
        except:
            user_info_dict['User ID'] = None

        try:
            # print("\nIG_ID:") # label
            # print(response['json_data']['business_discovery']['ig_id'])
            user_info_dict['User IG ID'] = response['json_data']['business_discovery']['ig_id']
        except:
            user_info_dict['User IG ID'] = None

        try:
            # print("\nwebsite:") # label
            # print(response['json_data']['business_discovery']['website']) # display users website
            user_info_dict['website'] = response['json_data']['business_discovery']['website']
        except:
            user_info_dict['website'] = None

        try:
            # print("\nnumber of posts:") # label
            # print(response['json_data']['business_discovery']['media_count']) # display number of posts user has made
            user_info_dict['Total Posts'] = response['json_data']['business_discovery']['media_count']
        except:
            user_info_dict['Total Posts'] = None
        
        try:    
            # print("\nfollowers:") # label
            # print(response['json_data']['business_discovery']['followers_count']) # display number of followers the user has
            user_info_dict['Followers'] = response['json_data']['business_discovery']['followers_count']
        except:
            user_info_dict['Followers'] = None
        
        try:
            # print("\nfollowing:") # label
            # print(response['json_data']['business_discovery']['follows_count'] )# display number of people the user follows
            user_info_dict['Following'] = response['json_data']['business_discovery']['follows_count']
        except:
            user_info_dict['Following'] = None

        # try:
        #     print("\nprofile picture url:") # label
        #     print(response['json_data']['business_discovery']['profile_picture_url']) # display profile picutre url
        #     user_info_dict['Profile Picture Url'] = response['json_data']['business_discovery']['profile_picture_url']
        # except:
        #     user_info_dict['Profile Picture Url'] = None

        try:
            # print("\nbiography:" )# label
            # print(response['json_data']['business_discovery']['biography']) # display users about section
            user_info_dict['Biography'] = response['json_data']['business_discovery']['biography']
        except:
            user_info_dict['Biography'] = None

        user_info_list.append(user_info_dict)

    user_info_df = pd.DataFrame(user_info_list)


    # one_df = get_user_media_one.return_media_one()
    media_df, one_df = get_user_media_new.return_last_media(uploaded_username)

    data_df = pd.merge(user_info_df, one_df, on="Username")
    data_df = pd.merge(data_df, media_df, on='Username')

    data_df['Avg Post Impressions'] = (data_df['Last 50 Posts Like Count'] + data_df['Last 50 Posts Comments Count'])/ data_df['Total Posts Count']
    data_df['Organic Ratio'] = data_df['Avg Post Impressions']/data_df['Followers']
    data_df['Follow Ratio'] = data_df['Following']/data_df['Followers']

    return data_df
    # data_df.to_csv('Insta_Data.csv')
