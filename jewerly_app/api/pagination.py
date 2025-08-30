from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class PaginationPageSize(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

    def get_paginated_response(self, data):
        return Response({
            'total': self.page.paginator.count,
            'page': self.page.number,
            'entries': data
        })
