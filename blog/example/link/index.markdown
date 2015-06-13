---
layout: base
title: Friends links
---

This is your friends links page.

<ul class="posts">
{% for link in site.data.links %}
  <li><span>{{ link.desc }}</span> &raquo; <a href="{{ link.url }}">{{ link.name }}</a></li>
{% endfor %}
</ul>
