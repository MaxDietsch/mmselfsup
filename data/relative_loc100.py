# dataset settings
dataset_type = 'mmpretrain.CustomDataset'
data_root = '../../SSL-HK'

train_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='Resize', scale=(128, 128)),
    dict(type='RandomGrayscale', prob=0.66, keep_channels=True),
    dict(type='RandomPatchWithLabels'),
    dict(
        type='PackSelfSupInputs',
        pseudo_label_keys=['patch_box', 'patch_label', 'unpatched_img'],
        meta_keys=['img_path'])
]

train_dataloader = dict(
    batch_size=100,
    num_workers=4,
    persistent_workers=True,
    sampler=dict(type='DefaultSampler', shuffle=True),
    collate_fn=dict(type='default_collate'),
    dataset=dict(
        type=dataset_type,
        data_root=data_root,
        ann_file='meta/train.txt',
        data_prefix=dict(img_path='train/'),
        pipeline=train_pipeline))
