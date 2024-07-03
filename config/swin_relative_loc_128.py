_base_ = [
        '../model/swin_relative_loc_128.py',
        '../data/relative_loc128.py',
        '../schedule/sgd_ssl.py',
        '../runtime/default.py'
        ]

load_from = None
resume = False
