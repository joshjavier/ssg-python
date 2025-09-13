import re


def extract_markdown_images(text):
    image_regex = r"!\[(.*?)\]\((.*?)\)"
    matches = re.findall(image_regex, text)
    return matches


def extract_markdown_links(text):
    link_regex = r"\[(.*?)\]\((.*?)\)"
    matches = re.findall(link_regex, text)
    return matches
