Summary:	GNOME DB frontend
Name:		mergeant
Version:	0.67
Release:	%mkrel 5
License:	GPLv2+
Group:		Databases
URL:		http://www.gnome-db.org/
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
Source1:	%{name}-icons.tar.bz2
Patch:		mergeant-0.67-format-strings.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	scrollkeeper
Buildrequires:	gnome-db2.0-devel
BuildRequires:	libgnomeprintui2-2-devel
BuildRequires:	libglade2.0-devel
BuildRequires:	gnome-common
BuildRequires:	intltool
BuildRequires:	gtk-doc
Requires:	scrollkeeper
Requires:	gnome-db2.0

%description
Mergeant is a program which helps administer a DBMS database using the gnome-db
framework. Basically, it memorizes all the structure of the database, and some
queries, and does the SQL queries instead of the user (not having to type all
over again those SQL commands, although it is still possible to do so).

%prep
%setup -q -n %{name}-%{version} -a1
%patch -p1

%build

%configure2_5x --disable-update-mimedb
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang %{name} --with-gnome

%if %mdkversion < 200900
%post
%update_scrollkeeper
%{update_menus}
%update_mime_database
%{update_icon_cache hicolor}
%endif

%if %mdkversion < 200900
%postun
%clean_scrollkeeper
%{clean_menus}
%clean_mime_database
%{clean_icon_cache hicolor}
%endif

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc README ChangeLog AUTHORS BUGS TODO 
%{_bindir}/*
%{_libdir}/bonobo/servers/*
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%{_datadir}/omf/*
%{_datadir}/mime/*/*.xml
%{_iconsdir}/hicolor/*/*/*

