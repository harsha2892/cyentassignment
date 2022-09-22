from sys import argv
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def fetch_repos(user):
    base_url = "https://api.github.com/users/"
    page_index = 1
    repos_end_point = "/repos?per_page=100&page="

    data = ""
    while data != None:
        url = "{}{}{}{}".format(base_url, user, repos_end_point, str(page_index))
        data = requests.get(url, verify=False, timeout=20)

        if data.status_code in (200, 202) and len(data.json()) > 0:
            response = data.json()

            for repo in response:
                name = repo['name']
                ssh_url = repo['ssh_url']

                print("repo name is '{}' and its url is '{}' and since it is able to fetch from internet it is public repo".format(name, ssh_url))

            page_index += 1
        else:
            break

if __name__ == "__main__":
    if len(argv) != 2:
        print("need user/org as input")
        print("ex: python3 fetch_repos.py netflix")
        exit(1)

    user = argv[1]
    fetch_repos(user)
