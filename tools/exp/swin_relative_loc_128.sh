#!/bin/bash

cd ..

python train.py ../config/swin_relative_loc_128.py --work-dir ../../mmpretrain/work_dirs/phase4/swin/ssl_relative_loc_128/lr_decr/
