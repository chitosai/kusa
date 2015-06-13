---
title: Index
layout: base 
---
<div id="home">
  <h1>{{ site.description }}</h1>
  <ul class="posts">
    {% for post in site.posts %}
      <li><span>{{ post.date.strftime('%Y/%m/%d') }}</span> &raquo; <a href="{{ post.url }}">{{ post.title }}</a></li>
    {% endfor %}
  </ul>
</div>
