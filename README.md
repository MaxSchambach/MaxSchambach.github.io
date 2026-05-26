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


## Deployment

The site is deployed to GitHub Pages via GitHub Actions (`.github/workflows/deploy.yml`). Every push to `master` triggers a build and deploy automatically, visible under the Actions tab.

## Local Build

Install Jekyll according to the [official docs](https://jekyllrb.com/docs/), then install dependencies and serve:

```
bundle install
bundle exec jekyll serve --livereload
```

