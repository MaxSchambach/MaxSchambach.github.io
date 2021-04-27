---
permalink: /cv/
title: "Curriculum vitae"
classes: wide
---
<link rel='stylesheet' type='text/css' href='/assets/css/cvstyle.css' />


## Education
<div>
    {% for post in site.categories.education %}
      <div class=cv>
        <p class="cvmain">{{ post.title }}<br> 
        <small>
        {% for val in post.cv-details %}
          &#8226; {{ val }} <br>
        {% endfor %}
        </small>
        </p>
      <p class="cvyears">{{ post.cv-years }}</p>
      </div>
    {% endfor %}
</div>
<div style="clear: both;"></div>


## Work Experience
<div>
    {% for post in site.categories.workexperience %}
      <div class=cv>
        <p class="cvmain">{{ post.title }}<br>
        <small> 
          {{ post.cv-details }}<br> 
          {{ post.cv-location }}
        </small>
        </p>
      <p class="cvyears">{{ post.cv-years }}</p>
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