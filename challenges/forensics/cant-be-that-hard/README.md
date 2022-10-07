# can't be that hard

**`Author:`** [KptCheeseWhiz](https://github.com/KptCheeseWhiz)

## Description

The flag is right there! It can't be that hard to read it.. right?

## Files

[Download the disk of the virtual machine](https://static.unitedctf.ca/6057b30d31893d354e045f7c8a856fd4/cant-be-that-hard.zip)

## Solution

The VM is a minimal Archlinux with an encrypted root partition. That partition automaticaly unlocks on boot which means the key is somewhere on the disk itself. The key is packaged by default into the initramfs under the name `/crypto_keyfile.bin`. Note: I forgot to remove the `/crypto_keyfile.bin` from the root disk, so you could try to retreive it directly without extracting it from the initramfs.

Steps from another Linux instance, the `X` in `/dev/sdX` should be replaced by the challenge's disk letter:
1. Unpack the initramfs in the `/dev/sdX2` partition, you will need the commands `zstd` and `cpio` to decompress it
2. Retrieve the `/crypto_keyfile.bin` from the uncompressed initramfs
3. Open the encrypted partition with the command `cryptsetup luksOpen --key-file crypto_keyfile.bin /dev/sdX3 root`
4. Mount the unlocked partition with the command `mount /dev/mapper/root /mnt`
5. Fetch the flag with the command `cat /mnt/home/jailed/flag.txt`
