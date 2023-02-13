import webbrowser
from msal import ConfidentialClientApplication, PublicClientApplication

#client_secret = 'Ozz8Q~4kzztKfpGwkptVKf8Z~cxaqV2wCizfDcqT'
client_secret = 'rIZ8Q~fML0bEdeJTkPVk~ZUWGaCMYN6G2CIvJdqE'
app_id = '2a0af66b-8482-4e97-86b3-23c7bfda0014'
#app_id = '29c7a779-bfe0-4c83-88fe-d6e8c16477d7'
SCOPES = ['User.Read']

client = ConfidentialClientApplication(client_id=app_id,client_credential=client_secret)
authorization_url = client.get_authorization_request_url(SCOPES)
print(authorization_url)
webbrowser.open(authorization_url)

autorization_code = 'f5e7b63d6d6d479dace6905feeded805'
access_token = client.acquire_token_by_authorization_code(code=autorization_code,scopes=SCOPES)

print(access_token)