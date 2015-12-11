Name:           ros-indigo-rosh
Version:        1.0.9
Release:        1%{?dist}
Summary:        ROS rosh package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/rosh
Source0:        %{name}-%{version}.tar.gz

Requires:       python-ipython
Requires:       ros-indigo-rosgraph
Requires:       ros-indigo-roshlaunch
Requires:       ros-indigo-rosmsg
Requires:       ros-indigo-rosnode
Requires:       ros-indigo-rosparam
Requires:       ros-indigo-rospy
Requires:       ros-indigo-rosservice
Requires:       ros-indigo-rostopic
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-rospy
BuildRequires:  ros-indigo-rosunit

%description
rosh is a Python-based scripting and runtime environment for ROS. Through rosh
and its various plugins, you can interact with ROS APIs in an introspectable and
unified approach.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Fri Dec 11 2015 Dan Lazewatsky <dan@lazewatsky.com> - 1.0.9-1
- Autogenerated by Bloom

* Thu Apr 16 2015 Dan Lazewatsky <dan@lazewatsky.com> - 1.0.9-0
- Autogenerated by Bloom

* Sun Aug 17 2014 Dan Lazewatsky <dan@lazewatsky.com> - 1.0.7-0
- Autogenerated by Bloom

* Fri Jul 25 2014 Dan Lazewatsky <dan@lazewatsky.com> - 1.0.6-0
- Autogenerated by Bloom

