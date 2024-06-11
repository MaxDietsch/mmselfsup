optim_wrapper = dict(
    optimizer=dict(type='SGD', lr=0.01, momentum=0.9, weight_decay=0.0001))

param_scheduler = dict(
    type='MultiStepLR', by_epoch=True, milestones=[60, 120, 180], gamma=0.5)

train_cfg = dict(by_epoch=True, max_epochs=200, val_interval=1)
