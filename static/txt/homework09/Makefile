test:
	@$(MAKE) -sk test-all

test-all:	test-scripts
	@../.scripts/grade.py

test-quiz:
	../.scripts/check.py

test-code:	test-playlist

test-scripts:
	@curl -sLO https://pnutz.h4x0r.space/courses/cse.20589.fa26/static/txt/homework09/playlist_server.test
	@chmod +x ./*.test

test-playlist:	test-scripts playlist_server.py
	@echo Testing playlist ...
	@./playlist_server.test -v
	@echo

clean:
	@rm -f *.test
