Random User Agents
==================

[![Build Status](https://travis-ci.org/drinorselmanaj/random_useragent.svg?branch=master)](https://travis-ci.org/drinorselmanaj/random_useragent)

Random User Agents is a python library that provides an easy way to generate random user-agent strings.

Installation
------------

You can install random_useragent by running the following command:

    pip install random_useragent

Or you can download direct from ``Github``\ \_ and install it manually.

Usage
-----

To randomly select an aspect ratio you can use ``.get_aspect_ratio_list()``, to generate screen resolution ``.random_resolution()`` and ``.random_agent()`` for random user-agent strings.
For example:

```python

    from random_useragent.random_useragent import Randomize

    # Get aspect ratio list.
    r_agent = Randomize()
    r_agent.get_aspect_ratio_list() # returns ['3:2', '4:3', '5:3', '5:4', '16:9', '16:10'].

    # Takes 2 arguments (self, aspect_ratio).
    r_agent.random_resolution('3:2') # returns screen resolution.

    # Takes 3 arguments (self, device_type, os)
    r_agent.random_agent('desktop','linux') # returns 'Desktop / Linux'
    r_agent.random_agent('desktop','mac') # returns 'Desktop / Linux'
    r_agent.random_agent('desktop','windows') # returns 'Desktop / Macintosh'

    r_agent.random_agent('tablet','android') # returns 'Tablet / Android'
    r_agent.random_agent('tablet','ios') # returns 'Tablet / iOS'

    r_agent.random_agent('smartphone','android') # returns 'Smartphone / Android'
    r_agent.random_agent('smartphone','ios') # returns 'Smartphone / iOS'
```

License
-------
The MIT License (MIT). Please see [License File](LICENSE.md) for more information.
