from rest_framework import pagination
from rest_framework.response import Response

class CustomPagination(pagination.PageNumberPagination):
    page_size = 5
    max_page_size = 10
    page_size_query_param = 'count'
    
    def get_paginated_response(self, data):
        return Response({
            'results': data,
            'page_number': self.page.number,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'count': self.page.paginator.count,
            'page_size': self.page.paginator.per_page.real,
        })

