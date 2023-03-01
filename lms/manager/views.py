from rest_framework.permissions import IsAuthenticatedOrReadOnly, SAFE_METHODS
from rest_framework.viewsets import ModelViewSet

from .models import Group, Course, Category, Audience, Address
from .serializers import GroupSerializer, CourseSerializer, CategorySerializer, AudienceSerializer, AddressSerializer


class IsManagerOrReadOnly(IsAuthenticatedOrReadOnly):

    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_authenticated and
            request.user.is_staff
        )


class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class AudienceViewSet(ModelViewSet):
    queryset = Audience.objects.all()
    serializer_class = AudienceSerializer


class AddressViewSet(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer