#
import requests


def getNumDraws(year):
    # Write your code here
    
    total_num_draws = 0
    current_page = 1
    
    req = requests.get("https://jsonmock.hackerrank.com/api/football_matches?year={}&page={}".format(year, current_page))
    json_data = req.json()
    game_data = json_data['data']
    total_page = json_data['total_pages']
    
    print(total_page)
    print(game_data)    

    while current_page <= total_page:
        req = requests.get("https://jsonmock.hackerrank.com/api/football_matches?year={}&page={}".format(year, current_page))
        json_data = req.json()
        game_data = json_data['data']
        
        for game in game_data:
            if game['team1goals'] == game['team2goals']:
                total_num_draws += 1
        
        current_page += 1
        
    return total_num_draws