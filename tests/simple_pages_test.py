"""This test the homepage"""
import datetime
from os import getenv

def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'<li><a href="/page/about">About</a></li>' in response.data
    assert b'<li><a href="/page/welcome">Welcome</a></li>' in response.data

def test_request_about(client):
    """This makes the index page"""
    response = client.get("/page/about")
    assert response.status_code == 200
    assert b"About Page" in response.data

def test_request_welcome(client):
    """This makes the index page"""
    response = client.get("/page/welcome")
    assert response.status_code == 200
    assert b"Welcome Page" in response.data


def test_request_page_not_found(client):
    """This makes the index page"""
    response = client.get("/page/page5")
    assert response.status_code == 404

def test_context_variables_environment(client):
    """This test checks if the environment is printed"""
    response = client.get("/page/about")
    env = getenv('FLASK_ENV', None)
    test_string = f"Environment: {env}"
    content = bytes(test_string, 'utf-8')
    assert response.status_code == 200
    assert content in response.data

def test_context_variables_year(client):
    """This tests checks if the copyright and current year are printed"""
    response = client.get("/page/about")
    current_date_time = datetime.datetime.now()
    date = current_date_time.date()
    year = date.strftime("%Y")
    test_string = f"Copyright: {year}"
    content = bytes(test_string, 'utf-8')
    assert response.status_code == 200
    assert content in response.data
