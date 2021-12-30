from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone

# Create your models here.
class ListaAmigos(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')
    friends = models.ManyToManyField(User, blank=True, related_name='friends')

    def __str__(self):
        return self.user.username


    def add_friend(self, perfil):
        if not perfil in self.friends.all():
            self.friends.add(perfil)

        
    def remove_friend(self, friend):
        if friend in self.friends.all():
            self.friends.remove(friend)

    def unfriend(self, friend):

        remover_friends_list = self
        remover_friends_list.remove_friend(friend)
        friend_list = ListaAmigos.objects.get(user=friend)
        friend_list.remove_friend(self.user)



    def is_friend(self, friend):
        if friend in self.friends.all():
            return True
        return False


class SolicitacaoAmigo(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    reciever = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reciever')
    is_active = models.BooleanField(default=True, blank=True, null=False)
    data_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.sender.username

    def accept(self):
        reciever_friends_list = ListaAmigos.objects.get(user=self.reciever)
        sender_friends_list = ListaAmigos.Objects.get(user=self.sender)

        if reciever_friends_list and sender_friends_list:
            reciever_friends_list.add_friend(self.sender)
            sender_friends_list.add_friend(self.reciever)
            self.is_active = False
            self.save()
            

    def decline(self):
        self.is_active = False
        self.save()

    def cancel(self):
        self.is_active = False
        self.save()