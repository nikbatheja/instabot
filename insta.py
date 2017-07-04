import requests

APP_ACCESS_TOKEN = '340907727.1677ed0.76c15d0fe93a4f0897c29065742c4167'

BASE_URL = 'https://api.instagram.com/v1/'

'''
Function declaration to get your own info
'''
def self_info():
    request_url = (BASE_URL + 'users/self/?access_token=%s') % (APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_info = requests.get(request_url).json()

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            print 'Username: %s' % (user_info['data']['username'])
            print 'No. of followers: %s' % (user_info['data']['counts']['followed_by'])
            print 'No. of people you are following: %s' % (user_info['data']['counts']['follows'])
            print 'No. of posts: %s' % (user_info['data']['counts']['media'])
        else:
            print 'User does not exist!'
    else:
        print 'Status code other than 200 received!'

def get_user_info(insta_username):
  user_id = get_user_id(insta_username)
  if user_id == None:
    print 'User does not exist!'
    exit()
  request_url = (BASE_URL + 'users/%s?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
  print 'GET request url : %s' % (request_url)
  user_info = requests.get(request_url).json()

  if user_info['meta']['code'] == 200:
    if len(user_info['data']):
      print 'Username: %s' % (user_info['data']['username'])
      print 'No. of followers: %s' % (user_info['data']['counts']['followed_by'])
      print 'No. of people you are following: %s' % (user_info['data']['counts']['follows'])
      print 'No. of posts: %s' % (user_info['data']['counts']['media'])
    else:
      print 'There is no data for this user!'
  else:
    print 'Status code other than 200 received!'
self_info()