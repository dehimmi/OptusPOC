import pytest


def test_pass():
    assert 1+1 == 3


#client.write_points(result, database='pythondb', time_precision='ms')

# python -m pytest test_example.py --pytest-influxdb --influxdb_host=localhost --influxdb_name=pythondb

# python -m pytest test_example.py --pytest-influxdb --influxdb_host=52.63.126.230 --influxdb_name=pythondb
