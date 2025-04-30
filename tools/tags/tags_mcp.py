from . import tags_api
from . import tags_formatter


def register(mcp):
    @mcp.tool()
    def get_all_tags() -> list:
        """
        Retrieve all tags from the system.

        Returns:
            list: A list of tag objects, each containing the tag's ID and label.
        """
        tags = tags_api.get_all_tags()
        return tags_formatter.format_tags(tags)

    @mcp.tool()
    def add_tag(label: str) -> dict:
        """
        Add a new tag with the given label.

        Args:
            label (str): The label for the new tag. This field is required.

        Returns:
            dict: The newly created tag object, containing its ID and label.
        """
        tag = tags_api.add_tag(label=label)
        return tags_formatter.format_tag(tag)

    @mcp.tool()
    def delete_tag(tagId: str) -> dict:
        """
        Soft delete a tag by its ID. The tag will be marked as deleted but not removed from the database.

        Args:
            tagId (str): The unique identifier of the tag to delete.

        Returns:
            dict: A message indicating the result of the delete operation.
        """
        response = tags_api.delete_tag(tagId)
        return response

    @mcp.tool()
    def update_tag(tagId: str, label: str) -> dict:
        """
        Update the label of an existing tag by its ID.

        Args:
            tagId (str): The unique identifier of the tag to update.
            label (str): The new label for the tag. This field is required.

        Returns:
            dict: The updated tag object, containing its ID and new label.
        """
        tag = tags_api.update_tag(tagId, label=label)
        return tags_formatter.format_tag(tag)
