Name:		fermilab-conf_login-screen-no-user-list
Version:	1.0
Release:	4%{?dist}
Summary:	Disable the login screen user list
Group:		Fermilab
License:	GPL
URL:		https://github.com/fermilab-context-rpms/fermilab-conf_login-screen-no-user-list
BuildArch:	noarch

Source0:	fermilab-conf_login-screen-no-user-list.tar.xz

BuildRequires:	bash coreutils
Requires:	system-release

# Top level package should require software specific packages
Requires:	%{name}-gdm == %{version}-%{release}


%description
By default the login-screen displays a list of all users with a
valid login shell and userspace UID in a nice graphical menu.

This list of users should be disabled.

Per: CS-Doc-1065


%package gdm
Summary:        Disable the GDM user list
Obsoletes:	zz_gdm_no_user_list
Obsoletes:	SL_gdm_no_user_list
Conflicts:	gdm < 3.8

Requires(post):	dconf
Requires(postun):	dconf

%description gdm
By default the GDM login-screen displays a list of all users with a
valid login shell and userspace UID in a nice graphical menu.

This list of users should be disabled.

Per: CS-Doc-1065


%prep
%setup -q -n conf


%build


%install

# for GDM
%{__install} -Dpm 644 dconf/20-no-user-list %{buildroot}/%{_sysconfdir}/dconf/db/distro.d/20-no-user-list
%{__install} -Dpm 644 dconf/locks/20-no-user-list %{buildroot}/%{_sysconfdir}/dconf/db/distro.d/locks/20-no-user-list

# for KDM
# ???

# for LXDE
# ???

%post gdm -p /bin/bash
dconf update
%postun gdm -p /bin/bash
dconf update


%files
%defattr(0644,root,root,0755)

%files gdm
%defattr(0644,root,root,0755)
%config %{_sysconfdir}/dconf/db/distro.d/20-no-user-list
%config %{_sysconfdir}/dconf/db/distro.d/locks/20-no-user-list

%changelog
* Tue Feb 22 2022 Pat Riehecky <riehecky@fnal.gov> - 1.0-4
- Use unified dconf options for EL7+

* Fri Dec 3 2021 Pat Riehecky <riehecky@fnal.gov> - 1.0-3.1
- Prep for EL9

* Tue Oct 06 2015 Bonnie King <bonniek@fnal.gov> - 1.0-3.sl7
- Use upstream prefered behavior for distribution customizations ENHC0001984

* Mon Aug 4 2014 Pat Riehecky <riehecky@fnal.gov> 1.0-2.sl7
- Removed GDM requirement to allow for deployment on no GUI nodes for SLF

* Tue Jul 29 2014 Pat Riehecky <riehecky@fnal.gov> 1.0-1.sl7
- Initial build
