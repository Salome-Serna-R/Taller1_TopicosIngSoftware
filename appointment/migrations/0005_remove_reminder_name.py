
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0004_reminder_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reminder',
            name='name',
        ),
    ]
