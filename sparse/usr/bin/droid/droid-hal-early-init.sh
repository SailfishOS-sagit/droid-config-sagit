#!/bin/bash
# Verbose script for mounting custom partitions
 
# Custom Partitions mounted
modem_part=/data/.stowaways/firmware/modem.img
dsp_part=/data/.stowaways/firmware/dsp.img
bluetooth_part=/data/.stowaways/firmware/bluetooth.img
vendor_part=/data/.stowaways/firmware/vendor.img
system_part=/data/.stowaways/firmware/system.img

# custom patches

dmesg_info() {
    echo "[mount-partitions.sh] $@" > /dev/kmsg
}

dmesg_info "Mount dynamic partitions"
mkdir -p /system_root /vendor /mnt

dmesg_info "$(mount -v -o loop,ro,barrier=1,discard -t ext4 $system_part /system_root)"
dmesg_info "$(mount --bind /system_root/system /system)"
dmesg_info "$(mount -v -o loop,ro,barrier=1,discard -t ext4 $vendor_part /vendor)"
dmesg_info "$(mount -v -o loop,ro,shortname=lower,uid=1000,gid=1000,dmask=227,fmask=337 -t vfat $modem_part  /vendor/firmware_mnt)"
dmesg_info "$(mount -v -o loop,ro,nosuid,nodev,barrier=1 -t ext4 $dsp_part /vendor/dsp)"
dmesg_info "$(mount -v -o loop,ro,shortname=lower,uid=1002,gid=3002,dmask=227,fmask=337 -t vfat $bluetooth_part /vendor/bt_firmware)"

# bind custom patches

# comment out when everything works
dmesg_info "$(findmnt)"
