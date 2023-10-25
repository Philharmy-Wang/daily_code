
# 基础配置文件路径
_base_ = r'C:\Users\12715\Documents\GitHub\mmdetection\configs\solo\solo_r50_fpn_8gpu_1x_coco.py'

# 自定义钩子
# custom_hooks = [
#     dict(type='WandbLoggerHook', init_args=dict(project='mmdetection', name='faster-rcnn-fire'), interval=1)
# ]

# 数据集设置
classes = ('fire', 'smoke')
num_classes = len(classes)

# 模型设置
model = dict(
    roi_head=dict(
        bbox_head=dict(
            num_classes=num_classes  # 更新类别数量
        )
    )
)

# 数据配置
data = dict(
    train=dict(
        img_prefix='data/coco/train2017',  # 更新图像前缀
        classes=classes,  # 更新类别
        ann_file='data/coco/annotations/instances_train2017.json'  # 更新注释文件路径
    ),
    val=dict(
        img_prefix='data/coco/val2017',  # 更新图像前缀
        classes=classes,  # 更新类别
        ann_file='data/coco/annotations/instances_val2017.json'  # 更新注释文件路径
    ),
    test=dict(
        img_prefix='data/coco/val2017',  # 更新图像前缀
        classes=classes,  # 更新类别
        ann_file='data/coco/annotations/instances_val2017.json'  # 更新注释文件路径
    )
)

# 优化器设置
optimizer = dict(type='SGD', lr=0.00261, momentum=0.9, weight_decay=0.0005)
optimizer_config = dict(grad_clip=None)

# 学习率策略
lr_config = dict(
    policy='step',
    warmup='linear',
    warmup_iters=2000,
    warmup_ratio=0.1,
    step=[218, 246]
)
total_epochs = 20

# 日志和检查点设置
checkpoint_config = dict(interval=1)
log_config = dict(
    interval=50,
    hooks=[
        dict(type='TextLoggerHook'),
        # dict(type='TensorboardLoggerHook')
    ]
)

# 运行时设置
evaluation = dict(interval=1, metric='bbox')
work_dir = './work_dirs/solo_custom'
load_from = None
resume_from = None
workflow = [('train', 1)]
