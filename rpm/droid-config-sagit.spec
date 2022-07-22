# ../droid-configs-device/droid-configs.inc
%define device sagit
%define vendor xiaomi
%define vendor_pretty Xiaomi
%define device_pretty Mi 6
%define rpm_device sagit
%define dcd_path ./
# Adjust this for your device
%define pixel_ratio 1.75

# Community HW adaptations need this
%define community_adaptation 1

# OTA via self-hosted repo needs to have all adaptation-community repos removed
Conflicts: community-adaptation-testing
Obsoletes: community-adaptation-testing

%define android_version_major 10

# Device-specific ofono configuration
Provides: ofono-configs
Obsoletes: ofono-configs-mer
Obsoletes: ofono-configs-binder

Requires: libgbinder-tools
Obsoletes: qt5-qpa-surfaceflinger-plugin

Provides: usb-moded-configs

%define ofono_enable_plugins bluez5,hfp_ag_bluez5 
%define ofono_disable_plugins bluez4,dun_gw_bluez4,hfp_ag_bluez4,hfp_bluez4,dun_gw_bluez5,hfp_bluez5

%include droid-configs-device/droid-configs.inc
%include patterns/patterns-sailfish-device-adaptation-sagit.inc
%include patterns/patterns-sailfish-device-configuration-sagit.inc
