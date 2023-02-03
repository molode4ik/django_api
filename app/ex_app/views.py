from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import BasePermission
from .models import *
from .serializers import *
from .scripts import request_data_processing


class ViewOnly(BasePermission):
    def has_permission(self, request, view):
        if request.user.has_perm('ex_app.view_teaser'):
            return True


class ChangeAndView(BasePermission):
    def has_permission(self, request, view):
        if request.user.has_perm('ex_app.change_teaser'):
            return True


class TeaserView(APIView):
    serializer_class = TeaserSerializer
    permission_classes = [ViewOnly]

    def get(self, request):
        teasers = Teaser.objects.all().values()
        return Response(teasers)

    def post(self, request):
        serializer_obj = TeaserSerializer(data=request.data)
        author = Author.objects.all().filter(user_id=request.user.id)
        if serializer_obj.is_valid() and author:
            Teaser.objects.create(title=serializer_obj.data.get('title'),
                                  description=serializer_obj.data.get('description'),
                                  category=serializer_obj.data.get('category'),
                                  author=author[0])
            return Response(0)
        return Response(-1)


class WorkTeasersView(APIView):
    serializer_class = WorkTeasersSerializer
    permission_classes = [ChangeAndView]

    def get(self, request):
        teasers = Teaser.objects.all().values()
        return Response(teasers)

    def post(self, request):
        data_list = request.data
        if not isinstance(request.data, list):
            data_list = [request.data]
        serializer_obj = WorkTeasersSerializer(data=data_list, many=True)
        if serializer_obj.is_valid():
            response = request_data_processing(serializer_obj)
            return Response(response)
        return Response(-1)
