from rest_framework.pagination import PageNumberPagination

class ProductPagination(PageNumberPagination):
    page_size = 10               # default items per page
    page_size_query_param = 'page_size'  # client can override ?page_size=20
    max_page_size = 50           # prevent excessive requests
