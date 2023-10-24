# 导入必需的库和模块
import argparse
import os
import os.path as osp
from mmengine.config import Config, DictAction
from mmengine.registry import RUNNERS
from mmengine.runner import Runner
from mmdet.utils import setup_cache_size_limit_of_dynamo

# 定义一个函数来解析命令行参数
def parse_args():
    parser = argparse.ArgumentParser(description='Train a detector')  # 创建一个解析器对象
    parser.add_argument('config', help='train config file path')  # 添加一个参数来接受训练配置文件的路径
    parser.add_argument('--work-dir', help='the dir to save logs and models')  # 添加一个参数来指定保存日志和模型的目录
    parser.add_argument('--amp', action='store_true', default=False, help='enable automatic-mixed-precision training')  # 添加一个开关来启用自动混合精度训练
    parser.add_argument('--auto-scale-lr', action='store_true', help='enable automatically scaling LR.')  # 添加一个开关来启用自动缩放学习率
    parser.add_argument('--resume', nargs='?', type=str, const='auto', help='resume from a specific checkpoint')  # 添加一个参数来指定从哪个检查点恢复，或自动从工作目录的最新检查点恢复
    parser.add_argument('--cfg-options', nargs='+', action=DictAction, help='override some settings in the used config')  # 添加一个参数来覆盖配置文件中的某些设置
    parser.add_argument('--launcher', choices=['none', 'pytorch', 'slurm', 'mpi'], default='none', help='job launcher')  # 添加一个参数来指定作业启动器
    parser.add_argument('--local_rank', '--local-rank', type=int, default=0)  # 添加一个参数来指定本地排名，通常用于分布式训练
    args = parser.parse_args()  # 解析命令行参数
    if 'LOCAL_RANK' not in os.environ:  # 检查是否已经设置了环境变量 'LOCAL_RANK'
        os.environ['LOCAL_RANK'] = str(args.local_rank)  # 如果没有，设置它
    return args  # 返回解析得到的参数对象

# 定义主函数
def main():
    args = parse_args()  # 调用上面定义的函数来解析命令行参数
    setup_cache_size_limit_of_dynamo()  # 设置缓存大小限制，以减少重复编译并提高训练速度
    cfg = Config.fromfile(args.config)  # 从指定的文件加载配置
    cfg.launcher = args.launcher  # 设置启动器类型
    if args.cfg_options is not None:  # 如果通过命令行提供了额外的配置选项
        cfg.merge_from_dict(args.cfg_options)  # 合并这些额外的配置选项到当前配置中
    # 设置工作目录
    if args.work_dir is not None:  # 如果通过命令行指定了工作目录
        cfg.work_dir = args.work_dir  # 使用命令行指定的工作目录
    elif cfg.get('work_dir', None) is None:  # 如果配置文件中没有指定工作目录
        cfg.work_dir = osp.join('./work_dirs', osp.splitext(osp.basename(args.config))[0])  # 使用配置文件名作为默认的工作目录
    # 启用自动混合精度训练和自动缩放学习率
    if args.amp is True:  # 如果通过命令行启用了自动混合精度训练
        cfg.optim_wrapper.type = 'AmpOptimWrapper'  # 设置优化器包装器类型
        cfg.optim_wrapper.loss_scale = 'dynamic'  # 设置损失缩放为动态
    if args.auto_scale_lr:  # 如果通过命令行启用了自动缩放学习率
        # 检查配置中是否有相应的设置
        if 'auto_scale_lr' in cfg and 'enable' in cfg.auto_scale_lr and 'base_batch_size' in cfg.auto_scale_lr:
            cfg.auto_scale_lr.enable = True  # 启用自动缩放学习率
        else:
            raise RuntimeError('Can not find "auto_scale_lr" or "auto_scale_lr.enable" or "auto_scale_lr.base_batch_size" in your configuration file.')
    # 设置恢复训练的配置
    if args.resume == 'auto':  # 如果通过命令行指定了自动恢复
        cfg.resume = True  # 设置恢复标志为True
        cfg.load_from = None  # 不从特定的检查点加载模型
    elif args.resume is not None:  # 如果通过命令行指定了从哪个检查点恢复
        cfg.resume = True  # 设置恢复标志为True
        cfg.load_from = args.resume  # 设置从哪个检查点加载模型
    # 构建运行器并开始训练
    if 'runner_type' not in cfg:  # 如果配置中没有指定运行器类型
        runner = Runner.from_cfg(cfg)  # 从配置构建默认的运行器
    else:
        runner = RUNNERS.build(cfg)  # 从注册表构建自定义的运行器
    runner.train()  # 开始训练

# 如果这个脚本是直接运行的，而不是被导入的，就调用上面定义的主函数
if __name__ == '__main__':
    main()
