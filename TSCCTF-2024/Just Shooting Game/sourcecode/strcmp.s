_start:
section .text
global _start
push rbp
mov rbp, rsp
mov rcx, [rax-8]
cmp rcx, [rbx-8]
jne _neq
xor rdx, rdx
_loop:
mov cl, [rax+rdx*1]
cmp cl, [rbx+rdx*1]
jne _neq
add rdx, 1
cmp rdx, [rax-8]
jl _loop
jmp _good
_neq:
ret
_good:
call 0
mov rsp, rbp
pop rbp
ret
