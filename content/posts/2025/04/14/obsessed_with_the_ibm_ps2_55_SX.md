Title: Obsessed with the IBM PS/2 55 SX
Category: vintage computing
Status: published
Tags: emulation, ibm, pc, ps/2, linux, os/2, 86box, netbsd, aix
Date: 2025-04-14 21:40
Cover: /images/Ibm_8555-401_front_linux.jpg

![Picture of an IBM PS/2 55 SX](/images/Ibm_8555-401_front_linux.jpg "Original image credit to <https://web.archive.org/web/20230308035226/https://www.okqubit.net/machines/ibm.html>")

I got a bit obsessed about running Linux on the IBM PS/2 [^1] 55SX after watching the video Clabreto made <https://www.youtube.com/watch?v=m-Xq-SpCu3o> about it. The PS/2 was the IBM's attempt at getting back the PC market after loosing it to the PC clones. It still used Intel CPUs but the BIOS was different and the expansion interface [ISA](https://en.wikipedia.org/wiki/Industry_Standard_Architecture) was replaced with [MCA](https://en.wikipedia.org/wiki/Micro_Channel_architecture). It's BIOS don't have a regular configuration interface like the orignal IBM and it's clones a XT or a modern EFI based system, you need what they call a Reference Floppy, a floppy disk they provide you with defaults and a bootable program to set up the BIOS. The configurations are persisted across boots in a volatile memory commonly knowns as CMOS backed by a battery (like a PC/XT) that usually powers the real time clock too. This battery dying is the source of a lot of frustration if you want to use this machines long after their prime.

## You wouldn't download a computer?

You might wonder how I got my hands on a [IBM PS/2 55 SX](https://en.wikipedia.org/wiki/IBM_PS/2_Model_55_SX). I did in fact at some point had a lot of old 8088, 80186, 80286, 386, 486 and pentium based machines, but never a PS/2. So one this days I was trying to run the game Wipeout and got this ready made configuration and disk image to run it on [86Box](https://86box.net/). I had heard about it before and (it's often mistaken for project Box86), so thought I might had the solution at hand.

86Box, like QEmu and others can emulate a generic machine but it can emulate some specific computer models and hardware, like graphics cards and motherboards with the original firmware. It seem simple at first, I just selected the right CPU, a 386SX[^2], and the machine model, then getting the correct Reference Floppy, [this one](https://www.ardent-tool.com/disks/rf5565x.zip), from the awesome (and awesomely named) [Ardent Tool of Capitalism](https://www.ardent-tool.com/) site, and I did got it right first try. Felt like I was watching a TV show and fallowing along at home, getting the same errors, the same error beeps, "inserting" the floppy, letting it do the automatic setup and seeing it beep just one time, confirming it was all ok, and booting a regular bootable floppy image, neat! It was then that the obsession got out of hand...

![Reference Floppy splash screen with the IBM classic logo](/images/reference_disk_splash.png "I agree with Clabreto, this is a nice render of the classic IBM logo")

Just follow the instructions on the screen, and in the end you will see:

![Final screen asking you to press Enter to reboot](/images/refrence_disk_finish_config.png "and we done")

Now the machine should reboot after you hit Enter and beep only once and boot any regular boot floppy or hard disk.


## Tunnel vision

I went looking for an old Linux distro, a most up to date release from the time this machine was relevant to Linux users. I think I tried Slackware first [issue I had] and Debian, I had a look at Damn Small Linux and even went for a [BSD](https://en.wikipedia.org/wiki/Berkeley_Software_Distribution), NetBSD was the obvious option since it runs on everything even on the latest version (I might go back and look into old FreeBSD releases). The PS/2 specific image boots it asks for the second floppy but it can't find the harddisk. Until then it was all fine.

Then I spent way to much time trying all floppy images that had any chance to boot and trying to tweak the virtual machine only it did boot but would not find the hard disk.

I was facing this issue with 86Box, every time I tried to swap floppy images it would crash. It was fine at first since every boot disk I tried never went anywhere but I think once I decided to install DOS and got to the point it asked for the next install disk, I had to figure out what was wrong with 86Box. That meant learning how to debug a flatpaked application. I had a lot of frustration because I refused to follow the instruction, and few gigabytes of download later I could get GDB to divulge the stack trace from the core dump. The issue was memory being deallocated before the code that keeps track of the list of images you used recently, used it. Turns out it was already fixed but not present on the version latest public release (4.2.1) of 86Box.

Well, I learned later that if you run 86Box as a AppImage, even 4.2.1, the latest release as of now, won't present the bug, fine, whatever.

I still faced some other issues getting errors saying that the disk controller was having a conflict and maybe the contents of the CMOS getting lost or corrupted. But once I found out where the 86Box project hosts the [latest builds](https://ci.86box.net/job/86Box/lastBuild/artifact/Old%20Recompiler%20(recommended)/), they no longer happened and I managed to finally install the infamous OS/2 ([this version from here](https://winworldpc.com/product/os-2-20/20) to be exact) and everything seems to be working fine.

## OS/2

Nothing to report here just download OS/2 2.0 from <https://winworldpc.com/product/os-2-20/20> or OS/2 3.0 <https://winworldpc.com/product/os-2-3x/os-2-30>, I managed to install and run <s>both without an issue</s> OS/2 2.0 but I can't seem to figure out how to boot 3.0 after the install.

![OS/2 3.0 boot screen](/images/os2_3_0_boot_screen.png "It does install and shows the boot screen")

## Attempt installing AIX

[AIX](https://en.wikipedia.org/wiki/IBM_AIX) is an IBM Unix system orignially for the IBM RT PC RISC workstation.

For starters the name of floppy images that are supposed to boot a installer with support for the [ESDI](https://en.wikipedia.org/wiki/Enhanced_Small_Disk_Interface) interface are inverted, the image *Boot_(ESDI)_02.img* is the only one of the two that boots and when asked to insert the "second floppy" it accepts the image *Boot_(ESDI)\_02.img*

![IBM AIX install asking for some configuration](/images/AIX_install_attempt.png "It asks for a few informations")

![IBM AIX install loading from the first(but named Boot_(ESDI)\_02.img floppy](/images/AIX_install_attempt_second_screenshot.png "Loading from the first floppy image named Boot_(ESDI)_02.img")

![IBM AIX install asking for the installation diskette](/images/AIX_install_attempt_third_screenshot.png "This is where I got stuck")

I had to screen capture what happens after this to see the errors because it happens too fast.

<s>Cool, but I still haven't figured out what it means by "installation diskette" yet.</s> You need a prestine copy of the Install floppy image for it to advance one step, so make sure to use a copy or download/decompress the original image if things goes wrong, also make the sure the image file is writable. But stil, I get a kind of kernel panic (see the image bellow).

![AIX install kernel panic](/images/AIX_install_attempt_fourth_screenshot.png "KERNEL TRAP")

I could not find in this installation guide anything I was doing different <https://www.ardent-tool.com/AIX_1-3/AIX_1-3_Installation.html>

This is another place to find the floppy images for AIX 1.3 <http://ps-2.kev009.com/aixps2/InstallImages/>

## Damn (Small Linux)

I got Damn Small Linux to boot but since 8 MB is not enough to load the CDROM kernel module I'm dropped into a very limited shell.

## NetBSD

NetBSD still supports PS/2 to this day <https://www.netbsd.org/ports/i386/ps2.html>. You will need to grab the floppy images from <https://cdn.netbsd.org/pub/NetBSD/NetBSD-10.1/i386/installation/floppy/>. Rename them from .fs to .img

No luck, NetBSD can't find the ESID disk and disable the controller.

![NetBSD edc driver's message about disabling the controller because it could not no disks were found](/images/netbsd_disabling_controllers.png "edc0: disabling controller (no drivers attached)")

![NetBSD message about not finding a disk](/images/netbst_message_about_disk.png "No disk found after a few installation steps")

Same goes for old versions like 3.0.3 <https://archive.netbsd.org/pub/NetBSD-archive/NetBSD-3.0.3/i386/installation/floppy/>, 6.1.5 and I even tried 2.1 <https://archive.netbsd.org/pub/NetBSD-archive/NetBSD-2.1/i386/installation/floppy/> and 1.6.2 <https://archive.netbsd.org/pub/NetBSD-archive/NetBSD-1.6.2/i386/installation/floppy/>. The minimum memory requirements and CPU were a concern but it seems that there is a bug on the NetBSD driver or on 86box. Not in the mood to debug either. Maybe other BSD have a different driver and will run on the 55 SX.

Well, check [ADF files](#adf-files) to see what I did but now I can see the SCSI controller BIOS message listing the disk. The install happened without an issue once I added a SCSI CDROM drive and use a folder with all the NetBSD 3.0.3 sets.

![NetBSD 3.0.3 Installing](/images/netbsd_install.png)

And then after the install, trying to get the boot order correct by removing the ESID disk, the BIOS went crazy and won't set up the SCSI controller correctly anymore. I give up for now.

## FreeDOS

*"[FreeDOS](https://www.freedos.org/) is a DOS-compatible operating system..."*. Very slow to install but seems to work fine. I assume it relies fully on BIOS interrupts to work.

Download the install floppy images from <https://www.ibiblio.org/pub/micro/pc-stuff/freedos/files/distributions/1.4/FD14-FloppyEdition.zip>

## ADF files

The way the Reference Floppy knows how to setup devices automatically is thought .ADF files present on it. You can find the ones based on the device id. I had a try adding the ones for the SCSI controllers that 86box emulates with mix success and I'm not sure anymore if I was doing it correctly. If you want to give it a try you only need to download and copy the files to the Reference Floppy and Ardent Tool of Capitalism got us covered <https://www.ardent-tool.com/adapters/ADF.html>

Alright, I gave it another try, and I think I got *Adaptec AHA-1640* SCSI controller working by copying <https://www.ardent-tool.com/adapters/adf/@0f1f.adf> to the Reference Floppy letting the automatic setup configure it.

## Let's try to update the 55 SX BIOS

There are no checks of the ROM files 86box relies on, so you can just drop a compatible version of the machine's BIOS with the same names and expect it to work, as long as they are the same size.

I downloaded <https://www.ardent-tool.com/firmware/system/8555/SX/92F0626.zip> and <https://www.ardent-tool.com/firmware/system/8555/SX/92F0627.zip> from <https://www.ardent-tool.com/firmware/system.html>. Note that 92F0627.rom should be renamed 33f8146.zm41 and 92F0627.rom to 33f8145.zm40 (maybe it's the reverse, you will know if it is right if the machine boots.

Unfortunately I didn't notice any advantage on doing that.

## Conclusion

Beyond the success running OS/2 and FreeDOS, booting the NetBSD's and the AIX's installers I still haven't managed to go much further than limited shells, specially with Damn Small Linux (0.8 ???).

I haven't managed to get any other disk controller but the one that works for OS/2, neither IDE nor SCSI.

I think I'm cured from the madness, for now.


If you have any question or suggestion feel free to leave a comment or reach out on Bluesky.


[^1]: Not to be mistaken with the Sony game console PS2, that funny enough got an IBM [Cell](https://en.wikipedia.org/wiki/Cell_(processor)) CPU on it's third generation, the PS3, a mix of PowerPC and some math optimized coprocessors.

[^2]: Without an internal FPU and only a 16 bits external bus to make it cheaper, like in the original IBM PC with it's [Intel 8088 CPU](https://en.wikipedia.org/wiki/Intel_8088), instead of the regular 32 bits external bus. In the case of the 8088 it had a 8 bits external bus unlike the 8086 that had a full 16 bits external bus.

*[BIOS]: Basic Input Output System
*[ISA]: Industry Standard Architecture
*[MCA]: Micro Channel Architecture
*[BSD]: Berkeley Software Distribution
*[ADF]: Adapter Description File
