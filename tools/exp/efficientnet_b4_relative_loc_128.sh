#!/bin/bash

cd ..

python train.py ../config/efficientnet_b4_relative_loc_128.py --work-dir ../../mmpretrain/work_dirs/phase4/efficientnet_b4/ssl_relative_loc_128/lr_decr/
