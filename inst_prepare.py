#!/usr/bin/python3

import os

bash = os.system
def install_gentoo():
    
    DictRelease = {
        1: "stage3-amd64-desktop-openrc",
        2: "stage3-amd64-desktop-systemd",
        3: "stage3-amd64-nomultilib-openrc",
        4: "stage3-amd64-nomultilib-systemd"
    }
    print("Select your redation for install \n"
        "1. Desktop OpenRC. \n"
        "2. Desktop SystemD. \n"
        "3. No-multilib OpenRC. \n"
        "4. No-multilib SystemD. \n"
        "5. Exit. \n"
    )
    release = int(input("Select: "))
    print("\n")

    if release in DictRelease:
        bash("wget https://mirror.yandex.ru/gentoo-distfiles/releases/amd64/autobuilds/latest-{}.txt".format(DictRelease.get(release)))
        with open("latest-{}.txt".format(DictRelease.get(release)), "r") as txtfile:
            txt=txtfile.readlines()
        newtext = str(txt[-1].split("/")[0])
        bash("wget https://mirror.yandex.ru/gentoo-distfiles/releases/amd64/autobuilds/current-{}/{}-{}.tar.xz".format(DictRelease.get(release), DictRelease.get(release), newtext))
        bash("rm -r latest-*.txt")
        bash("tar xvpf {}-{}.tar.xz --xattrs-include='*.*' --numeric-owner".format(DictRelease.get(release), newtext))
        print("\n")
        mounting_root()

    elif release == 5:
        print("\n")
        print("Good Bye! \n")
        quit()
        
    else:
        print("Error. Invalid input \n")
        input("Press Enter for exit")
        quit()

    
def mounting_root():
    print("\n")
    bash(
        "mount --types proc /proc proc && "
        "mount --rbind /sys sys && mount --make-rslave sys && mount --rbind /dev dev && mount --make-rslave dev && mount --bind /run run && mount --make-slave run && "
        "cp /etc/resolv.conf etc/ && mkdir --parents etc/portage/repos.conf && cp usr/share/portage/config/repos.conf etc/portage/repos.conf/gentoo.conf && "
        "echo Welcome to Gentoo chroot! && "
        "chroot . /bin/bash"
    )

print("\n")
print("Hello to Gentoo easy mounting :) \n")

print(
    "1. Prepare to install Gentoo. \n"
    "2. Mounting root and chroot. \n"
    )

inst = int(input("Select: "))
print("\n")
targetdir = input("Input Directory for chroot: ")
print("\n")

bash("lsblk")
print("\n")

instGentoo = input("Select root drive: /dev/")

bash("mkdir {} &> /dev/null".format(targetdir))
bash("mount /dev/{} {}".format(instGentoo, targetdir))
os.chdir(targetdir)

if inst == 1:
    install_gentoo()
elif inst == 2:
    mounting_root()
else:
    print("Error. Invalid input. \nExit.")
    quit()
