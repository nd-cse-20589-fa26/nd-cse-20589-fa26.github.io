test:
	@$(MAKE) -sk test-all

test-all:	test-scripts
	@../.scripts/grade.py

test-quiz:
	../.scripts/check.py

test-code:	test-findit

test-scripts:
	@curl -sLO https://pnutz.h4x0r.space/courses/cse.20589.fa26/static/txt/homework07/findit.test
	@chmod +x ./*.test

test-findit:	test-scripts findit.py
	@echo Testing findit ...
	@./findit.test -v
	@echo

clean:
	@rm -f *.test
