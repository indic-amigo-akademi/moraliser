import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from enum import Enum


class LinkType(Enum):
    LINK = 0
    IMAGE = 1
    VIDEO = 2
    AUDIO = 3
    TEXT = 4
    YOUTUBE = 11
    FACEBOOK = 12
    INSTAGRAM = 13
    SPOTIFY = 14


class LinkPreview:
    def __init__(self, url):
        self.__url = url
        self.__title = None
        self.__description = None
        self.__domain = None
        self.__image = None
        self.__type = LinkType.LINK

        self.__process_url()

    def __get_title(self, soup: BeautifulSoup):
        og_title_ele = soup.find("meta", attrs={"property": "og:title"})
        if og_title_ele is not None:
            og_title = og_title_ele["content"].strip()
            if len(og_title) > 0:
                return og_title

        twitter_title_ele = soup.find("meta", attrs={"name": "twitter:title"})
        if twitter_title_ele is not None:
            twitter_title = twitter_title_ele["content"].strip()
            if len(twitter_title) > 0:
                return twitter_title

        title_ele = soup.find("title")
        if title_ele is not None:
            title = title_ele.text.strip()
            if len(title) > 0:
                return title

        h1_ele = soup.find("h1")
        if h1_ele is not None:
            h1 = h1_ele.text.strip()
            if len(h1) > 0:
                return h1

        h2_ele = soup.find("h2")
        if h2_ele is not None:
            h2 = h2_ele.text.strip()
            if len(h2) > 0:
                return h2
        return None

    def __get_description(self, soup: BeautifulSoup):
        og_desc_ele = soup.find("meta", attrs={"property": "og:description"})
        if og_desc_ele is not None:
            og_desc = og_desc_ele["content"].strip()
            if len(og_desc) > 0:
                return og_desc

        twitter_desc_ele = soup.find("meta", attrs={"name": "twitter:description"})
        if twitter_desc_ele is not None:
            twitter_desc = twitter_desc_ele["content"].strip()
            if len(twitter_desc) > 0:
                return twitter_desc

        meta_desc_ele = soup.find("meta", attrs={"name": "description"})
        if meta_desc_ele is not None:
            meta_desc = meta_desc_ele["content"].strip()
            if len(meta_desc) > 0:
                return meta_desc

        p_eles = soup.find_all("p")
        for p_ele in p_eles:
            # check if p_ele is visible
            if p_ele.parent.name != "script" and p_ele.parent.name != "style":
                p_text = p_ele.get_text().strip()
                if len(p_text) > 0:
                    return p_text

        return None

    def __get_domain(self, soup: BeautifulSoup):
        domain = None
        canonical_link_ele = soup.find("link", attrs={"rel": "canonical"})
        if canonical_link_ele is not None:
            canonical_link = canonical_link_ele["href"]
            if len(canonical_link) > 0:
                domain = canonical_link

        og_url_ele = soup.find("meta", attrs={"property": "og:url"})
        if og_url_ele is not None and domain is None:
            og_url = og_url_ele["content"]
            if len(og_url) > 0:
                domain = og_url

        if domain is not None:
            parsed_url = urlparse(domain)
        else:
            parsed_url = urlparse(self.__url)
        domain = str(parsed_url.hostname).replace("www.", "")

        return domain

    def __get_image(self, soup: BeautifulSoup):
        og_image_ele = soup.find("meta", attrs={"property": "og:image"})
        if og_image_ele is not None:
            og_image = og_image_ele["content"]
            if len(og_image) > 0:
                return og_image

        twitter_image_ele = soup.find("meta", attrs={"name": "twitter:image"})
        if twitter_image_ele is not None:
            twitter_image = twitter_image_ele["content"]
            if len(twitter_image) > 0:
                return twitter_image

        link_rel_image_ele = soup.find("link", attrs={"rel": "image_src"})
        if link_rel_image_ele is not None:
            link_rel_image = link_rel_image_ele["href"]
            if len(link_rel_image) > 0:
                return link_rel_image

        meta_image_ele = soup.find("meta", attrs={"name": "image"})
        if meta_image_ele is not None:
            meta_image = meta_image_ele["content"]
            if len(meta_image) > 0:
                return meta_image

        image_eles = soup.find_all("img")
        for image_ele in image_eles:
            # Check if aspect ratio is not more than 3
            if image_ele.has_attr("width") and image_ele.has_attr("height"):
                width = int(image_ele["width"])
                height = int(image_ele["height"])
                if (
                    width / height < 3
                    and height / width < 3
                    and width > 50
                    and height > 50
                ):
                    image_url = image_ele["src"]
                    if len(image_url) > 0:
                        return image_url

        return None

    def __check_for_type(self, content_type):
        if content_type is not None:
            if "image/" in content_type:
                return LinkType.IMAGE
            elif "video/" in content_type:
                return LinkType.VIDEO
            elif "audio/" in content_type:
                return LinkType.AUDIO
            elif "text/" in content_type and "/html" not in content_type:
                return LinkType.TEXT

        if "youtube.com" in self.__domain:
            return LinkType.YOUTUBE
        elif "facebook.com" in self.__domain:
            return LinkType.FACEBOOK
        elif "instagram.com" in self.__domain:
            return LinkType.INSTAGRAM
        elif "spotify.com" in self.__domain:
            return LinkType.SPOTIFY

        return LinkType.LINK

    def __process_url(self):
        try:
            res = requests.get(self.__url)
            if res.status_code == 200:
                soup = BeautifulSoup(res.content, "lxml")

                content_type = res.headers.get("Content-Type")

                self.__domain = self.__get_domain(soup=soup)
                self.__type = self.__check_for_type(content_type)

                if self.__type == LinkType.LINK:
                    self.__title = self.__get_title(soup=soup)
                    self.__description = self.__get_description(soup=soup)
                    self.__image = self.__get_image(soup=soup)
                if self.__type == LinkType.IMAGE:
                    self.__image = self.__url
                    self.__title = self.__url
                

            else:
                return None
        except requests.exceptions.RequestException as e:
            return None

    def to_dict(self) -> dict:
        return {
            "title": self.__title,
            "description": self.__description,
            "domain": self.__domain,
            "image": self.__image,
            "url": self.__url,
            "type": self.__type.name,
        }
