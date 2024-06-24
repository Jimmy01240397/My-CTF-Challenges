all: main.c asm.h
		#gcc -o meowway $< -fno-stack-protector -no-pie -z now
		gcc -o meowway $< -lssl -lcrypto

asm.h: genasm.py
		python3 $< asm.h gadget.py

clean: 
		rm -rf meowway asm.h gadget.py
