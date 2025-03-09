AUTHOR = 'xspager'
SITENAME = 'xspager\'s Blog'
SITETITLE = 'xspager\'s Blog'
SITESUBTITLE = 'Whatever I manage to post'
SITEURL = ""

PATH = "content"

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
)

# Social widget
SOCIAL = (
    ("twitter", "https://twitter.com/DanielOCL"),
    ("bluesky", "https://bsky.app/profile/danielocl.com.br"),
)

DEFAULT_PAGINATION = 3

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

THEME='Flex'

COPYRIGHT_YEAR = "2013-2025"

SUMMARY_MAX_LENGTH = 2024
SUMMARY_MAX_PARAGRAPHS = 5

STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

PATH_METADATA = r'posts/(?P<date>\d{4}/\d{2}).*'

THEME_TEMPLATES_OVERRIDES = ["templates"]