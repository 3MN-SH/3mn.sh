---
title: Home
layout: home
permalink: /
---
**Hello World.**

My name is **Shane**, also known as **3MN**. Welcome to my little corner of the internet. This website acts as an attempt to consolidate all of my creative outlets into one place. My mission with this website is to explore my own interpretation of meaning and identity through analog and digital creativity, and give the things I create a place to exist (which I am notoriously bad at doing).

Below are some tables which give a general layout of the website and a description of what each category and has to offer. 

{% for category in site.navigation %}
<h3>// {{ category.name }}<span class='blip'>({{ category.blip }})</span>
</h3>

<table>
<tr>
    <th>Page</th>
    <th>Description</th>
</tr>
{% for parent in category.parents %}
<tr>
    <td>
        <a href='{{ parent.url }}'>{{ parent.text }}</a>
        {% if parent.children %}
            <ul class="sitemap">
            {% for child in parent.children %}
                <li class="sitemap"><a href='{{ child.url }}'>{{ child.text }}</a></li>
            {% endfor %}
            </ul>
        {% endif %}
    </td>
    <td>{{ parent.description }}</td>
</tr>
{% endfor %}
</table> 
{% endfor %}

There's also a few secret pages sprinkled around that I won't divulge. Hope you enjoy my cozy litte corner of the internet!