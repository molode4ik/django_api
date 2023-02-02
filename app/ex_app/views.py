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
        print(request.user)

        serializer_obj = TeaserSerializer(data=request.data)
        if serializer_obj.is_valid():
            author = Author.objects.get(id=serializer_obj.data.get('author'))
            new_teaser = Teaser.objects.create(title=serializer_obj.data.get('title'),
                                               description=serializer_obj.data.get('description'),
                                               category=serializer_obj.data.get('category'), author=author)
            return Response(0)
        return Response(-1)


class WorkTeasersView(APIView):
    serializer_class = WorkTeasersSerializer
    permission_classes = [ChangeAndView]

    def get(self, request):
        teasers = Teaser.objects.all().values()
        return Response(teasers)

    def post(self, request):
        serializer_obj = WorkTeasersSerializer(data=request.data)
        if serializer_obj.is_valid():
            print(request.data)
            teaser = Teaser.objects.all().filter(id=serializer_obj.data.get('id'))
            if teaser.first().status == '':
                status = serializer_obj.data.get('status')
                teaser.update(status=status)
                if status == 'paid':
                    author = Author.objects.all().filter(id=teaser.first().author.pk)
                    new_value = author.first().money + env.int("MONEY_UPDATE")
                    author.update(money=new_value)
                return Response(0)
        return Response(-1)
