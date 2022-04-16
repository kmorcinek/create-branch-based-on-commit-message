#!/usr/bin/env bash

COMMIT_MSG=`git show -s --format=%s`
OUT=`python3 parsing.py "$COMMIT_MSG"`

git checkout -b $OUT