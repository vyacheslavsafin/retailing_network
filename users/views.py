from rest_framework.generics import CreateAPIView
from users.serializers import UserSerializer


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        user.set_password(serializer.data.get('password'))
        user.save()
