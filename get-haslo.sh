#!/bin/bash
if [ $# -lt 1 ]; then
    echo "Brakuje argumentu $1."
    exit 1
fi
hasla | grep $1
