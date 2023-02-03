from environs import Env
from .models import Teaser, Author

env = Env()
env.read_env()


def request_data_processing(serializer_obj):
    result = {}
    for req_data in serializer_obj.data:
        teaser = Teaser.objects.get(id=req_data.get('id'))
        result.update({teaser.pk: -1})
        if teaser.status == '':
            status = req_data.get('status')
            update_teaser(teaser, status)
            if status == 'paid':
                update_author(teaser)
            result.update({teaser.pk: 0})
    return result


def update_teaser(teaser, status):
    teaser.status = status
    teaser.save()


def update_author(teaser):
    author = Author.objects.get(id=teaser.author.pk)
    payment = author.money + env.int("PAYMENT")
    author.money = payment
    author.save()