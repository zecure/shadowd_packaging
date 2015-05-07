# Copyright 1999-2015 Gentoo Foundation
# Distributed under the terms of the GNU General Public License v2
# $Header: $

EAPI=2
inherit cmake-utils user systemd

DESCRIPTION="Shadow Daemon web application firewall"
HOMEPAGE="https://shadowd.zecure.org/"
SRC_URI="https://shadowd.zecure.org/files/${P}.tar.gz"

LICENSE="GPL-2"
SLOT="0"
KEYWORDS="~amd64 ~x86"
IUSE="+mysql +postgres"

DEPEND="
	>=dev-util/cmake-2.8.12
	>=dev-libs/openssl-1.0.1
	>=dev-libs/boost-1.55.0
	>=dev-libs/jsoncpp-0.5.0
	>=dev-libs/crypto++-5.6.2
	>=dev-db/libdbi-0.9.0"

RDEPEND="${DEPEND}
	mysql?    ( dev-db/libdbi-drivers[mysql] )
	postgres? ( dev-db/libdbi-drivers[postgres] )"

pkg_setup() {
	enewgroup shadowd
	enewuser shadowd -1 -1 /dev/null shadowd
}

src_install() {
	newinitd "${FILESDIR}"/shadowd.initd shadowd
	newconfd "${FILESDIR}"/shadowd.confd shadowd
	systemd_dounit "${FILESDIR}/${PN}.service"

	cmake-utils_src_install
	fowners shadowd:shadowd /etc/shadowd/shadowd.ini
}
