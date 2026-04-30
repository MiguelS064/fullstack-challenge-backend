import requests

URL = "https://api.stackexchange.com/2.2/search?order=desc&sort=activity&intitle=perl&site=stackoverflow"

def get_data():
    return requests.get(URL).json()["items"]


def get_answered_stats():
    data = get_data()
    answered = sum(1 for x in data if x["is_answered"])
    unanswered = len(data) - answered

    return {
        "answered": answered,
        "unanswered": unanswered
    }


def get_max_reputation():
    data = get_data()
    max_rep = max(data, key=lambda x: x["owner"].get("reputation", 0))

    print("Mayor reputación:", max_rep["title"])

    return {
        "title": max_rep["title"],
        "reputation": max_rep["owner"]["reputation"],
        "user": max_rep["owner"]["display_name"],
        "link": max_rep["link"],
        "answer_count" : max_rep["answer_count"]
    }


def get_min_views():
    data = get_data()
    min_views = min(data, key=lambda x: x["view_count"])

    print("Menor vistas:", min_views["title"])

    return {
        "title": min_views["title"],
        "reputation": min_views["owner"]["reputation"],
        "user": min_views["owner"]["display_name"],
        "link": min_views["link"],
        "view_count" : min_views["view_count"]
    }


def get_oldest():
    data = get_data()
    oldest = min(data, key=lambda x: x["creation_date"])

    print("Más vieja:", oldest["title"])

    return {
        "title": oldest["title"],
        "reputation": oldest["owner"]["reputation"],
        "user": oldest["owner"]["display_name"],
        "link": oldest["link"],
        "creation_date" : oldest["creation_date"]
    }


def get_newest():
    data = get_data()
    newest = max(data, key=lambda x: x["creation_date"])

    print("Más nueva:", newest["title"])

    return {
        "title": newest["title"],
        "reputation": newest["owner"]["reputation"],
        "user": newest["owner"]["display_name"],
        "link": newest["link"],
        "creation_date" : newest["creation_date"]
    }