---
permalink: /cv/
title: "Curriculum Vitae"
classes: wide
---
<link rel='stylesheet' type='text/css' href='/assets/css/cvstyle.css' />


## Education
<div>
    {% for post in site.categories.education %}
      <div class="cv">
        <div class="cvmain">{{ post.title }}<br> 
          <small>
          {% for val in post.cv-details %}
            &#8226; {{ val }} <br>
          {% endfor %}
          {% if post.thesis %}&#8226; Thesis: {% if post.thesis-link %}<a href="{{ post.thesis-link }}" target="_blank">{{ post.thesis }}</a>{% else %}{{ post.thesis }}{% endif %}{% endif %}
          </small>
        </div>
        <div class="cvyears">{{ post.cv-years }}</div>
      </div>
    {% endfor %}
</div>
<div style="clear: both;"></div>


## Work Experience
<div>
    {% for post in site.categories.workexperience %}
      <div class="cv">
        <div class="cvmain">{{ post.title }}<br>
        <small> 
          {{ post.cv-details }}<br> 
          {{ post.cv-location }}
        </small>
        </div>
      <div class="cvyears">{{ post.cv-years }}</div>
      </div>
    {% endfor %}
</div>
<div style="clear: both;"></div>



## Scientific Duties
**Reviews**  
<small>
IEEE Transactions on Image Processing<br>
tm – Technisches Messen
</small>

**Conferences**  
<small>
Program Committee, Optical Characterization of Materials (OCM), 2021
</small>