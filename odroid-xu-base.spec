Name:           odroid-xu-base
Version:        0.3.0
Release:        1%{?dist}
Summary:        Basic system configurations for ODROID-XU

Group:          System Environment/Base
License:        BSD
URL:            http://odroid.com/dokuwiki/doku.php?id=en:odroid-xu
Source0:        firmware.sh
Source1:        50-firmware.rules
Source2:        60-persistent-v4l.rules
Source3:        60-persistent-v4l.conf
Source4:        50-hk_hdmi.rules
Source5:        50-hk_hdmi.conf
Source6:        60-hk_cec.rules
Source7:        Odroid-max98090.conf
Source8:        40-smsc95xx.conf

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
install -p -m0644 -D %{SOURCE4} %{buildroot}%{_prefix}/lib/udev/rules.d/50-hk_hdmi.rules
install -p -m0644 -D %{SOURCE5} %{buildroot}%{_prefix}/lib/dracut/dracut.conf.d/50-hk_hdmi.conf
install -p -m0644 -D %{SOURCE6} %{buildroot}%{_prefix}/lib/udev/rules.d/60-hk_cec.rules
install -p -m0644 -D %{SOURCE7} %{buildroot}%{_datadir}/alsa/cards/Odroid-max98090.conf
install -p -m0644 -D %{SOURCE8} %{buildroot}%{_prefix}/lib/dracut/dracut.conf.d/40-smsc95xx.conf

install -d %{buildroot}%{_prefix}/lib/firmware/
ln -s s5p-mfc-v6.fw %{buildroot}%{_prefix}/lib/firmware/mfc_fw.bin

%files
%{_prefix}/lib/udev/firmware.sh
%{_prefix}/lib/udev/rules.d/50-firmware.rules
%config(noreplace) %{_sysconfdir}/udev/rules.d/60-persistent-v4l.rules
%config(noreplace) %{_sysconfdir}/dracut.conf.d/60-persistent-v4l.conf
%{_prefix}/lib/udev/rules.d/50-hk_hdmi.rules
%{_prefix}/lib/dracut/dracut.conf.d/50-hk_hdmi.conf
%{_prefix}/lib/udev/rules.d/60-hk_cec.rules
%{_prefix}/lib/firmware/mfc_fw.bin
%{_datadir}/alsa/cards/Odroid-max98090.conf
%{_prefix}/lib/dracut/dracut.conf.d/40-smsc95xx.conf
%dir %{_datadir}/alsa
%dir %{_datadir}/alsa/cards

%changelog
* Wed Oct 19 2016 Scott K Logan <logans@cottsay.net> - 0.3.0-1
- Add smsc95xx dracut config

* Sun Apr 05 2015 Scott K Logan <logans@cottsay.net> - 0.2.0-1
- Add hk_hdmi, hk_cec and Odroid-max98090.conf

* Sat Apr 04 2015 Scott K Logan <logans@cottsay.net> - 0.1.0-1
- Initial package
