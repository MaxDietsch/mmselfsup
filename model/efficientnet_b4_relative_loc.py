model = dict(
    type='RelativeLoc',
    data_preprocessor=dict(
        type='mmselfsup.RelativeLocDataPreprocessor',
        mean=[151.14, 102.69, 97.74],
        std=[70.03, 55.91, 54.73],
        bgr_to_rgb=True),
    backbone=dict(type='EfficientNet', arch='b4'),
    neck=dict(
        type='RelativeLocNeck',
        in_channels=1792,
        out_channels=3584,
        with_avg_pool=True),
    head=dict(
        type='ClsHead',
        loss=dict(type='mmpretrain.CrossEntropyLoss'),
        with_avg_pool=False,
        in_channels=3584,
        num_classes=8,
        init_cfg=[
            dict(type='Normal', std=0.005, layer='Linear'),
            dict(type='Constant', val=1, layer=['_BatchNorm', 'GroupNorm'])
        ]))
