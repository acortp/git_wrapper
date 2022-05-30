from django.db import migrations


def create_admin_user(apps, schema_editor):
    from django.contrib.auth import get_user_model
    from django.conf import settings

    admin = get_user_model().objects.create_superuser(
        username=settings.DJANGO_ADMIN_NAME,
        email=settings.DJANGO_ADMIN_EMAIL,
        password=settings.DJANGO_ADMIN_PASSWORD,
        git_access_token=settings.ADMIN_GIT_TOKEN
    )

    admin.save()


class Migration(migrations.Migration):
    dependencies = [("users", "0001_initial")]

    operations = [
        migrations.RunPython(create_admin_user)
    ]