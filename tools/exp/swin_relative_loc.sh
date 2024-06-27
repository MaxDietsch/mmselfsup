#!/bin/bash

cd ..

python train.py ../config/swin_relative_loc.py --work-dir ../../mmpretrain/work_dirs/phase4/swin/ssl_relative_loc/lr_decr/
