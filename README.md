# Personal webpage of Maximilian Schambach

## How To Use
There are 5 top level pages: Home, News, CV, Publications, and Teaching.


### Home
Content is provided simply via the markdown file `_pages/home.md`.

### News
Content is generated using posts in `news/_posts`.
To add a post, simply add a new markdown file here.
Due to the folder scheme, posts are automatically assigned the `news` category.
As is common for Jekyll posts, naming scheme has to be `YYYY-MM-DD-title.md`.
This holds for all following post-like content.

### CV
The CV is created using the entries in `cv/`.
See the folder for examples on education and work experience.

### Publications
List is automatically generated from posts in `publications`.
By placing the publication in the corresponding subfolder (`preprint`, `journal`, `conference`) the category is automatically assigned. See the folder for some examples and specifically defined variables to specify authors, journal name, etc.


## Local Build

To build, install Jekyll according to the [official docs](https://jekyllrb.com/docs/).

**Caution:** this build does not work with Ruby 3.x. So make sure to install Jekyll e.g. with Ruby 2.7.3.
It is advised to not downgrade the system's Ruby installation, but use an environment, for example via `rbenv`. 

So the procedure is:

  - install `rbenv`
  - initialize via `rbenv init` (see the doc for details)
  - install Ruby 2.7.3 via `rbenv install 2.7.3`
  - switch to Ruby 2.7.3 via `rbenv local 2.7.3`
  - verify by calling `gem env home`
  - install bundler via `gem install bundler`

Then, the website can be build and served locally calling 

```
bundle exec jekyll serve --livereload
```

from the top-level of this repository.

