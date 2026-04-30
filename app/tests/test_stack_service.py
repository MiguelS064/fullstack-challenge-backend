from unittest.mock import patch
from app.services.stack_service import (
    get_answered_stats,
    get_max_reputation,
    get_min_views,
    get_oldest,
    get_newest,
)

MOCK_DATA = [
    {
        "is_answered": True,
        "title": "Perl question A",
        "view_count": 100,
        "creation_date": 1000,
        "link": "http://a.com",
        "answer_count": 2,
        "owner": {"reputation": 500, "display_name": "UserA"},
    },
    {
        "is_answered": False,
        "title": "Perl question B",
        "view_count": 5,
        "creation_date": 3000,
        "link": "http://b.com",
        "answer_count": 0,
        "owner": {"reputation": 200, "display_name": "UserB"},
    },
    {
        "is_answered": True,
        "title": "Perl question C",
        "view_count": 300,
        "creation_date": 500,
        "link": "http://c.com",
        "answer_count": 5,
        "owner": {"reputation": 800, "display_name": "UserC"},
    },
]


# Todos los tests mockean get_data (tu función interna)
# así no se hace ninguna llamada HTTP real

@patch("app.services.stack_service.get_data", return_value=MOCK_DATA)
def test_answered_stats(mock):
    result = get_answered_stats()
    assert result["answered"] == 2
    assert result["unanswered"] == 1


@patch("app.services.stack_service.get_data", return_value=MOCK_DATA)
def test_max_reputation(mock):
    result = get_max_reputation()
    assert result["reputation"] == 800
    assert result["user"] == "UserC"


@patch("app.services.stack_service.get_data", return_value=MOCK_DATA)
def test_min_views(mock):
    result = get_min_views()
    assert result["view_count"] == 5
    assert result["user"] == "UserB"


@patch("app.services.stack_service.get_data", return_value=MOCK_DATA)
def test_oldest(mock):
    result = get_oldest()
    assert result["creation_date"] == 500
    assert result["user"] == "UserC"


@patch("app.services.stack_service.get_data", return_value=MOCK_DATA)
def test_newest(mock):
    result = get_newest()
    assert result["creation_date"] == 3000
    assert result["user"] == "UserB"