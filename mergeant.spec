Summary: GNOME DB frontend
Name: mergeant
Version: 0.67
Release: %mkrel 1
License: GPL
Group: Databases
URL: http://www.gnome-db.org/
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
Source1: %name-icons.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: scrollkeeper
Buildrequires: gnome-db2.0-devel
BuildRequires: libgnomeprintui2-2-devel
BuildRequires: libglade2.0-devel
BuildRequires: automake
BuildRequires: gnome-common
BuildRequires: intltool
BuildRequires: gtk-doc
Requires: scrollkeeper
Requires: gnome-db2.0

%description
Mergeant is a program which helps administer a DBMS database using the gnome-db
framework. Basically, it memorizes all the structure of the database, and some
queries, and does the SQL queries instead of the user (not having to type all
over again those SQL commands, although it is still possible to do so).

%prep
%setup -q -n %{name}-%{version} -a1

%build

%configure2_5x --disable-update-mimedb
%make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall_std

%find_lang %{name} --with-gnome

%__install -D -m 644 %{name}48.png %buildroot/%_liconsdir/%name.png
%__install -D -m 644 %{name}32.png %buildroot/%_iconsdir/%name.png
%__install -D -m 644 %{name}16.png %buildroot/%_miconsdir/%name.png

%post
%update_scrollkeeper
%{update_menus}
%update_mime_database
%{update_icon_cache hicolor}

%postun
%clean_scrollkeeper
%{clean_menus}
%clean_mime_database
%{clean_icon_cache hicolor}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc README ChangeLog AUTHORS BUGS TODO 
%{_bindir}/*
%{_libdir}/bonobo/servers/*
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%{_datadir}/omf/*
%{_datadir}/mime/*/*.xml
%{_iconsdir}/*/%name.png
%{_iconsdir}/hicolor/*/*/*
%{_iconsdir}/%name.png
