from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import User, Team, Activity, Leaderboard, Workout

class APITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        User.objects.create(name="Test User", email="test@user.com", team="marvel")
        Team.objects.create(name="marvel", members=["test@user.com"])
        Activity.objects.create(user_email="test@user.com", activity="Test Activity", duration=30)
        Leaderboard.objects.create(team="marvel", points=100)
        Workout.objects.create(name="Test Workout", suggested_for="marvel")

    def test_api_root(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('users', response.data)

    def test_users_endpoint(self):
        response = self.client.get('/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_teams_endpoint(self):
        response = self.client.get('/teams/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_activities_endpoint(self):
        response = self.client.get('/activities/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_leaderboard_endpoint(self):
        response = self.client.get('/leaderboard/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_workouts_endpoint(self):
        response = self.client.get('/workouts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)
