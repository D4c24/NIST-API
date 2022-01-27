import requests

### https://www.circl.lu/services/cve-search/
### https://cve.circl.lu/api/
### URL example - curl -H "limit: 10" -H "cvss_modifier: above" -H "cvss_score: 6.8" -H "rejected: show" https://cve.circl.lu/api/query

def run():
    payload = {'limit': '5', 'cvss_modifier': 'above', 'cvss_score': '6.8'}
    r = requests.get('http://cve.circl.lu/api/query', params=payload)
    print(r.text)

if __name__ == '__main__':
    run()        