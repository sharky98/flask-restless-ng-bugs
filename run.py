#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Own modules
from project import create_app

app = create_app(config='../local.cfg')

if __name__ == '__main__':
    app.run()
