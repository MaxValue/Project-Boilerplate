#!/usr/bin/env bash

list=(
          'some string'\
          'another string'\
          )

for i in "${list[@]}"; do
     case "$1" in
          globhere )
               # rar command
               if commandhere; then
                    echo "True!"
                    break
               fi
               ;;
          anotherglob )
               if anothercommandhere; then
                    echo "Also True!"
                    break
               fi
               ;;
     esac
done
