# Filename: m2p2.py
# Author: Zachary Milne
# Course: ITSC203
# Details: Create Output that looks like the sample below:
    # Report generated by: John Smith
    # Contact	: (contained an email, removed for privacy)
    # Date/Time	: Jan-12-2021  09:27:33 (utc: 232142341342)
    # File				: mytest.exe
    # Magic			: 0x5A4D
    # PE Header Offset	: 0x456
    # Format			: 64 bit
    # Endian			: big
    # Machine		: x86-64
    # Entry Point		: 0x401000

from datetime import date,timezone
import pefile
import datetime
import codecs

pe = pefile.PE("/home/zacky/Desktop/notepad.exe")
time = date.today()
dtime= datetime.datetime.now(timezone.utc)
utctime= dtime.replace(tzinfo=timezone.utc)
timestamp = utctime.timestamp()

if hex(pe.FILE_HEADER.Machine) == '0x14c':
    machine = 'x86'
else:
    machine = 'x64'
if hex(pe.OPTIONAL_HEADER.Magic) == '0x20b':
    fileform = '64 bit'
else:
    fileform = '32 bit'

print("Report generated by:  Zack Milne")
print("Contact:              zackmilne@madeupdomain.com")
print("Date/Time:           ",time.strftime("%B %d, %Y"), timestamp)
print("File:		      notepad.exe")
print("Magic:               ", hex(pe.DOS_HEADER.e_magic))
print("PE Header Offset:    ", hex(pe.DOS_HEADER.e_lfanew))
print("Format:              ", fileform)
print("Endian:               big")
print("Machine:             ", machine)
print("Entry Point:         ", hex(pe.OPTIONAL_HEADER.AddressOfEntryPoint))
