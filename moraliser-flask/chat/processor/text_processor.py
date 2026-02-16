import requests
from bs4 import BeautifulSoup
import json
import re
from urllib.parse import urljoin
from flask import current_app

# Sample headers for GoogleBot
req_headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.131 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
    "Connection": "keep-alive",
    "Accept-Encoding": "gzip,deflate,br",
}


class Link:
    def __init__(self, link: str) -> None:
        self.__url = link
        self.__title = ""
        self.__desc = ""
        self.__img = ""
        self.__site_name = ""
        self.__embed = False

        self.__scoop_link__()

    def __add_protocol__(self, link: str):
        if link.startswith("/"):
            return urljoin(self.__url, link)
        if not link.startswith("http"):
            return urljoin("http://", link)
        return link

    def __resolve_redirect__(self, link: str):
        pass

    def __parse_title__(self, soup: BeautifulSoup) -> str:
        title = ""
        og_title_el = soup.find("meta", property="og:title")
        tw_title_el = soup.find("meta", property="twitter:title")
        h1_el = soup.find("h1")
        h2_el = soup.find("h2")

        if og_title_el is not None and og_title_el.get("content").strip() != "":
            title = og_title_el.get("content")
        elif tw_title_el is not None and tw_title_el.get("content").strip() != "":
            title = tw_title_el.get("content")
        elif soup.title is not None and soup.title.strip() != "":
            title = soup.title.string
        elif h1_el is not None and h1_el.text.strip() != "":
            title = h1_el.text
        elif h2_el is not None:
            # first h2 occurence
            title = h2_el.text

        return title

    def __parse_desc__(self, soup: BeautifulSoup) -> str:
        desc = ""
        og_desc_el = soup.find("meta", property="og:description")
        desc_el = soup.find("meta", {"name": "description"})
        p_visible_desc_el = soup.find(
            "p",
            style=lambda value: value != "display:none" or value != "visibility:hidden",
        )

        if og_desc_el is not None and og_desc_el.get("content").strip() != "":
            desc = og_desc_el.get("content")
        elif desc_el is not None and desc_el.get("content").strip() != "":
            desc = desc_el.get("content")
        elif p_visible_desc_el is not None:
            desc = p_visible_desc_el.text

        return desc

    def __parse_url__(self, soup: BeautifulSoup) -> str:
        url = ""
        og_url_el = soup.find("meta", property="og:url")
        can_li_url_rel = soup.find("link", rel="canonical")

        if og_url_el is not None:
            url = self.__add_protocol__(og_url_el.get("content"))
        elif can_li_url_rel is not None:
            url = self.__add_protocol__(can_li_url_rel.get("content"))
        else:
            # use the url param
            url = self.__url

        return url

    def __parse_site_name__(self, soup: BeautifulSoup) -> str:
        site_name = ""

        og_site_name_el = soup.find("meta", property="og:site_name")
        tw_site_name_el = soup.find("meta", property="twitter:site")

        if og_site_name_el is not None and og_site_name_el.get("content").strip() != "":
            site_name = og_site_name_el.get("content")
        elif (
            tw_site_name_el is not None and tw_site_name_el.get("content").strip() != ""
        ):
            site_name = self.__add_protocol__(tw_site_name_el.get("content"))

        return site_name

    def __parse_image__(self, soup: BeautifulSoup) -> str:
        img = ""

        og_img_el = soup.find("meta", property="og:image")
        li_shortcut_img_el = soup.find("link", rel="shortcut icon")
        li_img_el = soup.find("link", rel="icon")

        if og_img_el is not None and og_img_el.get("content").strip() != "":
            img = self.__add_protocol__(og_img_el.get("content"))
        elif (
            li_shortcut_img_el is not None
            and li_shortcut_img_el.get("href").strip() != ""
        ):
            img = self.__add_protocol__(li_shortcut_img_el.get("href"))
        elif li_img_el is not None and li_img_el.get("href").strip() != "":
            img = self.__add_protocol__(li_img_el.get("href"))

        if img == "":
            imgs = soup.find_all(
                "img",
                width=lambda value: value >= 50,
                height=lambda value: value >= 50,
            )
            imgs = list(
                filter(
                    lambda img: max(img.get("width"), img.get("height"))
                    / min(img.get("width") < 3, img.get("height")),
                    imgs,
                )
            )
            # Select image with max area
            imgs = sorted(
                imgs, key=lambda img: img.get("width") * img.get("height"), reverse=True
            )
            if len(imgs) > 0:
                img = imgs[0]

        return img

    def __scoop_link__(self):
        res = requests.get(self.__url, headers=req_headers)
        # print(res.headers["Content-Type"])
        current_app.logger.info(res)

        soup = BeautifulSoup(res.text, "lxml")

        self.__title = self.__parse_title__(soup=soup)
        self.__desc = self.__parse_desc__(soup=soup)
        self.__url = self.__parse_url__(soup=soup)
        self.__site_name = self.__parse_site_name__(soup=soup)
        self.__img = self.__parse_image__(soup=soup)

    def __parse_youtube(self):
        return True

    def __str__(self) -> str:
        return json.dumps(self.serialize(), indent=4)

    def serialize(self) -> dict:
        link_json = {
            "title": self.__title,
            "description": self.__desc,
            "image": self.__img,
            "url": self.__url,
            "site": self.__site_name,
            "embed": self.__embed,
        }
        return link_json


class TextProcessor:
    def __init__(self) -> None:
        pass

    def parse_links(self, text):
        links = []

        # Use a regular expression to find all links in the text.
        pattern = re.compile(r"(https?://[^\s]+)")
        matches = pattern.findall(text)

        # For each link, add it to the list of links.
        for match in matches:
            links.append(Link(match).serialize())

        return links
