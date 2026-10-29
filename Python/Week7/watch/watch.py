import re
import sys

def main():
    html = input("HTML: ")
    result = parse(html)
    print(result, end='')

def parse(s):
    """Extract YouTube video ID from an iframe embed and return youtu.be link.
    Returns None if no valid YouTube embed is found.
    """
    if not s or 'youtube' not in s.lower():
        return None

# Match common YouTube embed patterns:
    # - youtube.com/embed/VIDEO_ID
    # - Handles http/https, www, single/double quotes, and optional params after ID
    pattern = r'src=["\']https?://(?:www\.)?youtube\.com/embed/([A-Za-z0-9_-]+)'
    match = re.search(pattern, s, re.IGNORECASE)

if match:
        video_id = match.group(1)
        return f"https://youtu.be/{video_id}"

return None

if __name__ == "__main__":
    main()
