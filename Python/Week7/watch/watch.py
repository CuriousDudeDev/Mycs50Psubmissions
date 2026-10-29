import re
import sys


def main():
    print(parse(input("HTML: ")) , end= '')


def parse(s):
    before_and_after_iframe = s.split('</iframe>')
    before = before_and_after_iframe[0]
    if 'youtube.com' not in before:
        return None
    if 'youtube.com' in before_and_after_iframe[1]:
        return None

    till_src = before.split(' title') if 'title' in before else before.split('>')
    till_src = till_src[0]
    if 'youtube' not in till_src:
        return None
    src_link = till_src.split('src=')
    src_link = src_link[1].strip()
    src_link = src_link.split('embed/')
    code = src_link[1]
    return f"https://youtu.be/{code}"







if __name__ == "__main__":
    main()
