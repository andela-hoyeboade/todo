from api.serializers import BucketlistSerializer
from bucket.models import Bucketlist
from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response


class LoginView(ObtainAuthToken):

    """
    Returns a generated token
    """

    def post(self, request):
        username, password = request.data.get(
            'username'), request.data.get('password')
        if not username:
            return Response({'message':
                             'Username not provided.'},
                            status=status.HTTP_400_BAD_REQUEST)
        if not password:
            return Response({'message':
                             'Password not provided.'},
                            status=status.HTTP_400_BAD_REQUEST)
        if not User.objects.filter(username=username):
            return Response({'message':
                             'Username does not exist.'},
                            status=status.HTTP_400_BAD_REQUEST)
        # try:
        #user = User.objects.filter(username=username).first()
        # return Response({'data': {'username': user.username, 'password':
        # user.password}})
        return super(LoginView, self).post(request)
        # except:
        # return Response({'message': 'Password incorrect.'},
        #                    status=status.HTTP_400_BAD_REQUEST)


class BucketlistViewSets(viewsets.ModelViewSet):

    serializer_class = BucketlistSerializer
    queryset = Bucketlist.objects.all()

    def list(self, request):
        queryset = Bucketlist.objects.filter(owner=request.user)
        serializer = BucketlistSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = BucketlistSerializer(
            data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'message': 'Name missing'}, status=status.HTTP_400_BAD_REQUEST)


# class SingleBucketlistViewSets(viewsets.ModelViewSet):
#     serializer_class = BucketlistSerializer
#     queryset = Bucketlist.objects.all()
#
#     def retrieve(self, request, pk=None):
#         user = User.objects.get(username='migwi')
#         bucketlist = Bucketlist.objects.filter(pk=pk, owner=user)
#         if bucketlist:
#             return BucketlistSerializer(bucketlist)
#         return Response({'message': 'Not found'}, status=404)
