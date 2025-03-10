pkgname = "gnome-control-center"
pkgver = "45.2"
pkgrel = 0
build_style = "meson"
make_check_wrapper = ["weston-headless-run"]
hostmakedepends = [
    "meson",
    "pkgconf",
    "gobject-introspection",
    "gettext",
    "glib-devel",
    "polkit",
    "python",
    "tecla",
]
makedepends = [
    "libhandy-devel",
    "accountsservice-devel",
    "colord-devel",
    "colord-gtk-devel",
    "glib-devel",
    "gnome-desktop-devel",
    "gnome-settings-daemon-devel",
    "gnome-online-accounts-devel",
    "gsettings-desktop-schemas-devel",
    "libxml2-devel",
    "polkit-devel",
    "libpulse-devel",
    "upower-devel",
    "libgudev-devel",
    "libx11-devel",
    "libxi-devel",
    "libepoxy-devel",
    "gtk4-devel",
    "cups-devel",
    "ibus-devel",
    "networkmanager-devel",
    "modemmanager-devel",
    "gnome-bluetooth-devel",
    "libwacom-devel",
    "gcr-devel",
    "libnma-devel",
    "libsecret-devel",
    "udisks-devel",
    "gsound-devel",
    "libgtop-devel",
    "heimdal-devel",
    "libpwquality-devel",
    "libsmbclient-devel",
    "gnutls-devel",
]
depends = [
    "desktop-file-utils",
    "tecla",
    "udisks",
    "cups-pk-helper",
    "gsettings-desktop-schemas",
    "power-profiles-daemon-meta",
    "sound-theme-freedesktop",
]
checkdepends = ["python-dbusmock", "weston"] + depends
pkgdesc = "GNOME control center"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://gitlab.gnome.org/GNOME/gnome-control-center"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "0cfa3c332d6edacb73d06c6b26ffca1078e86ff59eac819b2931e0967753df70"


@subpackage("gnome-control-center-devel")
def _devel(self):
    self.depends += [f"{pkgname}={pkgver}-r{pkgrel}"]

    return self.default_devel()
