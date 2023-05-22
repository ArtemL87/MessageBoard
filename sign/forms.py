from django.contrib.auth.models import Group
from Board.models import User

class BasicSignupForm(SignupForm):

    def save(self, request):
        user = super(BasicSignupForm, self).save(request)
        basic_group = Group.objects.get(name='fans')
        basic_group.user_set.add(user)
        User.objects.create(username=user)
        return user