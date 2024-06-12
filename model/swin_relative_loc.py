model = dict(
    type='RelativeLoc',
    data_preprocessor=dict(
        type='RelativeLocDataPreprocessor',
        mean=[130.36, 84.27, 72.21],
        std=[80.45, 62.92, 57.33],
        bgr_to_rgb=True),
    backbone=dict(
        type='mmpretrain.SwinTransformer',
        arch='small',
        img_size=640,
        ),
    neck=dict(
        type='RelativeLocNeck',
        in_channels=768,
        out_channels=1536,
        with_avg_pool=True),
    head=dict(
        type='ClsHead',
        loss=dict(type='mmpretrain.CrossEntropyLoss'),
        with_avg_pool=False,
        in_channels=1536,
        num_classes=8,
        init_cfg=[
            dict(type='Normal', std=0.005, layer='Linear'),
            dict(type='Constant', val=1, layer=['_BatchNorm', 'GroupNorm'])
        ]))
