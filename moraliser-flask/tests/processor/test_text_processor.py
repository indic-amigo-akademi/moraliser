import pytest
from chat.processor.text_processor import Link


def test_link_with_post_from_creepypasta():
    url = "https://www.creepypasta.com/the-lockwood-house/"
    li = Link(url)
    li_json = li.serialize()
    assert li_json["title"] == "The Lockwood House - Creepypasta"
    assert (
        li_json["description"]
        == "I'm not particularly a religious person. I never really connected with the idea of believing in a God or a Devil; something like religion never really"
    )
    assert (
        li_json["image"]
        == "https://www.creepypasta.com/wp-content/uploads/The-lockwood-house.jpg"
    )
    assert li_json["site"] == "Creepypasta"
    assert li_json["url"] == url
    assert li_json["embed"] == False


def test_link_with_post_from_medium():
    url = "https://blog.medium.com/medium-embraces-mastodon-19dcb873eb11"
    li = Link(url)
    li_json = li.serialize()
    assert li_json["title"] == "Medium embraces Mastodon"
    assert (
        li_json["description"]
        == "The fediverse is a breath of fresh air for writers and social media"
    )
    assert (
        li_json["image"]
        == "https://miro.medium.com/max/1024/1*-kbWgTfVb3CZZ6xS6i8O9g.png"
    )
    assert li_json["site"] == "Medium"
    assert li_json["url"] == url
    assert li_json["embed"] == False


def test_link_without_og_tags():
    url = "https://shivishbrahma.github.io/"
    li = Link(url)
    li_json = li.serialize()
    assert li_json["title"] == "Shivishbrahma"
    assert li_json["description"] == "Portfolio of Purbayan Chowdhury (Shivishbrahma)"
    assert li_json["image"] == "https://shivishbrahma.github.io/favicon.ico"
    assert li_json["site"] == ""
    assert li_json["url"] == url
    assert li_json["embed"] == False


# def test_link_with_img_url():
#     url = ""
#     li = Link(url)
