# Kusa草

A Python based static blog program with Markdown support.

---

### Feature

- Write posts in Markdown.   
- Jekyll-like, you can migrate your jekyll blog to Kusa with only a few modifications.   
- Easy to setup, all you need is python && pip && (nginx || apache).   

### Why did I make Kusa?

Simplely because I don't know Ruby, and I couldn't find an alternative product in Python which is easy enough for me to edit.   
Kusa is less than 1k lines, that's simple enough for me to add new feature.

### Setup

1. Clone this repo to anywhere you like and run:

   ```
   python setup.py develop
   ```

2. cd to the path where you want to put your blog and run:   

   ```
   kusa init
   kusa build
   ```

   Kusa will automatically put an example blog in this folder.   

3. Set your nginx/apache's root path to path_to_your_blog/_dist, if you have your nginx/apache configured correctly, you should be able to browse the blog now.

### Thanks

Kusa uses [Jinja2](http://jinja.pocoo.org/) to render templates, [PyYAML](http://pyyaml.org/) to parse yaml and [Mistune](https://github.com/lepture/mistune) to compile Markdown.