from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated, BasePermission
from django.contrib.auth.decorators import permission_required
from environs import Env
from .models import *
from .serializers import *

env = Env()
env.read_env()


class ViewOnly(BasePermission):
    def has_permission(self, request, view):
        if request.user.has_perm('ex_app.view_teaser'):
            return True


class ChangeAndView(BasePermission):
    def has_permission(self, request, view):
        if request.user.has_perm('ex_app.view_teaser') and request.user.has_perm('ex_app.change_teaser'):
            return True


class TeaserView(APIView):
    serializer_class = TeaserSerializer
    permission_classes = [ViewOnly]

    def get(self, request):
        teasers = Teaser.objects.all().values()
        return Response(teasers)

    def post(self, request):
        serializer_obj = TeaserSerializer(data=request.data)
        #print(request.data)
        if serializer_obj.is_valid():
            Teaser.objects.create(title=serializer_obj.data.get('title'),
                                  description=serializer_obj.data.get('description'),
                                  category=serializer_obj.data.get('category'),
                                  author=Author.objects.get(id=serializer_obj.data.get('author')))
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
            for req_data in serializer_obj.data:
                teaser = Teaser.objects.get(id=req_data.get('id'))
                if teaser.status == '':
                    status = req_data.get('status')
                    teaser.status = status
                    if status == 'paid':
                        author = Author.objects.get(id=teaser.author.pk)
                        payment = author.money + env.int("PAYMENT")
                        author.money = payment
                        author.save()
                    teaser.save()
            return Response(0)
        return Response(-1)
