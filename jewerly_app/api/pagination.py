from rest_framework.pagination import PageNumberPagination


class PaginationPageSize(PageNumberPagination):
    page_size = 10