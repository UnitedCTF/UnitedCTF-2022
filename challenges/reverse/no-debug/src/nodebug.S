bits 64

%macro clear 1
	xor %1,%1
%endmacro

section .text alloc exec write align=16
	global _start
	_start:
		mov rbp,rsp
		;; ptrace(PTRACE_TRACEME, 0, 0, 0)
		clear rax
		clear rdi
		clear rsi
		clear rdx
		clear r10
		mov al,0x65
		syscall

		test rax,rax
		jl error
		jmp main

	error:
		;; write(STDOUT_FILENO, "I said no debugging\n", 0x14)
		mov rax,0xa676e69
		mov QWORD [rbp-0x8],rax
		mov rax,0x676775626564206f
		mov QWORD [rbp-0x10],rax
		mov rax,0x6e20646961732049
		mov QWORD [rbp-0x18],rax
		clear rax
		clear rdi
		clear rdx
		lea rsi,[rbp-0x18]
		mov dl,0x14
		inc al
		syscall

		call exit
		jmp exit

	main:
		;; write(STDOUT_FILENO, "Flag checker v13.37\nGive me your input: ", 0x28)
		clear rax
		mov QWORD [rbp-0x8],rax
		mov rax,0x203a7475706e6920
		mov QWORD [rbp-0x10],rax
		mov rax,0x72756f7920656d20
		mov QWORD [rbp-0x18],rax
		mov rax,0x657669470a37332e
		mov QWORD [rbp-0x20],rax
		mov rax,0x3331762072656b63
		mov QWORD [rbp-0x28],rax
		mov rax,0x6568632067616c46
		mov QWORD [rbp-0x30],rax
		clear rax
		clear rdi
		clear rdx
		lea rsi,[rbp-0x30]
		mov dl,0x28
		inc al
		syscall

		;; read(STDIN_FILENO, $rsp, 0xff);
		clear rax
		clear rdi
		clear rdx
		mov rsi,rsp
		mov dl,0xff
		syscall

	decrypt:
		clear rcx
		mov rdi,0xae347ce8b65c8cf1
		lea rsi,[rel code]
	_loop:
		mov rax,[rsi+rcx*8]
		xor rax,rdi
		mov [rsi+rcx*8],rax
		inc rcx
		test rax,rax
		jne _loop
		jmp code

	exit:
		clear rax
		clear rdi
		inc dl
		mov al,0x3c
		syscall

section .data progbits alloc exec write align=16
	code:
		dq 0x9f7ca7d9fe9cbdb9, 0xe6d2f5a0496dc438, 0x517c7ce8b679997c, 0x5ec7fc2b48970436, 0xa43046308652887b, 0xd22a856877a28684, 0x1ef44da0496dc419, 0x7687ce56015983cd, 0x67b8d86710c04a63, 0x14e3f77e08d41038, 0x79e7ee706bda5a75, 0xae347ce8b65c8c36
	endmarker:
		dq 0xae347ce8b65c8cf1