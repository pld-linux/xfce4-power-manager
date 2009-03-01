Summary:	Power manager for the Xfce desktop environment
Summary(pl.UTF-8):	Zarządca energii dla środowiska Xfce
Name:		xfce4-power-manager
Version:	0.6.2
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://goodies.xfce.org/releases/xfce4-power-manager/%{name}-%{version}.tar.bz2
# Source0-md5:	923d4dba39b1f313631b636e7b5d772d
URL:		http://goodies.xfce.org/projects/applications/xfce4-power-manager
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.8
BuildRequires:	dbus-glib-devel >= 0.74
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.14.0
BuildRequires:	gtk+2-devel >= 2:2.10.6
BuildRequires:	hal-devel >= 0.5.6
BuildRequires:	intltool
BuildRequires:	libnotify-devel
BuildRequires:	libxfcegui4-devel >= 4.6.0
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	xfce4-dev-tools >= 4.6.0
BuildRequires:	xfconf-devel >= 4.6.0
Requires(post,postun):	gtk+2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Power manager for the Xfce desktop environment.

%description -l pl.UTF-8
Zarządca energii dla środowiska Xfce.

%prep
%setup -q

%build
%{__intltoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_datadir}/locale/pt{_PT,}

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
%attr(755,root,root) %{_bindir}/xfce4-power-manager
%{_desktopdir}/xfce4-power-manager.desktop
%{_iconsdir}/hicolor/*/*/*
%{_datadir}/xfce4/doc/C/*
