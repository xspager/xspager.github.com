Title: More things in March
Date: 2025-03-23 13:08
Lang: en
Status: published
Category: studying
Tags: pelican, markdown, golang, verilog

![Australian Pelican in flight. Image by Penny from Pixabay](/images/australian-pelican-9268481_1280.jpg)
<!-- Image by <a href="https://pixabay.com/users/pen_ash-5526837/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=9268481">Penny</a> from <a href="https://pixabay.com//?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=9268481">Pixabay</a> -->

I've been busy looking for a new job and all the pain that comes with that, and in the meanwhile trying to make this blog nicer. One of this days I'll make a similar post to the one I made in 2013 on how to make a your own static site like this one using [Pelican](https://getpelican.com/) and Github pages but I'll just share some stuff for now.

So I found out you can customize the Markdown Pelican understands by configuring [Python Markdown](https://python-markdown.github.io/), you can enable and configure some [extensions](https://python-markdown.github.io/extensions/) it has built in and third-party ones by creating a dictionary on your pelicanconf.py like

```python
MARKDOWN = {
    'extensions': ['codehilite', 'extra', 'footnotes', 'toc', 'abbr'],
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
    }
}
```

I need to comment my own config file, but I believe besides the defaults I'm enabling the [Table of Contents](https://python-markdown.github.io/extensions/toc/) and [Abbreviations](https://python-markdown.github.io/extensions/abbreviations/) extensions. A tip, Python Markdown is not restricted to Pelican so you can use it and enable this and other extension whenever you need to parse some Markdown.

I also got some extension to Pelican itself enabled and working. I was already using [sitemap](https://github.com/pelican-plugins/sitemap) before to generate a sitemap.xml. Now you can see an estimation of how long it will take to read and article thanks to the [statistics](https://github.com/pelican-plugins/statistics) extension, share the articles without exposing your privacy thanks to [share-post](https://github.com/pelican-plugins/share-post) (I submmited a PR to add the article title to the [Bluesky](https://bsky.app/) [intent URL](https://docs.bsky.app/docs/advanced-guides/intent-links)).

I'm also planning to use [series](https://github.com/pelican-plugins/series) to be able to join multiple articles into series of articles, [markdown-include](https://github.com/pelican-plugins/markdown-include) to inject the contents of a file like source code or a some other markdown file on an article, and I'm looking at a solution to generate captions for images and to make images more responsive, as in generate version of the images in the article so the visitor browser only downloads the highest resolution image it can show given the space for the image on the page, but something like the extension [image-process](https://github.com/pelican-plugins/image-process) relies on capabilities that you can't have when using Markdown so I'll be looking into that.

I have also tried to dip my toes again into Golang and Verilog (to simulate the Alto on a FPGA). I was convinced for a few days that with some effort I can get myself to understand BNF and parsing so I could write a BCPL parser, maybe later I'll give it another try. I'm also writing an article about Terra (the language) and how to generate binaries to run on "bare metal", so watch out for that.

I REALLY need to get back to studing ReactJS 😅

Stay safe and stay alive!

*[FPGA]: Field-Programmable Gate Array
*[BCPL]: Basic Combined Programming Language