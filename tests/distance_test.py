# tests/distance_test.py
from first_project.lib import haversine

def test_haversine():
    assert type(haversine(lon1, lat1, lon2, lat2)) != str



