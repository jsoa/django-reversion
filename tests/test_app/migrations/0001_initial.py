# Generated by Django 3.1.2 on 2020-10-16 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('reversion', '0001_squashed_0004_auto_20160611_1202'),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='v1', max_length=191)),
            ],
        ),
        migrations.CreateModel(
            name='TestModelEscapePK',
            fields=[
                ('name', models.CharField(max_length=191, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='TestModelInline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inline_name', models.CharField(default='v1', max_length=191)),
                ('test_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_app.testmodel')),
            ],
        ),
        migrations.CreateModel(
            name='TestModelRelated',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='v1', max_length=191)),
            ],
        ),
        migrations.CreateModel(
            name='TestModelWithNaturalKey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='v1', max_length=191)),
            ],
        ),
        migrations.CreateModel(
            name='TestModelParent',
            fields=[
                ('testmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='test_app.testmodel')),
                ('parent_name', models.CharField(default='parent v1', max_length=191)),
            ],
            bases=('test_app.testmodel',),
        ),
        migrations.CreateModel(
            name='TestModelThrough',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='v1', max_length=191)),
                ('test_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='test_app.testmodel')),
                ('test_model_related', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='test_app.testmodelrelated')),
            ],
        ),
        migrations.CreateModel(
            name='TestModelNestedInline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nested_inline_name', models.CharField(default='v1', max_length=191)),
                ('test_model_inline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_app.testmodelinline')),
            ],
        ),
        migrations.CreateModel(
            name='TestModelInlineByNaturalKey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_app.testmodelwithnaturalkey')),
            ],
        ),
        migrations.CreateModel(
            name='TestModelGenericInline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.IntegerField()),
                ('inline_name', models.CharField(default='v1', max_length=191)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
            ],
        ),
        migrations.AddField(
            model_name='testmodel',
            name='related',
            field=models.ManyToManyField(blank=True, related_name='_testmodel_related_+', to='test_app.TestModelRelated'),
        ),
        migrations.AddField(
            model_name='testmodel',
            name='related_through',
            field=models.ManyToManyField(blank=True, related_name='_testmodel_related_through_+', through='test_app.TestModelThrough', to='test_app.TestModelRelated'),
        ),
        migrations.CreateModel(
            name='TestMetaWithNullRevision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=191)),
                ('revision', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='reversion.revision')),
            ],
        ),
        migrations.CreateModel(
            name='TestMeta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=191)),
                ('revision', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reversion.revision')),
            ],
        ),
    ]
