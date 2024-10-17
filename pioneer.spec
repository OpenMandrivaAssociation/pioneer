%define		oversion	alpha30

Name:		pioneer
Version:	0.0.%{oversion}
Release:	2
Summary:	Space adventure game, reminiscent of Frontier: Elite 2
Group:		Games/Arcade
License:	GPLv3+
URL:		https://pioneerspacesim.net/
# See https://github.com/pioneerspacesim/pioneer/tags
Source:		%{name}-%{oversion}.tar.gz
BuildRequires:	imagemagick
BuildRequires:	pkgconfig(assimp) >= 3.0
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glew)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(SDL_image)
BuildRequires:	pkgconfig(sigc++-2.0)
BuildRequires:	pkgconfig(vorbisfile)
Requires:	%{name}-data = %{version}

%description
Pioneer is a space adventure game set in the Milky Way galaxy at the turn of
the 31st Century.

The game is open-ended, and you are free to explore the millions of star
systems in the game. You can land on planets, slingshot past gas giants, and
burn yourself to a crisp flying between binary star systems.

When Pioneer is finished there will be many ways to make ends meet: piracy,
smuggling, bounty-hunting, mining, doing missions for the various factions
fighting for power, freedom or self-determination.

Pioneer has a sneaking resemblance to Frontier: Elite 2.

%files
%defattr(644,root,root,755)
%doc Changelog.txt AUTHORS.txt README.txt Quickstart.txt
%attr(755,root,root) %{_gamesbindir}/%{name}
%attr(755,root,root) %{_gamesbindir}/lmrmodelviewer
%{_datadir}/applications/%{name}.desktop
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_iconsdir}/hicolor/*/apps/%{name}.png

#----------------------------------------------------------------------------

%package data
Summary:	Game data files for Pioneer
Requires:	%{name} = %{version}
BuildArch:	noarch

%description data
Game data files for Pioneer.

%files data
%defattr(644,root,root,755)
%{_gamesdatadir}/%{name}

#----------------------------------------------------------------------------

%prep
%setup -q -n %{name}-%{oversion}
for N in 16 32 64 128; do convert data/icons/badge.png -resize ${N}x${N} $N.png; done

%build
./bootstrap
%configure2_5x \
	--bindir=%{_gamesbindir} \
	PIONEER_DATA_DIR=%{_gamesdatadir}/%{name}

%make

%install
%makeinstall_std

install -D 16.png %{buildroot}%{_miconsdir}/%{name}.png
install -D 32.png %{buildroot}%{_liconsdir}/%{name}.png
install -D 64.png %{buildroot}%{_iconsdir}/hicolor/64x64/apps/%{name}.png
install -D 128.png %{buildroot}%{_iconsdir}/hicolor/128x128/apps/%{name}.png

# menu-entry
mkdir -p  %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=Pioneer
Comment=Space adventure game
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Game;ArcadeGame;
EOF


