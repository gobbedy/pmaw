from psaw import PushshiftAPI as psawAPI
from pmaw import PushshiftAPI as pmawAPI
import os
import time


#pmaw_api = pmawAPI(num_workers=os.cpu_count()*5)
psaw_api = psawAPI()

for num_workers in [2, 4, 8, 16]:
    pmaw_api = pmawAPI(num_workers=num_workers)
    start = time.time()
    test = pmaw_api.search_submissions(after=1612372114,
                                  before=1612501714,
                                  subreddit='wallstreetbets',
                                  filter=['title', 'link_flair_text', 'selftext', 'score'])
    end = time.time()
    print("num_workers: " + str(num_workers))
    print("pmaw took " + str(end - start) + " seconds.")
    print("num_results: " + str(len(test)))
    print("-"*50)

'''
start = time.time()
test_gen = psaw_api.search_submissions(after=1612372114,
                              before=1612501714,
                              subreddit='wallstreetbets',
                              filter=['title', 'link_flair_text', 'selftext', 'score'])
test = list(test_gen)
end = time.time()
print("psaw took " + str(end - start) + " seconds.")
'''