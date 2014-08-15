Summary:	Power manager for the Xfce desktop environment
Summary(pl.UTF-8):	Zarządca energii dla środowiska Xfce
Name:		xfce4-power-manager
Version:	1.3.1
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://archive.xfce.org/src/apps/xfce4-power-manager/1.3/%{name}-%{version}.tar.bz2
# Source0-md5:	b97bfabe8ad54baa11ac79aadcb6e81a
URL:		http://goodies.xfce.org/projects/applications/xfce4-power-manager
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.8
BuildRequires:	dbus-glib-devel >= 0.74
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.16.0
BuildRequires:	gtk+2-devel >= 2:2.12.0
BuildRequires:	intltool
BuildRequires:	libnotify-devel >= 0.4.1
BuildRequires:	libtool
BuildRequires:	libxfce4ui-devel >= 4.10.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.601
BuildRequires:	upower-devel
BuildRequires:	xfce4-dev-tools >= 4.11.0
BuildRequires:	xfce4-panel-devel >= 4.11.0
BuildRequires:	xfconf-devel >= 4.10.0
Requires:	gtk-update-icon-cache
Requires:	upower
Requires:	xfce4-dirs >= 4.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Power manager for the Xfce desktop environment.

%description -l pl.UTF-8
Zarządca energii dla środowiska Xfce.

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/locale/ur_PK
%{__rm} $RPM_BUILD_ROOT%{_libdir}/xfce4/panel/plugins/libxfce4battery.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%{_sysconfdir}/xdg/autostart/xfce4-power-manager.desktop
%attr(755,root,root) %{_bindir}/xfce4-power-manager
%attr(755,root,root) %{_bindir}/xfce4-power-manager-settings
%attr(755,root,root) %{_sbindir}/xfpm-power-backlight-helper
%attr(755,root,root) %{_sbindir}/xfce4-pm-helper
%attr(755,root,root) %{_libdir}/xfce4/panel/plugins/libxfce4battery.so
%{_desktopdir}/xfce4-power-manager-settings.desktop
%{_datadir}/xfce4/panel-plugins/xfce4-battery-plugin.desktop
%{_iconsdir}/hicolor/*/*/*
%{_datadir}/polkit-1/actions/org.xfce.power.policy
%{_datadir}/appdata/xfce4-power-manager.appdata.xml
%{_mandir}/man1/xfce4-power-manager*.1*
