terralib.includepath = terralib.includepath..";/usr/include/efi;/usr/include/efi/x86_64;/usr/include/x86_64-linux-gnu/"

local target = terralib.newtarget {
	Triple = "x86_64-pc-none";
}

local C = terralib.includecstring([[
	#include <stdbool.h>
	#include <efi.h>
	#include <efilib.h>

	bool Cls()
	{
		EFI_STATUS status;

		// We need to use uefi_call_wrapper to match the calling convention used in EFI
		status = uefi_call_wrapper(ST->ConOut->ClearScreen, 1, ST->ConOut);
		// Set Text color to a light green
		uefi_call_wrapper(ST->ConOut->SetAttribute, 2, ST->ConOut, EFI_TEXT_ATTR(EFI_LIGHTGREEN, EFI_BACKGROUND_BLACK));

		if(EFI_ERROR(status)){
			Print(u"ERROR: Cls status %d", status);
		}
		return EFI_ERROR(status);
	}
]], {}, target)

-- EFI use 16bits strings by default so we can't use Print, we use AsciiPrint instead
-- this is just a convinience function to cast the int8 pointer to uint8
terra Print(str_p: &int8)
	C.AsciiPrint([&uint8](str_p))
end

terra hello_efi(ImageHandler: C.EFI_HANDLE, SystemTable: &C.EFI_SYSTEM_TABLE)
    C.InitializeLib(ImageHandler, SystemTable)

	if C.Cls() then
		Print("FAILED TO CLEAR SCREEN")
	end

    Print("Hello, World from Terra!\n")

    Print("\n\n\n")
    Print("Press any key to reboot\n")
    C.WaitForSingleEvent(SystemTable.ConIn.WaitForKey, 0)
	
    return C.EFI_SUCCESS;
end

-- we generate the object code and save it to hello_efi.o
terralib.saveobj('hello_efi.o', {
	efi_main=hello_efi,
},{
	"-fno-stack-protector",
	"-fpic",
	"-fshort-wchar",
	"-mno-red-zone",
}, target)