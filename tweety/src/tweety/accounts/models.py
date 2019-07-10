from django.db import models
from django.conf import settings
from django.urls import reverse_lazy
from django.db.models.signals import post_save
# Create your models here.

class UserProfileManager(models.Manager):
    use_for_related_fields = True

    def all(self):
        qs = self.get_queryset().all()
        try:
            if self.instance:
                qs = qs.exclude(user=self.instance)
        except:
            pass
        return qs

    def toggleFollow(self, user, toToggleUser):
        userProfile, created = UserProfile.objects.get_or_create(user=user)
        if toToggleUser in userProfile.following.all():
            userProfile.following.remove(toToggleUser)
            added = False
        else:
            userProfile.following.add(toToggleUser)
            added = True
        return added

    def isFollwoing(self, user, followedByUser):
        userProfile, created = UserProfile.objects.get_or_create(user=user)
        if created:
            return False
        if followedByUser in userProfile.following.all():
            return True
        return False

    def recommended(self, user, limitTo=10):
        profile = user.profile
        following = profile.get_following()
        print(following)
        qs = self.get_queryset().exclude(user__in=following).exclude(id=profile.id).order_by("?")[:limitTo]
        print(qs)
        return qs

class UserProfile(models.Model):
    user       = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='profile')
    following  = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='followed_by')

    # user.profile.following -> users i follow
    # user.followed_by -> users that follow me - reverse relationship

    objects = UserProfileManager()

    def __str__(self):
        return str(self.user.username)

    def get_following(self):
        return self.following.all().exclude(username=self.user.username)

    def get_follow_url(self):
        return reverse_lazy("profiles:follow", kwargs={"username":self.user.username})

    def get_absolute_url(self):
        return reverse_lazy("profiles:detail",kwargs={"username":self.user.username})
    

def post_save_user_receiver(sender, instance, created, *args, **kwargs):
    print(instance)
    if created:
        new_profile = UserProfile.objects.get_or_create(user=instance)

post_save.connect(post_save_user_receiver, sender=settings.AUTH_USER_MODEL)