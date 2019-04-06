#!/bin/bash
git clone https://github.com/zecure/shadowd_ui.git source
docker build -t zecure/shadowd_ui .
