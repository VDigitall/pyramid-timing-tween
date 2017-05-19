# Introduction

Timing tween for measure request process time.

### Installation

```shell
pip install timingtween
```

or

```shell
git clone https://VDigitall@gitlab.quintagroup.com/VDigitall/pyramid-timing-tween.git
cd timingtween
pip install .
```

### How to use

In application settings add options `do_timing = true`

```python
from pyramid.config import Configurator
from timingtween.timingtween.tween import includeme as include_tween
config = Configurator()
include_tween(config)
```
