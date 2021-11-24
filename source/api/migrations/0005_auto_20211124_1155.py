# Generated by Django 2.2.10 on 2021-11-24 11:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20211124_1128'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='option',
            name='survey',
        ),
        migrations.AddField(
            model_name='option',
            name='question',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='options', to='api.Question', verbose_name='Вопрос'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='option',
            name='text',
            field=models.CharField(max_length=500, verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='question',
            name='survey',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='api.Survey', verbose_name='Опрос'),
        ),
        migrations.AlterField(
            model_name='question',
            name='text',
            field=models.CharField(max_length=500, verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='question',
            name='type',
            field=models.CharField(choices=[('text', 'text'), ('one_option', 'one_option'), ('plural_option', 'plural_option')], default='text', max_length=30, verbose_name='Тип'),
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.IntegerField()),
                ('text', models.CharField(blank=True, max_length=500, null=True)),
                ('option', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='option_answers', to='api.Option')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='question_answers', to='api.Question')),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='survey_answers', to='api.Survey')),
            ],
        ),
    ]
