
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='course',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='trainee',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=50)),
                ('NationalNumber', models.IntegerField(null=True)),
                ('Branch', models.IntegerField(null=True)),
                ('Course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trainee.course')),
            ],
        ),
    ]
