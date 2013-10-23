# models.py
# author = Jonathan Huang
from __future__ import unicode_literals

from django.db import models

class Demographic(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    start_date = models.TextField()
    end_date = models.TextField()
    gender = models.CharField(max_length=6L, blank=True)
    birth_year = models.IntegerField(null=True, blank=True)
    birth_country = models.TextField(blank=True)
    country = models.TextField(blank=True)
    countrytext = models.TextField(blank=True)
    hispanic = models.CharField(max_length=16L, blank=True)
    native_american = models.IntegerField()
    east_asian = models.IntegerField()
    south_asian = models.IntegerField()
    other_asian = models.IntegerField()
    black = models.IntegerField()
    hawaiian = models.IntegerField()
    white = models.IntegerField()
    decline = models.IntegerField()
    education_level = models.TextField(blank=True)
    current_student = models.CharField(max_length=40L, blank=True)
    current_program = models.TextField(blank=True)
    agriculture = models.IntegerField()
    architecture = models.IntegerField()
    culture_studies = models.IntegerField()
    biology = models.IntegerField()
    business = models.IntegerField()
    communication = models.IntegerField()
    comm_tech = models.IntegerField()
    compsci = models.IntegerField()
    construction = models.IntegerField()
    education = models.IntegerField()
    engineering = models.IntegerField()
    engineeringtech = models.IntegerField()
    english = models.IntegerField()
    human_sciences = models.IntegerField()
    foreign_lang = models.IntegerField()
    health = models.IntegerField()
    law_enforcement = models.IntegerField()
    law = models.IntegerField()
    humanities = models.IntegerField()
    library_science = models.IntegerField()
    math_stat = models.IntegerField()
    mechanic = models.IntegerField()
    military_tech = models.IntegerField()
    interdisciplinary = models.IntegerField()
    fitness = models.IntegerField()
    culinary = models.IntegerField()
    philosophy = models.IntegerField()
    physical_sciences = models.IntegerField()
    precision_production = models.IntegerField()
    psych = models.IntegerField()
    social_services = models.IntegerField()
    history = models.IntegerField()
    theology = models.IntegerField()
    transportation = models.IntegerField()
    art = models.IntegerField()
    other_area = models.IntegerField()
    current_employment_status = models.TextField(blank=True)
    industry = models.TextField(blank=True)
    english_writing = models.CharField(max_length=36L, blank=True)
    english_reading = models.CharField(max_length=36L, blank=True)
    english_speaking = models.CharField(max_length=36L, blank=True)
    arabic = models.IntegerField()
    bengali = models.IntegerField()
    cantonese = models.IntegerField()
    mandarin = models.IntegerField()
    wu = models.IntegerField()
    french = models.IntegerField()
    german = models.IntegerField()
    hindi = models.IntegerField()
    italian = models.IntegerField()
    korean = models.IntegerField()
    japanese = models.IntegerField()
    javanese = models.IntegerField()
    malay_indonesian = models.IntegerField()
    persian = models.IntegerField()
    portuguese = models.IntegerField()
    punjabi = models.IntegerField()
    russian = models.IntegerField()
    spanish = models.IntegerField()
    telugu = models.IntegerField()
    vietnamese = models.IntegerField()
    marathi = models.IntegerField()
    tamil = models.IntegerField()
    thai = models.IntegerField()
    turkish = models.IntegerField()
    urdu = models.IntegerField()
    other_lang = models.IntegerField()
    comments = models.TextField(blank=True)
    age = models.IntegerField(null=True, blank=True)
    state = models.TextField()
    class Meta:
        db_table = 'demographic'

class ForumViewLog(models.Model):
    id = models.IntegerField(primary_key=True)
    log_user_id = models.CharField(max_length=120L)
    thread_id = models.IntegerField()
    timestamp = models.BigIntegerField()
    user_ip = models.CharField(max_length=255L)
    class Meta:
        db_table = 'forum_view_log'

class LogHashMapping(models.Model):
    user_id = models.IntegerField()
    log_user_id = models.CharField(max_length=255L, primary_key=True)
    class Meta:
        db_table = 'hash_mapping'

class VideoEventLog(models.Model):
    id = models.IntegerField(primary_key=True)
    log_user_id = models.CharField(max_length=120L)
    lecture_id = models.IntegerField()
    event_timestamp = models.BigIntegerField()
    user_ip = models.CharField(max_length=255L)
    ready_state = models.CharField(max_length=4L, blank=True)
    action = models.CharField(max_length=10L)
    network_state = models.CharField(max_length=4L, blank=True)
    error = models.CharField(max_length=4L, blank=True)
    playback_rate = models.CharField(max_length=4L, blank=True)
    paused = models.IntegerField()
    current_time = models.FloatField(null=True, blank=True)
    prev_time = models.FloatField(null=True, blank=True)
    class Meta:
        db_table = 'video_event_log'
