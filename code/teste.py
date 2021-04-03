from googleapiclient import discovery
import json
import csv

API_KEY = 'AIzaSyB_wryWmzpPOdmlt_j6bmnXrg_0xBFVUBY'

# Generates API client object dynamically based on service name and version.
service = discovery.build('commentanalyzer', 'v1alpha1', developerKey=API_KEY)

var = 'covid-tweets.csv'
analyze_request = {
  'comment': {'text': 'vai tomar no cu'},
  'requestedAttributes': {'TOXICITY': {}}
}

response = service.comments().analyze(body=analyze_request).execute()


print(json.dumps(response, indent=2))



