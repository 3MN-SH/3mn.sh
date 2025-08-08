---
layout: page
permalink: /guestbook
title: Guestbook
comments: true
---
This page uses [Disqus](https://disqus.com/) to capture and display comments. I intend to migrate this over to a self-hosted platform at some point so I can break away from the ads and things that are attached to this.

If you wanna say hi, feel free to comment below -- all responses are deeply appreciated! 

{% if page.comments %}

<div id="disqus_thread">
<script>
    (function() { // DON'T EDIT BELOW THIS LINE
    var d = document, s = d.createElement('script');
    s.src = 'https://3mn.disqus.com/embed.js';
    s.setAttribute('data-timestamp', +new Date());
    (d.head || d.body).appendChild(s);
    })();
</script>
<noscript>Please enable JavaScript to view the <a href="https://disqus.com/?ref_noscript">comments powered by Disqus.</a></noscript>
</div>
{% endif %}