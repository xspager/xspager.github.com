Title: Terra and Lua - UEFI
Category: programming
Status: published
Lang: en
Tags:lua, terra, c, lowlevel, uefi
Date: 2025-05-28 23:15
Series: Terra and Lua
Cover: /images/2015_epic_earthmoonstill.jpg

![2015: Moon crosses Earth (EPIC/DSCOVR)](/images/2015_epic_earthmoonstill.jpg "2015: Moon crosses Earth (EPIC/DSCOVR) *Image Credit: NASA/NOAA*")

Now in part 2 we will see how we can generate code and link it to [GNU-EFI](https://wiki.osdev.org/GNU-EFI) so it can run on the EFI environment, but first.

[TOC]

## What is (U)EFI?

I asked ChatGPT... I'm kidding, I'm kidding. I'll copy more or less the wording on Wikipedia rather. [UEFI](https://en.wikipedia.org/wiki/UEFI) (Unified Extensible Firmware Interface) is a specification for the firmware of computer systems that supports booting from a hardware-based EFI (Extensible Firmware Interface) environment, and it's used by both UEFI 1.0 & later versions as well with some older BIOSes like APM or MSC. So basically is the standard for modern BIOS. It started being used in 2000 on Itanium systems and was shipped with the brand new at the time Intel based Macintosh computers. All desktop class and server computers have been using EFI for decades now, even the ones that have an ARM or RISC-V CPUs. You should check the Wikipedia article, it's pretty good.

Unlike the BIOSes of the past developed in Assembly for the specific CPU architecture, the development in EFI is made using C using a specific SDK that Intel provides for free.

For [Wintel](https://en.wikipedia.org/wiki/Wintel) reasons the EFI environment looks very Windows-like, it uses [PE binaries](https://en.wikipedia.org/wiki/Portable_Executable) and Windows calling conventions. Even the shell available on the [Intel TianoCore EDK](https://en.wikipedia.org/wiki/TianoCore_EDK_II) look more like MS-DOS than a Unix shell.

## Good, but how do I get started with this mess?

We will create a Docker image with Terra, development tools to help us with FAT filesystems.

```Dockerfile
{!content/posts/2025/05/28/Dockerfile!}
```

Now we build it and launch it adding the current path in `/hello` inside the container.

```bash
# build the Docker container and tag it as terra_end_lua
$ docker build -t terra_end_lua .
# run the container and place the current directory as the folder /hello inside the container
$ docker run -v `pwd`:/hello --rm -it terra_and_lua
```

## Ok, but how do I compile Terra code to run without the systems's libC?
We will need three new things that weren't covered in the previous article, how do you add more paths to the include path, how to specify the target platform and some extra flags, you can see them highlighted in the code bellow:

```Lua hl_lines="1 3 4 5 54 55 56 57"
{!content/posts/2025/05/28/hello_efi.t!}
```

The [triplet](https://wiki.osdev.org/Target_Triplet) we are specifying say we are targeting an [x86_64](https://en.wikipedia.org/wiki/X86-64) CPU without an OS. You will have to take my word about the flags in the bottom of the file, but one very important is `-fshort-wchar` that tell the compiler... that our C strings are 16 bits wide (correct me if I'm wrong here). Check [this article](https://wiki.osdev.org/GNU-EFI) in OSDev if you want more information.

We added includes for the GNU-EFI library headers, and out entrypoint function `hello_efi` is not expecting argc and argv as parameters now, but one [struct and a pointer to another struct](https://uefi.org/specs/UEFI/2.10/04_EFI_System_Table.html#efi-image-entry-point) EFI initializes for us, ImageHandler (that has nothing to do with bitmaps and PNGs) and SystemTable. We the pass both to GNU-EFI's InitializeLib function.

Note that I added a C function called Cls that calls [ClearScreen](https://uefi.org/specs/UEFI/2.10/12_Protocols_Console_Support.html#efi-simple-text-output-protocol-clearscreen) then uses [SetAttribute](https://uefi.org/specs/UEFI/2.10/12_Protocols_Console_Support.html#efi-simple-text-output-protocol-setattribute) to set the text color to light green. The Terra function *Print()* there is just a convenience to cast the correct pointer type, it then calls GNU-EFI's *AsciiPrint()* function.

I also created a Makefile to document and automate building our program. It basically compiles our Terra code, links with GNU-EFI and make a PE executable that EFI expects.

```Makefile
{!content/posts/2025/05/28/Makefile!}
```

Again, details in <https://wiki.osdev.org/GNU-EFI>.

Now we need to build a FAT disk image with the .efi file we generated so we can boot it with [QEmu](https://en.wikipedia.org/wiki/QEMU). To make things simpler I added the package *ovmf* on the Docker container that provides a BIOS image with EFI support (it will be copied by the script bellow) so all you need to do is install the package for your host system that provides qemu-system-x86_64. Then inside the container you can run the following script:

```bash
{!content/posts/2025/05/28/pack.sh!}
```
As instructed, copy the command line and run on your host system that line, you should see this:

![Screenshot of QEmu showing we succeded clearing the screen and setting the text to light green and printed our messages](/posts/2025/05/28/hello.png "Hello, World from Terra!")

If you want to play with the code you can keep calling `$ make && ./pack.sh` inside the container when you want to try a change and in another terminal you call QEmu to test it.

If you have a computer with an unlocked EFI you can even try to run hello.efi on baremetal.

## Conclusion

This article is inspired and based on some code I put together almost 10 years ago as a proof of concept using more C: <https://github.com/xspager/hello_efi_from_terra>. I could probably do things in better ways (let me know if have some ideas), and be better at showing the Terra language, but I was more interested sharing what I did. Also if you interested on UEFI check [Queso Fuego's playlist on YouTube](https://www.youtube.com/watch?v=t3iwBQg_Gik&list=PLT7NbkyNWaqZYHNLtOZ1MNxOt8myP5K0p).

I might add a part 3 to show how you can you put some pixels in the screen. Feel free to leave a comment or message me on BlueSky. Bye for now!