from functools import wraps
from time import time
import requests
import requests_cache
from sportsreference.soccer.mls.teams import Teams

requests_cache.install_cache('cache', backend='sqlite', expire_after=30000)


def timeit(f):
    def timed(*args, **kw):
        start = time()
        result = f(*args, **kw)
        end = time()
        if len(args) > 0:
            print("%r %s  %2.2f ms" % (f.__name__, args[0], (end-start)*1000))
        else:
            print("%r %2.2f ms" % (f.__name__, (end - start) * 1000))
        return result
    return timed


@timeit
def find_current_year_teams():
    current_mls_teams = Teams()
    for team in current_mls_teams:
        print("%r %d-%d-%d" % (team.name, team.wins, team.losses, team.draws))


@timeit
def find_teams(year):
    current_mls_teams = Teams(str(year))
    for team in current_mls_teams:
        print("%r %d-%d" % (team.name, team.wins, team.losses))


if __name__ == "__main__":

    for year in range(1996, 2019):
        find_teams(year)
    find_current_year_teams()
