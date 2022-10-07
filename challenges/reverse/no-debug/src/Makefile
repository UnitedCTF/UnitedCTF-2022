all:
	nasm -felf64 nodebug.S -o nodebug.o
	ld nodebug.o -onodebug
	strip -s nodebug
	mv nodebug ../dist/
	rm nodebug.o
