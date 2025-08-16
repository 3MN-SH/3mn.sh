---
layout: page
title: Blog
---
This is page for various essay-styled articles regarding some pretty niche topics. I don't intend to stick to specific topics, and eventually I plan to implement a tag/search system for sorting out all the articles. For now though, It's just gonna be a continous list of things that I write with no particular pattern.

# Archive
{% assign blogs = site.schreiben-blog | sort: "date" | reverse %}
{% for blog in blogs %}
<li>{% assign date_format = "%Y-%m-%d" %}{{ blog.date | date: date_format }} ~ <a href="{{ blog.url | relative_url }}">{{ blog.title | escape }}</a>
{% endfor %}