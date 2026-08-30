#!/bin/sh

PREV_TIMESTAMP=0

inotifywait -e close_write -r -m $(pwd) | \
    while read path action file; do
    	case $file in
    	    *.md|*.css|*.yaml)
    	    CURR_TIMESTAMP=$(date +%s)
	    if [ $(($CURR_TIMESTAMP - $PREV_TIMESTAMP)) -lt 2 ]; then
	    	continue
	    fi
	    PREV_TIMESTAMP=$CURR_TIMESTAMP
    	    make install
    	    ;;
    	esac
    done
