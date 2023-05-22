# Generated by Django 4.2.1 on 2023-05-17 13:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Board', '0003_alter_post_author_alter_post_category_com_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_com',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_com', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='comment',
            name='user_com',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Board.user_com'),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Board.user_com'),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
