---
layout: page
title: Now
permalink: /now
---
This is my [now](https://nownownow.com/about) page, which I intend to update as often as I feel like giving the the world a glimpse as to what I am currently up to. Most of these updates will focus around updates regarding projects, transitions, and other life events that I am dealing with. 

{% assign nows = site.wer-now | sort: "title" | reverse %}
{% for now in nows limit: 1 %}
<h1>{{ now.title }}</h1>
<blockquote>
{{ now.status }}
</blockquote>
{% endfor %}

# Archive
{% assign nows = site.wer-now | sort: "title" | reverse %}
{% for now in nows offset: 1 %}- [{{now.title}}]({{now.url}})
{% endfor %}
