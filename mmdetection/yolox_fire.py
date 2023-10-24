# custom_imports = dict(imports=['mmdet.engine.hooks.wandb_logger_hook'], allow_failed_imports=False)

# 导入基本配置
_base_ = r'C:\Users\12715\Documents\GitHub\mmdetection\configs\yolox\yolox_tiny_8xb8-300e_coco.py'    #tiny
# _base_ = r'C:\Users\12715\Documents\GitHub\mmdetection\configs\yolox\yolox_nano_8xb8-300e_coco.py'  #nano


# 模型设置
model = dict(
    # 数据预处理
    data_preprocessor=dict(batch_augments=[
        dict(
            type='BatchSyncRandomResize',  # 随机尺寸调整
            random_size_range=(640, 640),  # 随机尺寸范围
            size_divisor=32,  # 尺寸除数
            interval=10)  # 间隔
    ]),
    # 主干网络配置
    backbone=dict(deepen_factor=0.33, widen_factor=0.375),
    # 网络结构配置
    neck=dict(in_channels=[96, 192, 384], out_channels=96),
    # 框头配置
    bbox_head=dict(
        in_channels=96,
        feat_channels=96,
        num_classes=2,  # 类别数
    )
)

# 数据集设置
classes = 'fire', 'smoke',  # 类别

# 图像尺寸
img_scale = (640, 640)  # 宽度、高度

# 创建 metainfo 变量
METAINFO = dict(classes=('fire', 'smoke',))  # 根据你的数据集类别来设定

# 训练管道
train_pipeline = [
    dict(type='Mosaic', img_scale=img_scale, pad_val=114.0),  # Mosaic 数据增强
    dict(
        type='RandomAffine',  # 随机仿射变换
        scaling_ratio_range=(0.5, 1.5),
        border=(-img_scale[0] // 2, -img_scale[1] // 2)),
    dict(type='YOLOXHSVRandomAug'),  # YOLOX HSV 随机增强
    dict(type='RandomFlip', prob=0.5),  # 随机翻转
    dict(type='Resize', scale=img_scale, keep_ratio=True),  # 调整尺寸
    dict(
        type='Pad',  # 填充
        pad_to_square=True,
        pad_val=dict(img=(114.0, 114.0, 114.0))),
    dict(type='FilterAnnotations', min_gt_bbox_wh=(1, 1), keep_empty=False),  # 过滤注释
    dict(type='PackDetInputs')  # 打包检测输入
]

# 测试管道
test_pipeline = [
    dict(type='LoadImageFromFile', backend_args={{_base_.backend_args}}),  # 从文件加载图像
    dict(type='Resize', scale=(640, 640), keep_ratio=True),  # 调整尺寸
    dict(
        type='Pad',  # 填充
        pad_to_square=True,
        pad_val=dict(img=(114.0, 114.0, 114.0))),
    dict(type='LoadAnnotations', with_bbox=True),  # 加载注释
    dict(
        type='PackDetInputs',  # 打包检测输入
        meta_keys=('img_id', 'img_path', 'ori_shape', 'img_shape',
                   'scale_factor'))
]

# 数据配置
data = dict(
    samples_per_gpu=32,  # 每个 GPU 的样本数
    workers_per_gpu=1,  # 每个 GPU 的工作者数
    train=dict(
        type='CocoDataset',  # 数据集类型
        ann_file='data/coco/annotations/instances_train2017.json',  # 注释文件路径
        img_prefix='data/coco/images/train2017',  # 图像前缀路径
        pipeline=train_pipeline,
        classes=classes,
        METAINFO=METAINFO,  # 添加 metainfo 变量
    ),
    val=dict(
        type='CocoDataset',
        ann_file='data/coco/annotations/instances_val2017.json',
        img_prefix='data/coco/images/val2017',
        pipeline=test_pipeline,
        classes=classes,
        METAINFO=METAINFO,  # 添加 metainfo 变量
    ),
    test=dict(
        type='CocoDataset',
        ann_file='data/coco/annotations/instances_val2017.json',
        img_prefix='data/coco/images/val2017',
        pipeline=test_pipeline,
        classes=classes,
        METAINFO=METAINFO,  # 添加 metainfo 变量
    )
)

# 优化器设置
optimizer = dict(type='SGD', lr=0.00261, momentum=0.9, weight_decay=0.0005)
optimizer_config = dict(grad_clip=None)  # 梯度裁剪配置

# 学习率设置
lr_config = dict(
    policy='step',  # 策略
    warmup='linear',  # 热身
    warmup_iters=2000,  # 热身迭代数
    warmup_ratio=0.1,  # 热身比率
    step=[218, 246]  # 步长
)
total_epochs = 20  # 总周期数

# 日志和检查点设置
checkpoint_config = dict(interval=1)  # 检查点间隔
log_config = dict(
    interval=50,  # 日志间隔
    hooks=[
        dict(type='TextLoggerHook'),  # 文本日志钩子
        # dict(type='TensorboardLoggerHook')  # Tensorboard 日志钩子
    ]
)

# 运行时设置
evaluation = dict(interval=1, metric='bbox')  # 评估配置
work_dir = './work_dirs/yolox_tiny_custom'  # 工作目录
load_from = None  # 从哪里加载模型
resume_from = None  # 从哪里恢复模型
workflow = [('train', 1)]  # 工作流


load_from = r'C:\Users\12715\Documents\GitHub\mmdetection\configs\yolox\yolox_tiny_8x8_300e_coco_20211124_171234-b4047906.pth'

