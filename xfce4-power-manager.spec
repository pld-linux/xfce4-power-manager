Summary:	Power manager for the Xfce desktop environment
Summary(pl.UTF-8):	Zarządca energii dla środowiska Xfce
Name:		xfce4-power-manager
Version:	1.2.0
Release:	2
License:	GPL v2
Group:		X11/Applications
Source0:	http://archive.xfce.org/src/apps/xfce4-power-manager/1.2/%{name}-%{version}.tar.bz2
# Source0-md5:	935599b7114b0a4b0e2c9a5d6c72524c
Patch100:	0049-Autotools-updates.patch
Patch101:	0061-Remove-custom-OSD-brightness-popup-use-libnotify-ins.patch
Patch102:	0073-Ignore-useless-deprecation-warnings-for-now.patch
Patch103:	0074-Don-t-init-thread-on-gobject-3.32.patch
Patch104:	0075-Change-brightness-level-from-glong-to-gint32.patch
Patch105:	0079-Fix-Typo-in-xfpm-power.c.patch
Patch106:	0080-Fix-typo-in-error-message.patch
Patch107:	0081-Fix-typo.patch
Patch108:	0082-Fix-incorrect-check-for-suspend-permissions-bug-8438.patch
Patch109:	0145-Add-shutdown-reboot-functionality-for-systemd-Bug-10.patch
Patch110:	0146-Fix-empty-systray-icon-in-some-panels-on-battery-rem.patch
Patch111:	0147-Display-power-percentage.patch
Patch112:	0148-Fix-status-icon-for-devices-other-than-battery-and-u.patch
Patch113:	0149-Update-to-XFCE_PANEL_PLUGIN_REGISTER.patch
Patch114:	0150-Add-support-for-keyboard-backlight-control-Bug-10470.patch
Patch115:	0151-Don-t-allow-systemd-to-handle-suspend-hibernate-even.patch
Patch116:	0152-xfpm-power-info-add-current-percentage-of-batteries.patch
Patch117:	0153-xfpm-battery-do-not-show-an-icon-for-HID-devices.patch
Patch118:	0154-Update-xfce4-session-lock-screen-setting.patch
Patch119:	0155-Use-the-online-docs-for-help.patch
Patch120:	0156-Add-xfpm-backlight.c-to-potfiles.patch
Patch121:	0157-Remove-the-doc-configure-deps.patch
Patch122:	0171-Add-support-for-logind-suspend-resume-Bug-9963.patch
Patch123:	0172-Update-min-requirements-and-autotools.patch
Patch124:	0175-port-xfpm-to-libupower-glib-add-support-for-upower-0.patch
Patch125:	0176-get-rid-of-XfpmDeviceState-and-XfpmDeviceType.patch
Patch126:	0177-xfpm_backlight_button_pressed_cb-fix-popup-display.patch
Patch127:	0178-Fix-potential-uninitialized-variable.patch
Patch128:	0200-Add-a-option-for-network-manager-sleep-Bug-10702.patch
Patch129:	0201-Fix-for-enable-deprecared-and-gseal.patch
Patch130:	0202-Uninitialized-variable-start_time.patch
Patch131:	0203-Fix-uninitialized-pointer-read.patch
Patch132:	0206-Warn-when-no-lock-tool-succeeded-Bug-6413.patch
Patch133:	xfpm-enum-types.patch
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
BuildRequires:	xfce4-dev-tools >= 4.10.0
BuildRequires:	xfce4-panel-devel >= 4.10.0
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
%patch100 -p1
%patch101 -p1
%patch102 -p1
%patch103 -p1
%patch104 -p1
%patch105 -p1
%patch106 -p1
%patch107 -p1
%patch108 -p1
%patch109 -p1
%patch110 -p1
%patch111 -p1
%patch112 -p1
%patch113 -p1
%patch114 -p1
%patch115 -p1
%patch116 -p1
%patch117 -p1
%patch118 -p1
%patch119 -p1
%patch120 -p1
%patch121 -p1
%patch122 -p1
%patch123 -p1
%patch124 -p1
%patch125 -p1
%patch126 -p1
%patch127 -p1
%patch128 -p1
%patch129 -p1
%patch130 -p1
%patch131 -p1
%patch132 -p1
%patch133 -p1

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
%attr(755,root,root) %{_sbindir}/xfpm-power-backlight-helper
%attr(755,root,root) %{_libdir}/xfce4/panel/plugins/libxfce4brightness.so
%{_desktopdir}/xfce4-power-manager-settings.desktop
%{_datadir}/xfce4/panel-plugins/xfce4-brightness-plugin.desktop
%{_iconsdir}/hicolor/*/*/*
%{_datadir}/polkit-1/actions/org.xfce.power.policy
%{_mandir}/man1/xfce4-power-manager*.1*
