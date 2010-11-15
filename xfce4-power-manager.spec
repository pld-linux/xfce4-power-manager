Summary:	Power manager for the Xfce desktop environment
Summary(pl.UTF-8):	Zarządca energii dla środowiska Xfce
Name:		xfce4-power-manager
Version:	1.0.1
Release:	0.1
License:	GPL v2
Group:		X11/Applications
Source0:	http://archive.xfce.org/src/apps/xfce4-power-manager/1.0/%{name}-%{version}.tar.bz2
# Source0-md5:	683558affa77beefb14855c110c6bd28
Patch0:		%{name}-ac-am.patch
URL:		http://goodies.xfce.org/projects/applications/xfce4-power-manager
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.8
BuildRequires:	dbus-glib-devel >= 0.74
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.14.0
BuildRequires:	gtk+2-devel >= 2:2.10.6
BuildRequires:	intltool
BuildRequires:	libnotify-devel
BuildRequires:	libtool
BuildRequires:	libxfce4ui-devel >= 4.7.0
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	xfce4-dev-tools >= 4.7.0
BuildRequires:	xfconf-devel >= 4.7.0
Requires(post,postun):	gtk+2
Requires:	xfce4-dirs >= 4.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Power manager for the Xfce desktop environment.

%description -l pl.UTF-8
Zarządca energii dla środowiska Xfce.

%prep
%setup -q
%patch0 -p1

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-hal

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -r $RPM_BUILD_ROOT%{_datadir}/locale/ur_PK

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
%attr(755,root,root) %{_bindir}/xfce4-power-information
%attr(755,root,root) %{_bindir}/xfce4-power-manager
%attr(755,root,root) %{_bindir}/xfce4-power-manager-settings
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/xfce4-brightness-plugin
%{_desktopdir}/xfce4-power-manager-settings.desktop
%{_datadir}/xfce4/panel-plugins/xfce4-brightness-plugin.desktop
%{_iconsdir}/hicolor/*/*/*
%{_datadir}/xfce4/doc/C/*.html
%{_datadir}/xfce4/doc/C/images/*.png
%{_mandir}/man1/xfce4-power-manager*.1*
