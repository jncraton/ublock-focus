all: focus

focus: rules readermode
	python3 update.py

clean:
	rm -rf focus universal-readermode
