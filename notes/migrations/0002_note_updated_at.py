from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='updated_at',
            # Existing rows need *some* value for this new NOT NULL column.
            # default=timezone.now fills them in once; preserve_default=False
            # tells Django not to keep that default in the model itself,
            # because the field uses auto_now=True going forward instead.
            field=models.DateTimeField(auto_now=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
