from django.core.management.base import BaseCommand
from django.conf import settings
from djongo import models
from pymongo import MongoClient

# Sample data for population
def get_sample_data():
    users = [
        {"name": "Superman", "email": "superman@dc.com", "team": "dc"},
        {"name": "Batman", "email": "batman@dc.com", "team": "dc"},
        {"name": "Wonder Woman", "email": "wonderwoman@dc.com", "team": "dc"},
        {"name": "Iron Man", "email": "ironman@marvel.com", "team": "marvel"},
        {"name": "Captain America", "email": "cap@marvel.com", "team": "marvel"},
        {"name": "Black Widow", "email": "widow@marvel.com", "team": "marvel"},
    ]
    teams = [
        {"name": "marvel", "members": ["ironman@marvel.com", "cap@marvel.com", "widow@marvel.com"]},
        {"name": "dc", "members": ["superman@dc.com", "batman@dc.com", "wonderwoman@dc.com"]},
    ]
    activities = [
        {"user_email": "superman@dc.com", "activity": "Flight", "duration": 60},
        {"user_email": "ironman@marvel.com", "activity": "Suit Test", "duration": 45},
    ]
    leaderboard = [
        {"team": "marvel", "points": 300},
        {"team": "dc", "points": 250},
    ]
    workouts = [
        {"name": "Strength Training", "suggested_for": "dc"},
        {"name": "Agility Drills", "suggested_for": "marvel"},
    ]
    return users, teams, activities, leaderboard, workouts

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        client = MongoClient(settings.DATABASES['default']['CLIENT']['host'], settings.DATABASES['default']['CLIENT']['port'])
        db = client[settings.DATABASES['default']['NAME']]

        users, teams, activities, leaderboard, workouts = get_sample_data()

        # Clear collections
        db.users.delete_many({})
        db.teams.delete_many({})
        db.activities.delete_many({})
        db.leaderboard.delete_many({})
        db.workouts.delete_many({})

        # Insert sample data
        db.users.insert_many(users)
        db.teams.insert_many(teams)
        db.activities.insert_many(activities)
        db.leaderboard.insert_many(leaderboard)
        db.workouts.insert_many(workouts)

        # Ensure unique index on email
        db.users.create_index([("email", 1)], unique=True)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
