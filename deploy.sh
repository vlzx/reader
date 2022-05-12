#!/usr/bin/env bash

set -e

yarn build

cd dist

git init
git checkout -b deploy
git add .
git commit -m 'deploy'

git push -f git@github.com:vlzx/reader.git deploy:gh-pages

cd -
