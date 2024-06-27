# dataset settings
dataset_type = 'mmcls.CustomDataset'
data_root = '../data_dir/LD/'

train_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='RandomResizedCrop', size=640, scale=(0.2, 1.0), backend='pillow', interpolation='bicubic'),
    dict(type='PackSelfSupInputs', meta_keys=['img_path'])         
    ]

train_dataloader = dict(
    batch_size=16,
    num_workers=8,
    persistent_workers=True,
    sampler=dict(type='DefaultSampler', shuffle=True),
    collate_fn=dict(type='default_collate'),
    dataset=dict(
        type=dataset_type,
        data_root=data_root,
        ann_file='meta/train.txt',
        data_prefix=dict(img_path='train/'),
        pipeline=train_pipeline)
    )
