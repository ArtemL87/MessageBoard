from django.db.models.signals import post_save
from django.dispatch import receiver # импортируем нужный декоратор
from django.core.mail import send_mail
from django.contrib.auth.models import User
from .models import Post, Comment


@receiver(post_save, sender=Post)
def new_post(sender, instance, created, **kwargs):

    send_mail(
        subject=f'{instance.title_post}',
        message=f'{instance.text_post}',
        from_email='artem.l.1987@yandex.ru',
        recipient_list=[i['email'] for i in User.objects.all().values('email')]
    )

@receiver(post_save, sender=Comment)
def new_post(sender, instance, created, **kwargs):

    send_mail(
        subject=f'У Вас новый коментарий',
        message=f'Прочитать по ссылке http://127.0.0.1:8000/post/comment/{instance.id}',
        from_email='artem.l.1987@yandex.ru',
        recipient_list=[instance.post_com.author.email, ]
    )
    print(instance.post_com.author.email)