---
title: Portfolio
layout: page
permalink: /portfolio
---
<head>
<link rel="stylesheet" href="/assets/css/lightbox.css">
<script src="/assets/js/jquery.min.js"></script>
<script src="/assets/js/lightbox.js"></script>
</head>
This is a page containing my publicized photography. If you'd like to view something more streamlined and generally more artistic, I suggest you check out my Instagram page [@3MN_SH](https://www.instagram.com/3MN_SH/). Slowly working on making this a more professional thing for myself, so stay tuned for a different website where I plan to sell prints if you want to support me! 

# Gallery
{% assign files = site.data.portfolio | sort: "date" | reverse %}

<div class="photo-gallery">
    {% for file in files %}
    <a href="{{ file.path }}" data-lightbox="photo">
        <img src="{{ file.path }}" alt="{{ file.caption }}">
    </a>
    {% endfor %}
</div>