#!/usr/bin/env bash
echo "function gi() { curl -sL https://www.gitignore.io/api/\$@ ;}" >> \
~/.bashrc && source ~/.bashrc
