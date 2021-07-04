# These and other macros are documented in
# ../droid-configs-device/droid-configs.inc
# ../droid-configs-device/droid-configs.inc
%define device sagit
%define vendor xiaomi
%define vendor_pretty Xiaomi
%define device_pretty Mi 6
%define rpm_device sagit
%define dcd_path ./
# Adjust this for your device
%define pixel_ratio 1.8

# Community HW adaptations need this
%define community_adaptation 1

%define android_version_major 10

# Device-specific ofono configuration
Provides: ofono-configs
Obsoletes: ofono-configs-mer

%define ofono_enable_plugins bluez5,hfp_ag_bluez5 
%define ofono_disable_plugins bluez4,dun_gw_bluez4,hfp_ag_bluez4,hfp_bluez4,dun_gw_bluez5,hfp_bluez5

%include droid-configs-device/droid-configs.inc
%include patterns/patterns-sailfish-device-adaptation-sagit.inc
%include patterns/patterns-sailfish-device-configuration-sagit.inc

# IMPORTANT if you want to comment out any macros in your .spec, delete the %
# sign, otherwise they will remain defined! E.g.:
#define some_macro "I'll not be defined because I don't have % in front"
