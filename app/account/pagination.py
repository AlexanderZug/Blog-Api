from rest_framework.pagination import PageNumberPagination


class UserPostsPagination(PageNumberPagination):
    page_size = 10
