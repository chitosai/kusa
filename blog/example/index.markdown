---
title: Index
layout: base 
---

<div class="header">
	<h1>{{ site.name }}</h1>
	<h5>{{ site.description }}</h5>
	{% include 'nav.html' %}
</div>
<div class="posts">
	{% for post in site.posts %}
	<a href="{{ post.url }}">
		<h3>{{ post.title }}</h3>
		<p class="meta">{{ post.author }} posted on {{ post.date.strftime('%Y/%m/%d') }}</p>
	</a>
	{% endfor %}
</div>
