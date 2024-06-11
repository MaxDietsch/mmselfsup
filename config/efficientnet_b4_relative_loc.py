_base_ = [
        '../../model/efficientnet_b4_relative_loc.py',
        '../../data/relative_loc8.py',
        '../../schedule/sgd_ssl.py',
        '../../runtime/default.py'
        ]

load_from = None
resume = False
