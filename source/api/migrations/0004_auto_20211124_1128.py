# Generated by Django 2.2.10 on 2021-11-24 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20211124_0947'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name': 'Вопрос', 'verbose_name_plural': 'Вопросы'},
        ),
        migrations.AlterField(
            model_name='question',
            name='type',
            field=models.CharField(choices=[('text', 'text'), ('one_option', 'one_option'), ('plural_option', 'plural_option')], default='text', max_length=30),
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=500)),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='api.Question')),
            ],
            options={
                'verbose_name': 'Вариант',
                'verbose_name_plural': 'Варианты',
            },
        ),
    ]
