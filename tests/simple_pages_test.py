"""This test the homepage"""


def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'<a class="nav-link" href="/about">About</a>' in response.data
    assert b'<a class="nav-link" href="/page1">Git</a>' in response.data
    assert b'<a class="nav-link" href="/page2">Docker</a>' in response.data
    assert b'<a class="nav-link" href="/page3">Python/Flask</a>' in response.data
    assert b'<a class="nav-link" href="/page4">CI/CD</a>' in response.data

def test_request_index(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"IS601" in response.data


def test_request_about(client):
    """This makes the about page"""
    response = client.get("/about")
    assert response.status_code == 200
    assert b"About Page" in response.data


def test_request_page1(client):
    """This makes the GIT page"""
    response = client.get("/page1")
    assert response.status_code == 200
    assert b"Git" in response.data


def test_request_page2(client):
    """This makes the Docker page"""
    response = client.get("/page2")
    assert response.status_code == 200
    assert b"Docker" in response.data


def test_request_page3(client):
    """This makes the Python page"""
    response = client.get("/page3")
    assert response.status_code == 200
    assert b"Python" in response.data


def test_request_page4(client):
    """This makes the CICD page"""
    response = client.get("/page4")
    assert response.status_code == 200
    assert b"CI/CD" in response.data


def test_request_page5(client):
    """This makes the OOP page"""
    response = client.get("/page5")
    assert response.status_code == 200
    assert b"OOP" in response.data


def test_request_page6(client):
    """This makes the AAA Testing page"""
    response = client.get("/page6")
    assert response.status_code == 200
    assert b"AAA Testing" in response.data


def test_request_page7(client):
    """This makes the OOP Principles page"""
    response = client.get("/page7")
    assert response.status_code == 200
    assert b"OOP" in response.data


def test_request_page8(client):
    """This makes the SOLID page"""
    response = client.get("/page8")
    assert response.status_code == 200
    assert b"SOLID" in response.data



def test_request_page_not_found(client):
    """This makes the index page"""
    response = client.get("/page9")
    assert response.status_code == 404
