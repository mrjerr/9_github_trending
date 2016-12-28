import requests
from datetime import date, timedelta


def get_trending_repositories(top_size):
    url_search_repo = 'https://api.github.com/search/repositories'
    period = date.today() - timedelta(days=7)
    params = {'q': 'created:>{}'.format(period), 'sort': 'stars'}

    json_data = requests.get(url_search_repo, params=params).json()
    repositories_data = [
        {
            'html_url': i['html_url'],
            'description': i['description'],
            'stargazers_count': i['stargazers_count'],
            'repo_name': i['name'],
            'repo_owner': i['owner']['login']}
        for i in json_data['items'][:top_size]]

    return repositories_data


def get_open_issues_amount(repo_owner, repo_name):
    url_issues_repo = 'https://api.github.com/repos/{owner}/{repo}/issues'
    json_data = requests.get(
        url_issues_repo.format(owner=repo_owner, repo=repo_name)).json()
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
