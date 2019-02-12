Name:           pulseeffects
Version:        4.5.0
Release:        1%{?dist}
Summary:        Audio equalizer, filters and effects for Pulseaudio applications

License:        GPLv3+
Url:            https://github.com/wwmm/pulseeffects
Source0:        %url/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  boost-devel
BuildRequires:  desktop-file-utils
BuildRequires:  itstool
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  meson
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtkmm-3.0)
BuildRequires:  pkgconfig(glibmm-2.4) >= 2.56
BuildRequires:  pkgconfig(gstreamer-1.0) >= 1.12
BuildRequires:  pkgconfig(gstreamer-plugins-bad-1.0) >= 1.12
BuildRequires:  pkgconfig(libbs2b)
BuildRequires:  pkgconfig(libebur128)
BuildRequires:  pkgconfig(libpulse) >= 11.0
BuildRequires:  pkgconfig(lilv-0)
BuildRequires:  pkgconfig(samplerate)
BuildRequires:  pkgconfig(sigc++-2.0)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  zita-convolver-devel >= 3.1.0

Requires:       hicolor-icon-theme
Requires:       gstreamer1-plugins-good >= 1.12
#Requires:       ladspa-swh-plugins >= 0.4
Requires:       lv2-calf-plugins >= 0.90.0

Recommends:     zam-plugins
Recommends:     lv2-zam-plugins
Recommends:     ladspa-zam-plugins
Recommends:     mda-lv2
Recommends:     rubberband


%description
Limiters, compressor, reverberation, high-pass filter, low pass filter,
equalizer many more effects for PulseAudio applications.

%prep
%autosetup

%build
export LC_ALL="${LC_ALL:-UTF-8}"
%meson
%meson_build

%install
%meson_install

desktop-file-install %{buildroot}%{_datadir}/applications/com.github.wwmm.%{name}.desktop \
--dir=%{buildroot}%{_datadir}/applications

%find_lang %{name}

%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/com.github.wwmm.%{name}.appdata.xml

%files -f %{name}.lang
%doc README.md
%license LICENSE.md
%{_bindir}/%{name}
%{_datadir}/applications/*
%{_datadir}/glib-2.0/schemas/*
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/metainfo/com.github.wwmm.%{name}.appdata.xml
%{_datadir}/help/C/%{name}/*
%{_datadir}/help/pt_BR/%{name}/*
%{_datadir}/help/ru/%{name}/*
%{_datadir}/dbus-1/services/com.github.wwmm.%{name}.service
%{_libdir}/gstreamer-1.0/libgst*.so


%changelog
* Tue Feb 12 2019 Vasiliy N. Glazov <vascom2@gmail.com>  - 4.5.0-1
- Initial release for Fedora
