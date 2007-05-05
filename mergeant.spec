%define name mergeant
%define version 0.66
#%define cvsversion 0.cvs20060309

Summary: GNOME DB frontend
Name: %name
Version: %version
Release: %mkrel 22License: GPL
Group: Databases
URL: http://www.gnome-db.org/
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
Source1: %name-icons.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: scrollkeeper
Buildrequires: gnome-db2.0-devel
BuildRequires: libgnomeprintui2-2-devel
BuildRequires: libgnomeui2-devel
BuildRequires: libglade2.0-devel
BuildRequires: automake1.8
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

%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall_std

%find_lang %{name} --with-gnome

# Menu entry 
mkdir -p $RPM_BUILD_ROOT/%{_menudir}
cat >$RPM_BUILD_ROOT/%{_menudir}/%{name} <<EOF
?package(%{name}): command="%{_bindir}/mergeant" icon="%name.png" needs="X11" \
section="Applications/Databases" title="Mergeant" longtitle="DBMS admin tool" \
xdg="true"
EOF

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=Mergeant
Comment=GNOME DB frontend
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=X-MandrivaLinux-MoreApplications-Databases;Database;Office;
EOF

%__install -D -m 644 %{name}48.png %buildroot/%_liconsdir/%name.png
%__install -D -m 644 %{name}32.png %buildroot/%_iconsdir/%name.png
%__install -D -m 644 %{name}16.png %buildroot/%_miconsdir/%name.png

#remove unpackaged files
rm -f $RPM_BUILD_ROOT%{_libdir}/mergeant/plugins/*.{la,a}

%post
if [ -x %{_bindir}/scrollkeeper-update ]; then %{_bindir}/scrollkeeper-update -q || true ; fi
%{update_menus}

%postun
if [ -x %{_bindir}/scrollkeeper-update ]; then %{_bindir}/scrollkeeper-update -q || true ; fi
%{clean_menus}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc README ChangeLog AUTHORS BUGS TODO 
%{_bindir}/*
%{_libdir}/bonobo/servers/*
%{_datadir}/application-registry/*
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%{_datadir}/omf/*
%{_datadir}/mime-info/*
%{_menudir}/*
%{_iconsdir}/*/%name.png
%{_iconsdir}/%name.png
