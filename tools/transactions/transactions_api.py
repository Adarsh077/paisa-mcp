import requests
import config


def get_transaction_by_id(transactionId):
    response = requests.get(f"{config.api_baseurl}/transactions/{transactionId}")
    return response.json()


def create_transaction(label, amount, type, tags=[], date=None):
    data = {"label": label, "amount": amount, "type": type}
    if len(tags) > 0:
        data["tags"] = tags
    if date is not None:
        data["date"] = date
    response = requests.post(f"{config.api_baseurl}/transactions", json=data)
    return response.json()


def update_transaction(transactionId, label=None, tags=None, date=None, amount=None):
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
        f"{config.api_baseurl}/transactions/{transactionId}", json=update
    )
    return response.json()


def delete_transaction(transactionId):
    response = requests.delete(f"{config.api_baseurl}/transactions/{transactionId}")
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
):
    params = {}
    if label:
        params["label"] = label
    if tags:
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
    response = requests.get(f"{config.api_baseurl}/transactions/search", params=params)
    return response.json()
