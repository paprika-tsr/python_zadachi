import re


text_data = (
    "Полезные сайты: https://python.org, http://example.com, "
    "https://example.com и ftp://file.server.org"
)
url_pattern = r"https?://[a-zA-Z0-9./_-]+"
found_urls = re.findall(url_pattern, text_data)
for url in found_urls:
    print(url)
