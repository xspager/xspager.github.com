#/usr/bin/env bash
set -e

if [ ! -f uefi.img ]; then
	#dd if=/dev/zero of=uefi.img bs=512 count=$(((10 * 1024 * 2))) 2> /dev/null # 10MB
    truncate --size 10MB uefi.img

    #mformat -i uefi.img -f 1440 ::
    mformat -i uefi.img
    mmd -i uefi.img ::/EFI
    mmd -i uefi.img ::/EFI/BOOT
fi

if [[ $(mdir -i uefi.img ::EFI/BOOT/BOOTx64.EFI 2> /dev/null) ]]; then
    mdel -i uefi.img ::EFI/BOOT/BOOTx64.EFI
fi

mcopy -i uefi.img hello.efi ::/EFI/BOOT/BOOTx64.EFI

if [ ! -f OVMF.df ]; then
    cp /usr/share/ovmf/OVMF.fd .
fi

echo "Run the following command outside of the docker container:"
echo "qemu-system-x86_64 -bios OVMF.fd -drive file=uefi.img,index=0,media=disk,format=raw,if=ide -enable-kvm -vga cirrus -cpu kvm64 -device virtio-mouse-pci -usb -device usb-mouse"

# If you want to use the serial port to debug
##  socat -,raw,echo=0 tcp4:localhost:6666
#qemu-system-x86_64 -bios OVMF.fd -drive file=uefi.img,index=0,media=disk,format=raw,if=ide -enable-kvm -vga cirrus -cpu kvm64 -monitor stdio -serial tcp::6666,server -s