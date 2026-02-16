import pytest
from chat.utils.link_preview import LinkPreview

def test_LinkPreviewYoutube():
	url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
	preview = LinkPreview(url)
	assert preview.url == url
	assert preview.type == "YOUTUBE"
	assert preview.title == "Rick Astley - Never Gonna Give You Up (Official Music Video)"
	assert preview.description == "The official video for “Never Gonna Give You Up” by Rick Astley. Never: The Autobiography 📚 OUT NOW! Follow this link to get your copy and listen to Rick’s ..."
	assert preview.domain == "youtube.com"
	assert preview.image == "https://i.ytimg.com/vi/dQw4w9WgXcQ/maxresdefault.jpg"


def test_LinkPreviewLink():
	url = "https://www.google.com"
	preview = LinkPreview(url)
	assert preview.url == url
	assert preview.type == "LINK"
	assert preview.title == "Google"
	assert preview.description == "© 2025 - Privacy - Terms"
	assert preview.domain == "google.com"
	assert preview.image == "https://www.google.com/images/branding/googlelogo/1x/googlelogo_white_background_color_272x92dp.png"

def test_LinkPreviewInsta():
	url = "https://www.instagram.com/p/CQm-b08h3eZ/"
	preview = LinkPreview(url)
	assert preview.url == url
	assert preview.type == "INSTAGRAM"
	print(preview.title)
	assert preview.title == "A day in the life of a cat"
	assert preview.description == "This is a cat"
	assert preview.domain == "instagram.com"
	assert preview.image == "https://scontent-lga3-1.cdninstagram.com/v/t51.2885-15/e35/14486635_10153133556881825_1247574537_n.jpg?_nc_ht=scontent-lga3-1.cdninstagram.com&_nc_cat=103&_nc_ohc=s9H5L71W_e0AX8pW88H&tp=1&oh=602e76514359453194a1935332289256&oe=5F8E4332"
	