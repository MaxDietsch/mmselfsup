_base_ = [
        '../model/efficientnet_b4_relative_loc_128.py',
        '../data/relative_loc128.py',
        '../schedule/sgd_ssl.py',
        '../runtime/default.py'
        ]

load_from = None
resume = False
