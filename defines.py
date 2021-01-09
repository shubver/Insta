import requests
import json

def getCreds() :
	""" Get creds required for use in the applications
	
	Returns:
		dictonary: credentials needed globally
	"""

	creds = dict() # dictionary to hold everything
	creds['access_token'] = 'EAAJyvER7RPMBAE2gu5qlhZCnbY7Ad3KIjDq7eRxI3vLb53zhaSDtTKCPfvOlICvW4weHI1fY9AisRbF5P2NTXZCsKLNzw9e5h548pHdorhuGd8Ln2UDeFaXANaJTjLiIoIPTrUkHrzkq83nTmkm80u8SmDPEg6FKZCvrckE0AZDZD'
	# 'EAAJyvER7RPMBAMpD5w5Oxpi2v5kS7nkC0hnGotzYf3vzy1RpAEadd9WIknZB89PZAND1ch9piLUh3RDoyOY7cFdlEcq09OqR76Mufpuo2eNbEMV2S9IdcCNPzFu9d4EQdqVFHcXO0EZAO8IecwwRhY1bbLD1mrO1FPDb2pl48lfwKItxdfySUBZC0nGjTEHfmsRfjI2sggZDZD' # access token for use with all api calls
	creds['client_id'] = '689102881768691' # client id from facebook app IG Graph API Test
	creds['client_secret'] = 'f607cb9e0406a88014c42e9bc8259a42' # client secret from facebook app
	creds['graph_domain'] = 'https://graph.facebook.com/' # base domain for api calls
	creds['graph_version'] = 'v6.0' # version of the api we are hitting
	creds['endpoint_base'] = creds['graph_domain'] + creds['graph_version'] + '/' # base endpoint with domain and version
	creds['debug'] = 'no' # debug mode for api call
	creds['page_id'] = '494272930981284' # users page id
	creds['instagram_account_id'] = '17841409434132040' # users instagram account id
	creds['ig_username'] = ['powerdrift', 'vegnonveg', 'theakiolife', 'itz_mohit_verma']# ig username

	return creds

def makeApiCall( url, endpointParams, debug = 'no' ) :
	""" Request data from endpoint with params
	
	Args:
		url: string of the url endpoint to make request from
		endpointParams: dictionary keyed by the names of the url parameters
	Returns:
		object: data from the endpoint
	"""

	data = requests.get( url, endpointParams ) # make get request

	response = dict() # hold response info
	response['url'] = url # url we are hitting
	response['endpoint_params'] = endpointParams #parameters for the endpoint
	response['endpoint_params_pretty'] = json.dumps( endpointParams, indent = 4 ) # pretty print for cli
	response['json_data'] = json.loads( data.content ) # response data from the api
	response['json_data_pretty'] = json.dumps( response['json_data'], indent = 4 ) # pretty print for cli

	if ( 'yes' == debug ) : # display out response info
		displayApiCallData( response ) # display response

	return response # get and return content

def displayApiCallData( response ) :
	""" Print out to cli response from api call """

	print("\nURL: ") # title
	print(response['url']) # display url hit
	print("\nEndpoint Params: ") # title
	print(response['endpoint_params_pretty']) # display params passed to the endpoint
	print("\nResponse: ") # title
	print(response['json_data_pretty']) # make look pretty for cli