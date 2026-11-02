test:
	@$(MAKE) -sk test-all

test-all:	test-scripts
	@../.scripts/grade.py

test-quiz:
	../.scripts/check.py

test-code:	test-curlit

test-scripts:
	@curl -sLO https://pnutz.h4x0r.space/courses/cse.20589.fa26/static/txt/homework08/curlit.test
	@chmod +x ./*.test

test-curlit:	test-scripts curlit.py
	@echo Testing curlit ...
	@./curlit.test -v
	@echo

clean:
	@rm -f *.test
