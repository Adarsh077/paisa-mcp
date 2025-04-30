import requests
import config


def get_all_tags():
    response = requests.get(f"{config.api_baseurl}/tags")
    data = response.json()
    return data


def add_tag(label: str):
    response = requests.post(
        f"{config.api_baseurl}/tags",
        json={"label": label},
    )
    data = response.json()
    return data


def delete_tag(tagId: str):
    response = requests.delete(f"{config.api_baseurl}/tags/{tagId}")
    data = response.json()
    return data


def update_tag(tagId: str, label: str):
    response = requests.patch(
        f"{config.api_baseurl}/tags/{tagId}", json={"label": label}
    )
    data = response.json()
    return data
