%define		rel	4
%define		ver	0.3
%define		src	%{ver}-%{rel}
Summary:	Converter for DVD subtitles
Summary(pl):	Konwerter do napisów z DVD
Name:		subtitleripper
Version:	%{ver}_%{rel}
Release:	3
License:	GPL
Group:		Applications/Multimedia
Source0:	http://dl.sourceforge.net/subtitleripper/%{name}-%{src}.tgz
# Source0-md5:	c0bd49a88f667c68c4430ad25bbed510
Patch0:		%{name}-ppm.patch
URL:		http://subtitleripper.sourceforge.net/
BuildRequires:	netpbm-devel
Requires:	transcode
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DVD subtitle ripper based on transcode.

%description -l pl
Ripper do napisów z DVD oparty na transcode.

%prep
%setup -q -n subtitleripper
%patch0 -p0

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install pgm2txt $RPM_BUILD_ROOT%{_bindir}
install srttool $RPM_BUILD_ROOT%{_bindir}
install subtitle2pgm $RPM_BUILD_ROOT%{_bindir}
install subtitle2vobsub $RPM_BUILD_ROOT%{_bindir}
install vobsub2pgm $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README README.gocr README.srttool README.subtitle2pgm README.vobsub
%attr(755,root,root) %{_bindir}/*
