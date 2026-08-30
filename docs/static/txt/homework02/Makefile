test:
	@$(MAKE) -sk test-all

test-all:	test-scripts
	@../.scripts/grade.py

test-quiz:
	../.scripts/check.py

test-code:	test-cut test-wc

test-data:
	@curl -sLO https://pnutz.h4x0r.space/courses/cse.20589.fa26/static/txt/homework02/cut.input
	@curl -sLO https://pnutz.h4x0r.space/courses/cse.20589.fa26/static/txt/homework02/wc.input

test-scripts:	test-data
	@curl -sLO https://pnutz.h4x0r.space/courses/cse.20589.fa26/static/txt/homework02/cut.test
	@curl -sLO https://pnutz.h4x0r.space/courses/cse.20589.fa26/static/txt/homework02/wc.test
	@chmod +x ./*.test

test-cut:	test-scripts cut.py
	@echo Testing Cut ...
	@./cut.test -v
	@echo

test-wc: 	test-scripts wc.py
	@echo Testing WC ...
	@./wc.test -v
	@echo

clean:
	@rm -f *.input *.test
