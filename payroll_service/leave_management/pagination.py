# leave_management/pagination.py

from rest_framework.pagination import PageNumberPagination

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10  # Adjust the number of items per page as needed
    page_size_query_param = 'page_size'
    max_page_size = 100
