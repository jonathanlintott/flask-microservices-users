# project/tests/test_config.py

import os
import unittest

from flask import current_app
from flask_testing import TestCase

from project import create_app

app = create_app()

is_containerized = os.environ.get('CONTAINERIZED', 'no')


@unittest.skipIf(is_containerized == 'no', "Not in a container")
class TestDevelopmentConfig(TestCase):
    def create_app(self):
        app.config.from_object('project.config.DevelopmentConfig')
        return app

    def test_app_is_development(self):
        self.assertEqual(app.config['SECRET_KEY'], 'my_precious')
        self.assertTrue(app.config['DEBUG'])
        self.assertIsNotNone(current_app)
        self.assertEqual(
            app.config['SQLALCHEMY_DATABASE_URI'],
            'postgres://postgres:postgres@users-db:5432/users_dev'
        )


@unittest.skipIf(is_containerized == 'no', "Not in a container")
class TestTestingConfig(TestCase):
    def create_app(self):
        app.config.from_object('project.config.TestingConfig')
        return app

    def test_app_is_testing(self):
        self.assertTrue(app.config['SECRET_KEY'] == 'my_precious')
        self.assertTrue(app.config['DEBUG'])
        self.assertTrue(app.config['TESTING'])
        self.assertFalse(app.config['PRESERVE_CONTEXT_ON_EXCEPTION'])
        self.assertTrue(
            app.config['SQLALCHEMY_DATABASE_URI'] ==
            'postgres://postgres:postgres@users-db:5432/users_test'
        )


@unittest.skipIf(is_containerized == 'no', "Not in a container")
class TestProductionConfig(TestCase):
    def create_app(self):
        app.config.from_object('project.config.ProductionConfig')
        return app

    def test_app_is_production(self):
        self.assertTrue(app.config['SECRET_KEY'] == 'my_precious')
        self.assertFalse(app.config['DEBUG'])
        self.assertFalse(app.config['TESTING'])


if __name__ == '__main__':
    unittest.main()
