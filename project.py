from wsgiref import headers
import requests, json

### https://www.circl.lu/services/cve-search/
### https://cve.circl.lu/api/
### URL example - curl -H "limit: 10" -H "cvss_modifier: above" -H "cvss_score: 6.8" -H "rejected: show" https://cve.circl.lu/api/query

def run():
    ## Header
    ### limit: Limit the amount of vulnerabilities to return
    ### cvss_modifier: Select the CVSS score of the CVEs related to cvss_score
    ### cvss_score: CVSS score
    payload = {'limit': '10', 'cvss_modifier': 'above', 'cvss_score': '6.8', 'rejected': 'hide'}
    base_url = 'http://cve.circl.lu/api/query'
    i = (requests.get(base_url, headers=payload)).text
    data = json.loads(i)['results']
    cveID = [i['id'] for i in data]
    cveSummary = [i['summary'] for i in data]
    cveCVSS = [i['cvss'] for i in data]
    cveCWE = [i['cwe'] for i in data]
    for cve, summary, cvss, cwe in zip(cveID, cveSummary, cveCVSS, cveCWE):
      print("\nCVE: ",cve)
      print("Summary: ",summary)
      print("CVSS: ",cvss)
      print("CWE: ",cwe)


if __name__ == '__main__':
    run()