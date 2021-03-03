---
title: 'Woods Hole Palettes'
layout: page
content: []
---

These are taken from 
[Sarah Hu's Woods Hole palettes](https://github.com/shu251/PaletteWoodsHole) for R.
All Woods Hole palettes are qualitative.

# Contents

{% for p in palettes %}
- [{{p}}](#{{p | lower}})
{%- endfor %}

# Previews

{% for p in palettes %}
<section id="{{p | lower}}">
    <p class="h4"><a href="{{palette_dict[p].url}}">{{p}}</a></p>

    <img src="./img/{{p + '_discrete.png'}}" alt="{{p + ' discrete'}}">

</section>
{% endfor %}
