import requests
import config


def get_all_tags(jwt_token):
    headers = {"Authorization": f"Bearer {jwt_token}"} if jwt_token else {}

    response = requests.get(f"{config.api_baseurl}/tags", headers=headers)
    data = response.json()
    return data


def add_tag(label: str, jwt_token=None):
    headers = {"Authorization": f"Bearer {jwt_token}"} if jwt_token else {}

    response = requests.post(
        f"{config.api_baseurl}/tags", json={"label": label}, headers=headers
    )
    data = response.json()
    return data


def delete_tag(tagId: str, jwt_token=None):
    headers = {"Authorization": f"Bearer {jwt_token}"} if jwt_token else {}

    response = requests.delete(f"{config.api_baseurl}/tags/{tagId}", headers=headers)
    data = response.json()
    return data


def update_tag(tagId: str, label: str, jwt_token=None):
    headers = {"Authorization": f"Bearer {jwt_token}"} if jwt_token else {}

    response = requests.patch(
        f"{config.api_baseurl}/tags/{tagId}", json={"label": label}, headers=headers
    )
    data = response.json()
    return data
