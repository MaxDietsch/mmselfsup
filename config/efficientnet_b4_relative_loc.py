_base_ = [
        '../model/efficientnet_b4_relative_loc.py',
        '../data/relative_loc8.py',
        '../schedule/sgd_ssl.py',
        '../runtime/default.py'
        ]

load_from = '../../mmpretrain/work_dirs/phase4/efficientnet_b4/ssl_relative_loc/lr_decr/epoch_166.pth'
resume = True
