# preloadify
Create fat binaries with ease

This script is not a development of 2020, this GitHub repository could create a false impression.
It was lurking around on my computer for years, because I never thought it was quite finished,
and therefore never got around to releasing it. In truth it worked the whole time for the current
set of features, and I wanted to add some more before releasing it.

This script can be a great alternative to static compilation, or to cases where you have a
dynamically linked binary, that you'd like to port to other systems, but you aren't willing
to compile from source, or for some reason can't. To make this work preloadify uses LD_PRELOAD,
a unpacking/run script at the beginning of the created binary, tar, optional compression,
and patchelf.

Preloadify goes so far as to include the ld.so in the created binary (which is a sort of
self-contained package) in order to make absolutely sure that it will run on every Linux
system with compatible processor architecture, in example all 64bit-x86 Linux systems.
This allows for porting binaries from a full-fledged GNU/Linux to a bare-bones embedded
Linux system, that has for example BusyBox, or some uncommon libc, or no ld.so at all.

The --pack command line option allows you to pack other binaries into the same final fat binary,
the kicker here is that for those additional binaries preloadify also searches for needed
dynamic libraries and packs them into the fat binary, too. This means that the executable you
wanted to convert into a fat executable can also call those other packed executables at runtime
and they are also garantueed not to be missing any dynamic library dependencies.

Dependencies:
- docopt (pip3 install docopt)
- patchelf
- tar

The help output (preloadify --help) should be sufficient to understand how it works:
```
Usage: preloadify [options] EXECUTABLE OUTPUTFILE

Create an executable self-containing all dynamic library dependencies of the original.

Options:
  -l, --list                  Alphabetically sorted list of all dynamic libraries
                              that are included in the preloadified executable.
  -s, --size                  Lists the size of all dynamic libraries included in the
                              preloadified executable sorted by size.
  -b, --blacklist FILE        Using a blacklist you can exclude dynamic libraries
                              from being included in the preloadified executable.
                              Blacklist files have the following format:
                                  libsomelib
                                  libsomeotherlib
  -a, --addlist FILE          Include libraries and their respective dependencies
                              from a list in preloadified executable.
                              These usually are libraries that get dynamically
                              linked at runtime.
                              Addlist files have the following format:
                                  libsomelib
                                  libsomeotherlib
                                  /path/to/lib
  -c, --compression METHOD    One of gzip, bzip2 and xz.
                              By default compression is disabled.
                              Note that compression can influence portability negatively.
  -t, --tmpdir TMPDIR         Set a different tmp directory. Default is /tmp.
  -r, --run                   Run preloadified executable as soon as it is created.
                              (For testing purposes)
  --chrootify                 With this option the wrapper creates a chroot environment
                              for the executable emulating the system without its libraries.
                              This can be useful to test whether all library dependencies
                              have been taken care of through preloadifying.
  --pack EXECUTABLES          List of additional executables that should be part of the
                              preloadified executable separated by comma.
                              i.e. --pack bash,/path/to/program
                              Note that only the main executable will be executed
                              when executing the generated outputfile.
  -h, --help                  Show this help message and exit
  -v, --version               Display version information
```
