from rest_framework import generics, status, viewsets, serializers
from rest_framework.response import Response
from .models import Contact, Spam
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
import logging

logger = logging.getLogger(__name__)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
    
class UserSerializerRead(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'name', 'phone_number']

    def create(self, validated_data):
        user = User.objects.create_user(
            name=validated_data['name'],
            phone_number=validated_data['phone_number'])
        return Contact.objects.create(**validated_data)

class SpamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spam
        fields = ['id', 'phone_number', 'likelihood']

class UserRegistration(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        logger.debug(f"Received data: {request.data}")
        response = super().create(request, *args, **kwargs)
        logger.debug(f"Response data: {response.data}")
        return response

class UserLogin(generics.GenericAPIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

class ContactSearch(generics.ListAPIView):
    serializer_class = ContactSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        query = self.request.query_params.get('query', '')
        start_with_results = Contact.objects.filter(name__istartswith=query)
        contains_results = Contact.objects.filter(name__icontains=query).exclude(pk__in=start_with_results)
        return start_with_results | contains_results
    
    def perform_create(self, serializer):
        name = self.request.query_params.get('name', '')
        phone_number = self.request.query_params.get('phone_number', '')
        serializer.save(name=name, phone_number=phone_number)

class PhoneSearch(generics.ListAPIView):
    serializer_class = ContactSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        phone_number = self.request.query_params.get('phone', '')
        registered_user = Contact.objects.filter(phone_number=phone_number).first()
        if registered_user:
            return Contact.objects.filter(pk=registered_user.pk)
        else:
            return Contact.objects.filter(phone_number__icontains=phone_number)
        
class ContactDetail(generics.RetrieveAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

class SpamViewSet(viewsets.ModelViewSet):
    queryset = Spam.objects.all()
    serializer_class = SpamSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
