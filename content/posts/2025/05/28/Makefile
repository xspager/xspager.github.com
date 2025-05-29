FLAGS = -fno-stack-protector -fpic -fshort-wchar -mno-red-zone -I /usr/include/efi -I /usr/include/efi/x86_64 -DEFI_FUNCTION_WRAPPER

.PHONY: all clean

all:	hello.efi

hello.efi:  hello_efi.so
	objcopy -j .text              \
          -j .sdata               \
          -j .data                \
          -j .dynamic             \
          -j .dynsym              \
          -j .rel                 \
          -j .rela                \
          -j .reloc --target=efi-app-x86_64 hello_efi.so hello.efi

hello_efi.so:	hello_efi.o
	ld hello_efi.o /usr/lib/crt0-efi-x86_64.o -nostdlib -znocombreloc -T /usr/lib/elf_x86_64_efi.lds -shared -Bsymbolic -L /usr/lib -l:libgnuefi.a -l:libefi.a -o hello_efi.so

hello_efi.o:    hello_efi.t
	terra hello_efi.t

clean:
	rm -f hello_efi.efi hello_efi.so hello_efi.o