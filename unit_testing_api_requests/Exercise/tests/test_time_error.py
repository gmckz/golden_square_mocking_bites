from lib.time_error import *
from unittest.mock import Mock

def test_error_returns_correct_time_difference():
    request_mock = Mock()
    response_mock = Mock()
    response_mock.json.return_value = {"unixtime":1687266649}
    request_mock.get.return_value = response_mock
    time_mock = Mock()
    time_mock.time.return_value = 1687266549
    time_error = TimeError(request_mock, time_mock)
    assert time_error.error() == 100








