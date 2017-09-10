from .decorators import endpoint
from ..endpoints.transaction import *


class TransactionInterface(object):


    @endpoint(GETTransactions)
    def list(self, from_, to, pageSize, type):
        """
        Get a list of Transactions pages that satisfy a time-based Transaction
        query.

        Args:
            from:
                The starting time (inclusive) of the time range for the
                Transactions being queried.
            to:
                The ending time (inclusive) of the time range for the
                Transactions being queried.
            pageSize:
                The number of Transactions to include in each page of the
                results.
            type:
                A filter for restricting the types of Transactions to retrieve.

        Returns:
            v20.response.Response containing the results from submitting the
            request
        """
        pass


    @endpoint(GETTransactionID)
    def get(self, transactionID):
        """
        Get the details of a single Account Transaction.

        Args:
            transactionID:
                A Transaction ID

        Returns:
            v20.response.Response containing the results from submitting the
            request
        """
        pass

    # TODO Dont forget to handle for the _ on arg names
    @endpoint(GETIDrange)
    def range(self, from_, to, type_):
        """
        Get a range of Transactions for an Account based on the Transaction
        IDs.

        Args:
            from_:
                The starting Transaction ID (inclusive) to fetch.
            to:
                The ending Transaction ID (inclusive) to fetch.
            type_:
                The filter that restricts the types of Transactions to
                retrieve.

        Returns:
            v20.response.Response containing the results from submitting the
            request
        """
        pass


    @endpoint(GETSinceID)
    def since(self, id):
        """
        Get a range of Transactions for an Account starting at (but not
        including) a provided Transaction ID.

        Args:
            id:
                The ID of the last Transaction fetched. This query will return
                all Transactions newer than the TransactionID.

        Returns:
            v20.response.Response containing the results from submitting the
            request
        """
        pass

    # TODO think about the line parser you deleted here!
    @endpoint(GETTransactionsStream)
    def stream(self):
        """
        Get a stream of Transactions for an Account starting from when the
        request is made.

        Args:

        Returns:
            v20.response.Response containing the results from submitting the
            request
        """
        pass