import requests, json, pandas

### https://www.circl.lu/services/cve-search/
### https://cve.circl.lu/api/
### URL example - curl -H "limit: 10" -H "cvss_modifier: above" -H "cvss_score: 6.8" -H "rejected: show" https://cve.circl.lu/api/query

def run():
    payload = {'limit': '1', 'cvss_modifier': 'above', 'cvss_score': '6.8'}
    base_url = 'http://cve.circl.lu/api/query'
    ### become a reponse object into a string and save it in a dict.
    i = (requests.get(base_url, params=payload)).text
    data = json.loads(i)['results']
    #print(data.keys())
    cveID = [i['id'] for i in data]
    cveSummary = [i['summary'] for i in data]
    for cve, summary in zip(cveID, cveSummary):
      print "\nCVE: ",cve
      print "Summary: ",summary

if __name__ == '__main__':
    run()
