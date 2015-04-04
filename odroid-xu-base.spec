Name:           odroid-xu-base
Version:        0.1.0
Release:        1%{?dist}
Summary:        Basic system configurations for ODROID-XU

Group:          System Environment/Base
License:        BSD
URL:            http://odroid.com/dokuwiki/doku.php?id=en:odroid-xu
Source0:        firmware.sh
Source1:        50-firmware.rules
Source2:        60-persistent-v4l.rules
Source3:        60-persistent-v4l.conf

BuildArch:      noarch

Requires:       udev
Requires:       dracut
Requires:       linux-firmware

%description
Basic system configurations for ODROID-XU, such as firmware scripts and rules
for udev.

%prep

%build

%install
install -p -m0755 -D %{SOURCE0} %{buildroot}%{_prefix}/lib/udev/firmware.sh
install -p -m0644 -D %{SOURCE1} %{buildroot}%{_prefix}/lib/udev/rules.d/50-firmware.rules
install -p -m0644 -D %{SOURCE2} %{buildroot}%{_sysconfdir}/udev/rules.d/60-persistent-v4l.rules
install -p -m0644 -D %{SOURCE3} %{buildroot}%{_sysconfdir}/dracut.conf.d/60-persistent-v4l.conf

install -d %{buildroot}%{_prefix}/lib/firmware/
ln -s s5p-mfc-v6.fw %{buildroot}%{_prefix}/lib/firmware/mfc_fw.bin

%files
%{_prefix}/lib/udev/firmware.sh
%{_prefix}/lib/udev/rules.d/50-firmware.rules
%config(noreplace) %{_sysconfdir}/udev/rules.d/60-persistent-v4l.rules
%config(noreplace) %{_sysconfdir}/dracut.conf.d/60-persistent-v4l.conf
%{_prefix}/lib/firmware/mfc_fw.bin

%changelog
* Sat Apr 04 2015 Scott K Logan <logans@cottsay.net> - 0.1.0-1
- Initial package
