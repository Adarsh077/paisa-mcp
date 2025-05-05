from . import transactions_api


def register(mcp):
    @mcp.tool()
    def get_all_transactions(
        tags: str = "",
        type: str = "",
        startDate: str = "",
        endDate: str = "",
    ) -> list:
        """
        Retrieve all transactions, optionally filtered by tags, type, and date range.

        Args:
            tags (str, optional): Comma-separated tag IDs to filter transactions.
            type (str, optional): Transaction type ('income' or 'expense').
            startDate (str, optional): Start date (ISO format) for filtering.
            endDate (str, optional): End date (ISO format) for filtering.

        Returns:
            list: List of transaction objects.
        """
        return transactions_api.get_all_transactions(
            tags=tags, type=type, startDate=startDate, endDate=endDate
        )

    @mcp.tool()
    def get_transaction_by_id(transactionId: str) -> dict:
        """
        Retrieve a single transaction by its ID.

        Args:
            transactionId (str): The unique identifier of the transaction.

        Returns:
            dict: The transaction object if found.
        """
        return transactions_api.get_transaction_by_id(transactionId)

    @mcp.tool()
    def create_transaction(
        label: str, amount: float, type: str, tags: list[str] = [], date: str = ""
    ) -> dict:
        """
        Create a new transaction.

        Args:
            label (str): The label for the transaction.
            amount (float): The amount for the transaction.
            type (str): The type of transaction ('income' or 'expense').
            tags (list[str], optional): List of tag IDs as strings.  # type: ignore[valid-type]
            date (str, optional): Date of the transaction (ISO format).

        Returns:
            dict: The newly created transaction object.
        """
        return transactions_api.create_transaction(
            label, amount, type, tags=tags, date=date
        )

    @mcp.tool()
    def update_transaction(
        transactionId: str,
        label: str = "",
        tags: list[str] = [],
        date: str = "",
        amount: float = 0.0,
    ) -> dict:
        """
        Update an existing transaction by its ID.

        Args:
            transactionId (str): The unique identifier of the transaction.
            label (str, optional): New label.
            tags (list[str], optional): New list of tag IDs.
            date (str, optional): New date (ISO format).
            amount (float, optional): New amount.

        Returns:
            dict: The updated transaction object.
        """
        return transactions_api.update_transaction(
            transactionId, label=label, tags=tags, date=date, amount=amount
        )

    @mcp.tool()
    def delete_transaction(transactionId: str) -> dict:
        """
        Soft delete a transaction by its ID.

        Args:
            transactionId (str): The unique identifier of the transaction to delete.

        Returns:
            dict: A message indicating the result of the delete operation.
        """
        return transactions_api.delete_transaction(transactionId)

    @mcp.tool()
    def search_transactions(
        label: str = "",
        tags: str = "",
        startDate: str = "",
        endDate: str = "",
        select: str = "",
    ) -> list:
        """
        Search transactions by label, tags, date range, and select fields.

        Args:
            label (str, optional): Search by label.
            tags (str, optional): Comma-separated tag IDs.
            startDate (str, optional): Start date (ISO format).
            endDate (str, optional): End date (ISO format).
            select (str, optional): Comma-separated fields to include in results.

        Returns:
            list: List of matching transaction objects.
        """
        return transactions_api.search_transactions(
            label=label, tags=tags, startDate=startDate, endDate=endDate, select=select
        )
