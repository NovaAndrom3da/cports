pkgname = "python-configargparse"
pkgver = "1.7"
pkgrel = 2
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python"]
checkdepends = ["python-pytest", "python-pyyaml"]
pkgdesc = "Drop-in replacement for argparse"
license = "MIT"
url = "https://github.com/bw2/ConfigArgParse"
source = f"$(PYPI_SITE)/C/ConfigArgParse/ConfigArgParse-{pkgver}.tar.gz"
sha256 = "e7067471884de5478c58a511e529f0f9bd1c66bfef1dea90935438d6c23306d1"
# needs updating for 3.13
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
