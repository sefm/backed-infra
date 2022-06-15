import requests
import json
import argparse


# Initialize parser
parser = argparse.ArgumentParser()

# Adding optional argument
parser.add_argument("-r", "--repo", help = "use -r ")

# Read arguments from command line
args = parser.parse_args()

if args.repo:
    print("Displaying Output as: % s" % args.repo)



def get_issues(repo=''):
    user='sefm'
    token='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'  # created oath token that expires in two days
    # repo='backed-infra'
    headers = {'Authorization': 'token ' + token}

    response = requests.get('https://api.github.com/' + 'repos/' + user + '/' + repo + '/issues', headers=headers)
    json_response=json.loads(response.content) # Here we got array of json and we need iterate and filter only when state open
    # output_dict = [x for x in json_response if x['state'] == 'open'][0]  # we can use filter(lambda['state']  for testing true/false
    mylist = list(filter(lambda y: (y['state'] == 'open' and len(y['labels']) > 0), json_response)) # Also we're checking for only issues with labels
    for x in mylist : print(x)
    # h = [[x for x in json_response.get('state', list()) if x.get('state') == 'open']]

get_issues(repo=args.repo)
