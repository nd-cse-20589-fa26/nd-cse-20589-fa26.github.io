test:
	@$(MAKE) -sk test-all

test-all:	test-scripts
	@../.scripts/grade.py

test-quiz:
	../.scripts/check.py

test-code:	test-odds

test-scripts:
	@curl -sLO https://pnutz.h4x0r.space/courses/cse.20589.fa26/static/txt/reading05/odds.test
	@chmod +x ./*.test

test-odds: 	test-scripts odds.py
	@echo Testing odds ...
	@./odds.test -v
	@echo

clean:
	@rm -f *.test
