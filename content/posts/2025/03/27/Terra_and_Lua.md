Title: Terra and Lua
Category: programming
Status: published
Tags:lua, terra, c, lowlevel, uefi
Date: 2025-03-27 11:51
Cover: /images/pexels-pixabay-87009.jpg
Series: Terra and Lua

![Picture from Pixabay : https://www.pexels.com/photo/blue-and-white-planet-display-87009/](/images/pexels-pixabay-87009.jpg "Famous Apollo 8 image titled *Earthrise*")

Let's write some code that uses the services provided by the (U)EFI (modern BIOS) environment and we gonna use [Terra](https://terralang.org/), as is says in their website, a counterpart to [Lua](https://lua.org/). I'll assume that you know some C for Part 1.

[TOC]

## What is Terra?
*"Terra is a low-level system programming language that is embedded in and meta-programmed by the Lua programming language"*. This means you can write some typed code that looks like Lua, embed some Lua code, and compile the whole thing to machine code.

To install Terra you should have a look at their install guide <https://terralang.org/getting-started.html#installing-terra>

Now we can run some regular Lua code by passing it to terra

```lua
{!content/posts/2025/03/27/hello.lua!}
```

```bash
$ terra simple_hello.lua 
Hello, World!
```

## Calling a C functions from Terra

That was not very exiting, right? Now, let's call C's printf function to print our message:

```lua
{!content/posts/2025/03/27/hello_C.t!}
```

```bash
$ terra hello_C.t 
Hello, C!
```

## Generating some machine code

What if we could write a some "Lua" and compile it to a independent binary program?

```lua
{!content/posts/2025/03/27/hello_world_bin.t!}
```

```bash
$ terra hello_world_bin.t 
$ ./helloterra 
Hello, Terra!
$ ldd
	linux-vdso.so.1 (0x00007da5c64a9000)
	libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007da5c6200000)
	/lib64/ld-linux-x86-64.so.2 (0x00007da5c64ab000)
# we depend on no library or interpreter
```

## Getting command line parameters

The main function can have any name btw. We can pass treat that function the same the main funtion in C and get *argc* and *argv* from the OS

```lua
{!content/posts/2025/03/27/hello_world_args.t!}
```

```bash
# now we call terra to run our code and this will create our binary
$ terra hello_world_args.t
# call the resulting binary with three parameters
$ ./helloargs foo bar baz
Hello, Terra!
argv[0] ./helloargs
argv[1] foo
argv[2] bar
argv[3] baz
# Try renaming helloterra to something else and have a look at argv[0] (this is how busybox works)
```

## How Lua is part of this?
Here I would show how you can write some regular Lua code and call it from a compiled Terra program but that's not possible yet.

## The next part
On part 2 we will learn how to get code to run on the (U)EFI environment using GNU-EFI and QEmu.


This article is based on something similar I did long time ago: <https://github.com/xspager/hello_efi_from_terra>

*[BIOS]: Basic Input Output System