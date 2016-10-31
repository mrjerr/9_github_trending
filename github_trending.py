import requests
from datetime import date, timedelta


def get_trending_repositories(top_size):

    API_URL = 'https://api.github.com'
    API_SEARCH_REPO = '/search/repositories'
    PERIOD = date.today() - timedelta(days=7)
    PARAMS = {'q': 'created:>{}'.format(PERIOD), 'sort': 'stars'}

    json_data = requests.get(API_URL + API_SEARCH_REPO, params=PARAMS).json()
    result = [
        {
            'html_url': i['html_url'],
            'description': i['description'],
            'stargazers_count': i['stargazers_count'],
            'repo_name': i['name'],
            'repo_owner': i['owner']['login']}
        for i in json_data['items'][:top_size]]

    return result


def get_open_issues_amount(repo_owner, repo_name):
    API_URL = 'https://api.github.com'
    API_REPO_ISSUES = '/repos/{owner}/{repo}/issues'
    json_data = requests.get(
        API_URL +
        API_REPO_ISSUES.format(owner=repo_owner, repo=repo_name)
    ).json()
    if isinstance(json_data, dict):
        raise SystemExit(json_data['message'])
    return [(i['url'], i['title']) for i in json_data]


if __name__ == '__main__':
    for repo in get_trending_repositories(20):
        print('='*50)
        print('\t', repo['description'])
        print(repo['html_url'])
        print('-'*50)
        print('\tStars: {}'.format(repo['stargazers_count']))
        issues = get_open_issues_amount(
            repo_owner=repo['repo_owner'],
            repo_name=repo['repo_name'])
        print('\tIssues: {}'.format(len(issues)))
        for issue in issues:
            print('\t\t', issue[1])
            print('\t', issue[0])
