import pytest
from ..leaderboard.leaderboard_wth_generator_solution import get_player_leaderborad

def convert_to_int(data):
    return [int(x) for x in data]

@pytest.fixture
def get_ranking_fixture():
    with open('tests/fixtures/2000_data/ranking.csv', 'r') as f:                
        return f.read().split(',') 

@pytest.fixture
def get_player_ranks():
    with open('tests/fixtures/2000_data/player.csv') as f:
      return f.read().split(',')

@pytest.fixture
def get_expected_output():
    with open('tests/fixtures/2000_data/expected_out_puts.txt') as f:
        return f.read().replace('\n', ',').split(',')

def get_data(path):
    with open(path, 'r') as f:
        data = f.readlines()
    return data



@pytest.mark.parametrize('ranking, player, expected_res', [(pytest.lazy_fixture("get_ranking_fixture"), pytest.lazy_fixture("get_player_ranks"), pytest.lazy_fixture("get_expected_output"))])
def test_leadernboard(ranking, player, expected_res):
    ranking = convert_to_int(ranking)
    player = convert_to_int(player)
    expected_res = convert_to_int(expected_res)
    res = get_player_leaderborad(ranking, player)
    assert res == expected_res