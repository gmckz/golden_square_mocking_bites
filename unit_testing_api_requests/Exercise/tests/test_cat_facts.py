from lib.cat_facts import *
from unittest.mock import Mock

def test_provide_returns_cat_fact():
    requester_mock = Mock()
    response_mock = Mock()
    response_mock.json.return_value = {"fact":"When a cats rubs up against you, the cat is marking you with it's scent claiming ownership.","length":91}
    requester_mock.get.return_value = response_mock

    cat_facts = CatFacts(requester_mock)
    assert cat_facts.provide() == "Cat fact: When a cats rubs up against you, the cat is marking you with it's scent claiming ownership."