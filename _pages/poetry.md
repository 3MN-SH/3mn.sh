---
layout: page
title: Poetry
---
This is a colleciton of poetry that I've decided to publicize. I have been writing poetry since the early years of high school. Despite this, I kind of want to keep those writings in the past, as I'm not particularly fond of most of them. In any case, here's my collection of poetry:

# Archive
{% assign poems = site.schreiben-poetry | sort: "date" | reverse %}
{% for poem in poems %}
<li>{% assign date_format = "%Y-%m-%d" %}{{ poem.date | date: date_format }} ~ <a href="{{ poem.url | relative_url }}">{{ poem.title | escape }}</a>
{% endfor %}

