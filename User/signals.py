from django.db.models.signals import post_save, post_delete
from .models import Profile
from Project.models import Member

from django.core.mail import send_mail
from django.conf import settings


#---------------------create a profile automatically once member is created using sigals------#
 #    
def createProfile(sender, instance, created, **kwargs):
    if created:
        member = instance # instance is the instance of the sender
        profile = Profile.objects.create(
            member = member,
            name = member.f_name,
            address = member.address,
            age = member.age,
            sex = member.sex,
            phone = member.mobile_number,
            picture = member.profile_pic,

        )
        subject = 'Welcome to Gym'
        message = f' Hello Train Hard. Your {member.package_selected}package has been activated'
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [member.email],
            fail_silently=False
        )
    
post_save.connect(createProfile, sender=Member)


#---------------------------------------------------------------------------------------------------------#
#--------------if we want to delete member if profile is deleted run this function-------#
# def profileDeleted(sender, instance, **kwargs):
#     member = instance.member
#     member.delete()
#----------------------------------------------------------------------------------------------------#


# post_delete.connect(profileDeleted, sender=Profile) 

