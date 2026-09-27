test:
	@$(MAKE) -sk test-all

test-all:	test-scripts
	@../.scripts/grade.py

test-data:
	@curl -sLO https://pnutz.h4x0r.space/courses/cse.20589.fa26/static/txt/homework05/hulk.hashes
	@echo "*.hashes" > .gitignore
	@echo "*.test" >> .gitignore

test-quiz:
	../.scripts/check.py

test-code:	test-hulk

test-scripts:	test-data
	@curl -sLO https://pnutz.h4x0r.space/courses/cse.20589.fa26/static/txt/homework05/hulk.test
	@chmod +x ./*.test

test-hulk:	test-scripts hulk.py
	@echo Testing hulk ...
	@./hulk.test -v
	@echo

clean:
	@rm -f *.test
