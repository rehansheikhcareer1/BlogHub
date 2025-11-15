import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog_project.settings')
django.setup()

from django.contrib.auth.models import User
from accounts.models import UserProfile

# Create profiles for existing users
for user in User.objects.all():
    profile, created = UserProfile.objects.get_or_create(user=user)
    if created:
        print(f"✅ Profile created for {user.username}")
    else:
        print(f"ℹ️  Profile already exists for {user.username}")

print("\n✅ All users now have profiles!")
