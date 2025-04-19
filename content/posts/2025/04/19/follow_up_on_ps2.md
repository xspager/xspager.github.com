Title: Follow up on PS/2 55 SX
Category: vintage computing
Tags: emulation, ibm, pc, ps/2, 86box, netbsd
Status: published
Cover: /images/netbsd_dmesg.png

So I did got back to playing with NetBSD on the PS/2 55 SX as I was afraid I would ([check the original article here]({filename}../14/obsessed_with_the_ibm_ps2_55_SX.md)) and got it running. To be exact I got NetBSD 3.0.3 to install and run as I mentioned before, and after sorting the BIOS issues by deleting the file that store the non-volatile contents of the emulated BIOS and recreating the Reference Floppy with the .ADF files I still had to resort to using the installation boot disk to boot the installed system. By pressing any key and entering "boot hd1a:netbsd".

![Result of calling the command dmesg](/images/netbsd_dmesg.png)

I also got one network interface to work and used it to ping the Google servers but I could not test an HTTP connection due to the lack of a client program like WGet, cURL or even netcat.

![Ping Google.com](/images/netbsd_ping.png)

I manage to compile a hello world program:

![Hello, world on NetBSD 3.0.3](/images/netbsd_hello.png "Hello, PS2! (O2 to make it run really fast)")

I'll leve the screenshots of the setting I used and here the [86Box config file](/static/ibm_ps2_55_SX_good_86box.cfg)

![86Box Setting, Machine](/images/86Box_config_machine.png)

![86Box Setting, Display](/images/86Box_config_display.png)

![86Box Setting, Network](/images/86Box_config_network.png)

![86Box Setting, Storage](/images/86Box_config_storage.png)

![86Box Setting, Hard Disks](/images/86Box_config_hds.png)

To be honest I tried to manually install packages for a new version of NetBSD by adding a virtual SCSI CDROM driver and I could mount it (*mount -t iso9660 /dev/cd0a /mnt*) and copy the files, but it obviusly was not a very smart idea. I'm sure you could compile wget or something from source using the same method but I'm done with this. For now?