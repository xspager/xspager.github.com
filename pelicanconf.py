AUTHOR = 'xspager'
SITENAME = 'xspager\'s Blog'
SITETITLE = 'xspager\'s Blog'
SITESUBTITLE = 'Whatever I manage to post'
SITEURL = ""
SITELOGO = "/static/capybara_128x128.png"

PATH = "content"

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

MAIN_MENU = True

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

MENUITEMS = (
    ("Archives", "/archives.html"),
    ("Categories", "/categories.html"),
    ("Tags", "/tags.html"),
)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

THEME='Flex'

COPYRIGHT_YEAR = "2013-2026"
ROBOTS = "all"
SITEDESCRIPTION = "xspager's personal blog about geopolitics, technology and more"
LINKS_IN_NEW_TAB = True

SUMMARY_MAX_LENGTH = 64 + 32
SUMMARY_MAX_PARAGRAPHS = 4

STATIC_PATHS = ['images', 'extra/CNAME', 'extra/robots.txt', 'static']
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'extra/robots.txt': {'path': 'robots.txt'}
}

PATH_METADATA = r'posts/(?P<date>\d{4}/\d{2}).*'

THEME_TEMPLATES_OVERRIDES = ["templates"]

PLUGINS = ['sitemap', 'statistics', 'share_post', 'image_process', 'md_include', 'series']

REL_CANONICAL = True

THEME_COLOR = 'dark'
THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
THEME_COLOR_ENABLE_USER_OVERRIDE = True

PYGMENTS_STYLE = 'xcode'
PYGMENTS_STYLE_DARK = 'monokai'

MARKDOWN = {
    'extensions': ['codehilite', 'extra', 'footnotes', 'toc', 'abbr', 'yafg'],
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'yafg': {
            'stripTitle': False,
            'generateSource': True,
            'imageClass': 'image-process-crisp'
        },
    }
}

#IMAGE_PROCESS_PARSER = "lxml"
IMAGE_PROCESS = {
    "crisp": {
        "type": "picture",
        "sources": [
            {
                "name": "default",
                "media": "(min-width: 640px)",
                "srcset": [
                    ("640w", ["scale_out 640 480 True"]),
                    ("1024w", ["scale_out 1024 683 True"]),
                    ("1440w", ["scale_out 1440 900 True"]),
                    ("1600w", ["scale_out 1600 1200 True"]),
                ],
                "sizes": "100vw",
            },
            {
                "name": "source-1",
                "srcset": [
                    ("640w", ["scale_out 640 480 True"]),
                    ("1024w", ["scale_out 1024 683 True"]),
                    ("1440w", ["scale_out 1440 900 True"]),
                    ("1600w", ["scale_out 1600 1200 True"]),
                ]
            },
        ],
        "default": ("default", "640w"),
    },
}

# Prevent the theme from adding a fragment in the end of the links on the index page
DISABLE_URL_HASH = True

# Custom CSS
CUSTOM_CSS = 'static/custom.css'

# Foto de <a href="https://unsplash.com/pt-br/@byeduck?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Mateusz Bajdak</a> na <a href="https://unsplash.com/pt-br/fotografias/um-grupo-de-animais-que-estao-de-pe-na-grama-HETOq3h8XGA?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a>
FAVICON = 'static/capybara_128x128.png'
