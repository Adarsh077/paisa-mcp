from . import tags_api
from . import tags_formatter
import logging


def register(mcp):
    @mcp.tool()
    def get_all_tags(jwt_token: str = "") -> list:
        """
        Retrieve all tags from the system.

        Args:
            jwt_token (str): Authentication token. Leave empty if not required.

        Returns:
            list: A list of tag objects, each containing the tag's ID and label.
        """
        jwt_token_value = jwt_token if jwt_token else None
        tags = tags_api.get_all_tags(jwt_token=jwt_token_value)
        return tags_formatter.format_tags(tags)

    @mcp.tool()
    def add_tag(label: str, jwt_token: str = "") -> dict:
        """
        Add a new tag with the given label.

        Args:
            label (str): The label for the new tag. This field is required.
            jwt_token (str): Authentication token. Leave empty if not required.

        Returns:
            dict: The newly created tag object, containing its ID and label.
        """
        jwt_token_value = jwt_token if jwt_token else None
        tag = tags_api.add_tag(label=label, jwt_token=jwt_token_value)
        return tags_formatter.format_tag(tag)

    @mcp.tool()
    def delete_tag(tagId: str, jwt_token: str = "") -> dict:
        """
        Soft delete a tag by its ID. The tag will be marked as deleted but not removed from the database.

        Args:
            tagId (str): The unique identifier of the tag to delete.
            jwt_token (str): Authentication token. Leave empty if not required.

        Returns:
            dict: A message indicating the result of the delete operation.
        """
        jwt_token_value = jwt_token if jwt_token else None
        response = tags_api.delete_tag(tagId, jwt_token=jwt_token_value)
        return response

    @mcp.tool()
    def update_tag(tagId: str, label: str, jwt_token: str = "") -> dict:
        """
        Update the label of an existing tag by its ID.

        Args:
            tagId (str): The unique identifier of the tag to update.
            label (str): The new label for the tag. This field is required.
            jwt_token (str): Authentication token. Leave empty if not required.

        Returns:
            dict: The updated tag object, containing its ID and new label.
        """
        jwt_token_value = jwt_token if jwt_token else None
        tag = tags_api.update_tag(tagId, label=label, jwt_token=jwt_token_value)
        return tags_formatter.format_tag(tag)
