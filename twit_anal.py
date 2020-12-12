'''
https://www.geeksforgeeks.org/python-api-followers-in-tweepy/
screen_name = "geeksforgeeks"
  
# getting only 30 followers 
for follower in tweepy.Cursor(api.followers, screen_name).items(30): 
    print(follower.screen_name) 
# the screen_name of the targeted user 
screen_name = "geeksforgeeks"
  
# getting all the followers 
c = tweepy.Cursor(api.followers, screen_name) 
  
# counting the number of followers 
count = 0
for follower in c.items(): 
    count += 1
print(screen_name + " has " + str(count) + " followers.") 


https://www.programcreek.com/python/example/76301/tweepy.Cursor
    Given a Tweepy/smappPy TweepyPool api, query twitter's rest API for friends of
    given user_id. Returns IDs only (much faster / more per request).
    Parameters:
        api     - fully authenticated Tweepy api or smappPy TweepyPool api
        user_id - twitter user id
    Returns tuple: return code, list of IDs or None (if API call fails)
    """
    cursor = Cursor(api.friends_ids, user_id=user_id)
    user_list, ret_code = call_with_error_handling(list, cursor.items())
   
    if ret_code != 0:
        logger.warning("User {0}: Friends request failed".format(user_id))
    
    # Return user list from API or None (call_with_error_handling returns None if
    # call fail)
    return ret_code, user_lis