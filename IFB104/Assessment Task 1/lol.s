.section    __TEXT,__text,regular,pure_instructions
.macosx_version_min 11, 0
.globl  _start

_start:
    // Write "Hello, World!" to stdout
    mov x0, #1                  // file descriptor (stdout)
    adrp x1, helloworld         // address of string
    add x1, x1, :lo12:helloworld
    mov x2, #13                 // length of string
    mov x16, #4                 // syscall number (sys_write)
    svc #0x80                   // make syscall

    // Exit program
    mov x0, #0                  // exit code
    mov x16, #1                 // syscall number (sys_exit)
    svc #0x80                   // make syscall

.section    __TEXT,__cstring,cstring_literals
helloworld:
    .ascii  "Hello, World!\n"
