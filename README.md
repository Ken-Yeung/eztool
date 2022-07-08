# A package makes your life easier.

## Installation
```
pip install eztool
```
### For installing on Linux, run this before install
```
export INSTALL_ON_LINUX=1
```
---
## Usage
### Time now by timezone and format
```
import eztool

now = eztool.t_now(timezone = "Hongkong", time_fmt = "%d/%m/%Y %H:%M:%S")

print(now)

# output: 20/4/2004 15:20:40
```
### Timer
```
from eztool.timer import timer

T = timer()

T.start()
# output: eztool [Timer]: Start timing.

### Your Code Here

T.stop()
# output: eztool [Timer]: Consumed 0.054247083000000015 seconds.
```
