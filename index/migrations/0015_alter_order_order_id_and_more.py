# Generated by Django 5.2.2 on 2025-06-12 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0014_alter_role_permission_unique_together_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='Order_ID',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterUniqueTogether(
            name='role_permission',
            unique_together={('Role_ID', 'Perm_ID')},
        ),
        migrations.AlterUniqueTogether(
            name='user_role',
            unique_together={('User_ID', 'Role_ID')},
        ),
    ]
