---
layout: base
title: Friends links
---

<div class="header">
	<h1>{{ site.name }}</h1>
	<h5>{{ site.description }}</h5>
	{% include 'nav.html' %}
</div>
<div class="posts">
	{% for link in site.data.links %}
	<a href="{{ link.url }}" id="{{ link.name.replace(' ', '_') }}">
		<h3>{{ link.name }}</h3>
		<p class="meta">{{ link.desc }}</p>
	</a>
	{% endfor %}
</div>
