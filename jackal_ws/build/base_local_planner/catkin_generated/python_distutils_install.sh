#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/ahnaf/BARN/jackal_ws/src/base_local_planner"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/ahnaf/BARN/jackal_ws/install/lib/python3/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/ahnaf/BARN/jackal_ws/install/lib/python3/dist-packages:/home/ahnaf/BARN/jackal_ws/build/lib/python3/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/ahnaf/BARN/jackal_ws/build" \
    "/home/ahnaf/BARN/nav_challenge/bin/python3" \
    "/home/ahnaf/BARN/jackal_ws/src/base_local_planner/setup.py" \
    egg_info --egg-base /home/ahnaf/BARN/jackal_ws/build/base_local_planner \
    build --build-base "/home/ahnaf/BARN/jackal_ws/build/base_local_planner" \
    install \
    --root="${DESTDIR-/}" \
    --install-layout=deb --prefix="/home/ahnaf/BARN/jackal_ws/install" --install-scripts="/home/ahnaf/BARN/jackal_ws/install/bin"
