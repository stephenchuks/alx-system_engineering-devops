#/usr/bin/python3

import praw

def count_words(subreddit, word_list, count={}):
    # Initialize the Reddit object
    reddit = praw.Reddit(client_id='your_client_id',
                         client_secret='your_client_secret',
                         user_agent='your_user_agent')

    # Get the subreddit object
    try:
        sub = reddit.subreddit(subreddit)
    except praw.exceptions.NotFound:
        # Subreddit not found, return empty count
        return

    # Get the hot posts from the subreddit
    hot_posts = sub.hot(limit=10)

    # Iterate over the hot posts
    for post in hot_posts:
        # Get the lowercase title of the post
        title = post.title.lower()
        # Split the title into words
        words = title.split()
        # Iterate over the words
        for word in words:
            # Remove special characters from the word
            word = ''.join(e for e in word if e.isalnum())
            # Check if the word is in the word list
            if word.lower() in word_list:
                # Increment the count of the word
                if word in count:
                    count[word] += 1
                else:
                    count[word] = 1

    # If there are more hot posts, recursively call the function
    if len(count) < len(word_list):
        count_words(subreddit, word_list, count)

    # Sort the count by the count value (descending) and word (ascending)
    sorted_count = sorted(count.items(), key=lambda x: (-x[1], x[0]))

    # Print the count
    for word, count in sorted_count:
        print(f"{word}: {count}")

