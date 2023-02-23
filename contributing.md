---
abstract: This is a short contribution guide.
author: Dave Shawley, Edward Harris
---

# Contributing

Contributing to this project is as simple as making a for and a PR. Also, try to be nice to people, you don't know
what they're dealing with and you'd rather not make it worse.

## Setting up your environment

1. Clone this repository via https.

   ```{code-block} sh
   git clone https://github.com/edwardtheharris/sphinx-jsondomain edwardtheharris/sphinx-jsondomain
   ```

2. From the filesystem root of your local copy of this repository set up your virtual environment with [Pipenv](https://pipenv.pypa.io/en/latest/index.html)

   ```{code-block} sh
   cd edwardtheharris/sphinx-jsondomain
   pipenv install --dev
   pipenv shell
   ```

3. Improve the extension.
4. Check that the docs are consistent with your improvements.

   ```{code-block} sh
   sphinx-build docs/ build/docs
   cd build/docs
   python -m http.server
   ```

5. Ideally, increase test coverage.
6. Make a PR.

## Giving it Back

Once you have something substantial that you would like to contribute back
to the extension, push your branch up to github.com and issue a Pull Request
against the main repository.
