#!/usr/bin/env bash

err() {
  script_name="$1"
  args_length="$2"

  if [ ! $args_length -eq 2 ]
  then
    echo "Need only a path and extension"
    echo "Example: $script_name Python3 py"
    exit 1
  fi
}
