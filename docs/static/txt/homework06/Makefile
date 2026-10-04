test:
	@$(MAKE) -sk test-all

test-all:	test-scripts
	@../.scripts/grade.py

test-quiz:
	../.scripts/check.py

test-code:	test-timeit

test-scripts:
	@curl -sLO https://pnutz.h4x0r.space/courses/cse.20589.fa26/static/txt/homework06/timeit.test
	@chmod +x ./*.test

test-timeit:	test-scripts timeit.py
	@echo Testing timeit ...
	@./timeit.test -v
	@echo

clean:
	@rm -f *.test
