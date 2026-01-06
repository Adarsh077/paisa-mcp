def format_tag(tag):
    return {"_id": tag["_id"], "label": tag["label"]}


def format_tags(tags):
    formatted_tags = []
    for tag in tags:
        formatted_tags.append(format_tag(tag))
    return formatted_tags
