Title: How to (not) Install C on the AOS on a Nova MV
Category: programming
Status: published
Tags: data general, nova, bcpl, alto
Date: 2025-05-26 21:18
Cover: /images/Data-General-Nova-System-Museum-Enter-6095073.jpg

![a Nova rack in the center with a terminal on the top, PDP-11/35 control panel to the left on top of some other smaller rack a Data General branded teletype terminal in betwen the two and an old large ociloscope behine. On the right a table with a glass terminal with the Data General colors.](/images/Data-General-Nova-System-Museum-Enter-6095073.jpg "Credits:  	Bobo11 <https://commons.wikimedia.org/wiki/File:Data-General-Nova-System-Museum-Enter-6095073.jpg>")

## Motivation

I have this idea of restoring the [Mesa](https://en.wikipedia.org/wiki/Mesa_(programming_language))/[Cedar](https://en.wikipedia.org/wiki/Mesa_(programming_language)#Cedar) compiler but discipline and skill are lacking. I have documented the progress I made [from a archive that was released](https://xeroxalto.computerhistory.org/) by the [Computer History Museum](https://en.wikipedia.org/wiki/Computer_History_Museum) while ago in <https://github.com/xspager/Cedar_tools>.

So I was the other day watching the a [Data General Nova](https://en.wikipedia.org/wiki/Data_General_Nova) being restored ([Usagi Electric playlist](https://www.youtube.com/playlist?list=PLnw98JPyObn2PqgY1mfzXOtnUXlsXSMch), [Tech Tangents playlist](https://www.youtube.com/playlist?list=PLJVwF78cppBgwAHYKMffuhs0jblPHCyvL)) and wondered if I could get myself familiar with the software on that platform and see if that helps with recreating the kind of environment that was used to develop the [BCPL](https://en.wikipedia.org/wiki/BCPL) compiler and the rest of the software for the [Xerox Ato](https://en.wikipedia.org/wiki/Xerox_Alto).

I did not managed to figure out yet how to install the C development tools and libraries from the magnetic tape[^1], on the AOS operating system for the [Nova MV](https://en.wikipedia.org/wiki/Data_General_Eclipse_MV/8000) (obviously not the generation of Novas that were available at the time) and I'm not implying it was used or was event available at the time, I just bumped into it and wanted to try. The Alto implemented the Nova instruction sed and was programmed in Microcode, Assembly for the Nova and BCPL. C was not around at the time. It would be born from [B](https://en.wikipedia.org/wiki/B_(programming_language)) that itself was a descendent from BCPL.

## Going Nova

Of course I don't have access to a working Nova so I'm using what I believe is a fork (or a build, not sure) of the [SimH emulator](https://opensimh.org/) from the great resource [Novas are Forever](http://www.novasareforever.org/emulators/emulator-downloads). Specifically the MV emulator and the configuration and disk image provided there. You can find all kinds of magnetic tapes in the SimH 9trk file format with software.

```bash
# change mv.x86 to the binary for your platform (win/mv.exe for windows)
$ wget http://www.novasareforever.org/user/archive/public/wh/simh/mv/{progs/ubuntu/mv.x86,ini/simh.ini.aosvs,disks/DZP.6060.AOSVS.raw}
$ chmod +x mv.x86
$ ./mv.x86 simh.ini.aosvs
```

Ok, so let me show what learned:

After you start the emulator you will have to press enter to accept the default options for the two prompts you will see.

```text
                Operating System Load Menu

        1  Continue immediately with operating system load
        2  Enter the Technical Maintenance Menu

        Loading will continue automatically unless you respond
        within 45 seconds.

        The default system pathname is INSTALLED SYSTEM

        For assistance, press the Help key (SHIFT-F1) or H


        Enter choice [1]: 



AOS/VS Rev 7.73.00.00

Master LDU: DPF0

AOS/VS will continue with defaults automatically 
unless you respond within 00:00:30

Override default specs [N] ? 

From system on 26-May-25 at 19:26:39
Terminal Services initialization started
    Number of console lines genned : 0


From system on 26-May-25 at 19:26:39
Terminal Services initialization complete

AOS/VS CLI   Rev 07.73.00.00    26-MAY-25       19:26:39
) 
```

The ")" you see above is the prompt. Some commands include:

- DIR - show or set the current directory, like *cd* combined with *pwd* in Unix
- PATHNAME - show the path of a file, use "=" for the same effect of calling dir without parameters
- FILESTATUS - much like **ls** on Unix
- HELP - without parameters show a list of topics you can get help about, note the asterisk before the topic. You don't need it for help with commands.
- XEQ SED - run the text editor sed (not sure yet why some commands require to be called with xeq), somewhat similar to Vi
- TYPE - like the same command on MS-DOS
- SUPERUSER - show if you are a super user or not, you become a superuser by passing "ON" as parameter. The prompt becomes "Su)". You are only able to configure the system and do some other stuff as a super user, there is a pretty advance user permission system you can configure.

Novas are Forever have the AOS User Handbook <http://www.novasareforever.org/user/archive/public/docs/dg/sw/os/aos/093-000150-01__AOS_Users_Handbook__1979.pdf> if you want to have a look at other available commands. You should also check the other documentation they have: <http://www.novasareforever.org/archives/documentation/dg.sw/dg.sw.os>.

Some curiosities about this OS:

- The commands (at least) are case insensitive, so "dir" and "DIR" work the same
- You don't need to write the full command, just enough to match a unique command, so calling `fi` or `filestatus` have the same effect
- The root and the path separated is columns ":", so :UTIL:SED.PR is a full path to the SED.SR file in the UTIL directory
- Flags for the commands don't have spaces, so `HELP/V fi` will show the verbose help for the `filestatus` command
- CTRL-A will bring back the previous typed command line
- Peripherals can be refered by path and are present on :PER or using an "@" symbol as a shortcut, *:PER:MTC0* and *@MTC0* refer to the same peripheral

## SED editor
It's a modal editor, you use the escape key to get to the command line like Vi but to exit you use the **bye** command. You can pass a file as a command line argument like you would expect.

![screenhot of the terminal showing a helloword program in C being edited with SED](/posts/2025/05/26/sed_editing_hello_dot_c.png "SED editing a hello world program in C")

![screenshot og the terminal showing the help page for SED](/posts/2025/05/26/sed_help.png "SED help")

## Attaching a magnetic tape and loading
You can either drop to the emulator shell with `CTRL-E` or edit simh.ini.aosvs and use/add `Attach MTA [some_tape_file.9trk]` to mount a tape to the peripherals MTC0 in the AOS naming scheme. To return to go back to the AOS prompt use the emulator command *c* for *continue*. The command `load` is used to load dumps from the tape

The tape I tried to load is: <http://www.novasareforever.org/user/archive/public/sw/dg/mv/lang/c/071-000752-11__AOS-VS_C_rev_6.00__1982-1994__30053.9trk>

## Turning the computer off
Just type `bye` and it will propt if you really want to shut the syetem down, press y, then Enter to confirm, you will drop at the emulator prompt, then you can use either *exit* or *quit* to exit the emulator.

## Final note
Hopeful you got something out of this article. If you have any idea on how to get the C tape loaded on AOS let me know. If you have any interest or an idea on how to get the Cedar/Mesa compiler working talk to me on Bluesky or open an issue in <https://github.com/xspager/Cedar_tools>

[^1]: it might not be good, but I manage to rewind and dump two files from it so at least I figured out what is the right device to read from (MTC0)