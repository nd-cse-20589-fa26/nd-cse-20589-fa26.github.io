test:
	@$(MAKE) -sk test-all

test-all:	test-scripts
	@../.scripts/grade.py

test-quiz:
	../.scripts/check.py

test-code:	test-weather test-campus

test-scripts:
	@curl -sLO https://pnutz.h4x0r.space/courses/cse.20589.fa26/static/txt/homework03/weather.test
	@curl -sLO https://pnutz.h4x0r.space/courses/cse.20589.fa26/static/txt/homework03/campus.test
	@chmod +x ./*.test

test-weather:	test-scripts weather.py
	@echo Testing Weather ...
	@./weather.test -v
	@echo

test-campus: 	test-scripts campus.py
	@echo Testing Campus ...
	@./campus.test -v
	@echo

clean:
	@rm -f *.test
