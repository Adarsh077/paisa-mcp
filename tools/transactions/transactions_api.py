import requests
import config


def get_transaction_by_id(transactionId, jwt_token=None):
    headers = {"Authorization": f"Bearer {jwt_token}"} if jwt_token else {}

    response = requests.get(
        f"{config.api_baseurl}/transactions/{transactionId}", headers=headers
    )
    return response.json()


def create_transaction(label, amount, type, tags=[], date=None, jwt_token=None):
    headers = {"Authorization": f"Bearer {jwt_token}"} if jwt_token else {}

    data = {"label": label, "amount": amount, "type": type}
    if len(tags) > 0:
        data["tags"] = tags
    if date is not None:
        data["date"] = date
    response = requests.post(
        f"{config.api_baseurl}/transactions", json=data, headers=headers
    )
    return response.json()


def update_transaction(
    transactionId, label=None, tags=None, date=None, amount=None, jwt_token=None
):
    headers = {"Authorization": f"Bearer {jwt_token}"} if jwt_token else {}

    update = {}
    if label is not None:
        update["label"] = label
    if tags is not None:
        update["tags"] = tags
    if date is not None:
        update["date"] = date
    if amount is not None:
        update["amount"] = amount
    response = requests.patch(
        f"{config.api_baseurl}/transactions/{transactionId}",
        json=update,
        headers=headers,
    )
    return response.json()


def delete_transaction(transactionId, jwt_token=None):
    headers = {"Authorization": f"Bearer {jwt_token}"} if jwt_token else {}

    response = requests.delete(
        f"{config.api_baseurl}/transactions/{transactionId}", headers=headers
    )
    return response.json()


def search_transactions(
    label=None,
    tags=None,
    startDate=None,
    endDate=None,
    select=None,
    page=None,
    limit=None,
    type=None,
    jwt_token=None,
):
    headers = {"Authorization": f"Bearer {jwt_token}"} if jwt_token else {}

    params = {}
    if label:
        params["label"] = label
    if tags:
        if tags.lower() == "none":
            params["tags"] = []
        else:
            params["tags"] = tags
    if startDate:
        params["startDate"] = startDate
    if endDate:
        params["endDate"] = endDate
    if select:
        params["select"] = select
    if page:
        params["page"] = page
    if limit:
        params["limit"] = limit
    if type:
        params["type"] = type
    response = requests.get(
        f"{config.api_baseurl}/transactions/search", params=params, headers=headers
    )
    return response.json()
