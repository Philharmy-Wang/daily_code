# 查看某个目录下所有的文件
# 赋予权限：chmod +x list_files.sh
# 执行脚本：./list_files.sh

#!/bin/bash
# 设置目标目录
target_directory="/media/a1408/新加卷1/FLAME2_dt_rgb_ir"

# 定义一个函数来处理每个目录
process_directory() {
  local directory=$1
  echo "Directory: $directory"
  
  # 获取该目录下的所有文件（不包括子目录），并限制输出前10个
  local file_count=$(find "$directory" -maxdepth 1 -type f | wc -l)  # 计算文件数量
  if [ "$file_count" -gt 10 ]; then
    find "$directory" -maxdepth 1 -type f | head -10  # 显示前十个文件
    echo "... (and $(($file_count - 10)) more files)"  # 显示剩余文件数
  else
    find "$directory" -maxdepth 1 -type f  # 如果少于或等于10个文件，全部显示
  fi
  echo ""  # 输出一个空行作为分隔
}

# 递归处理每个目录
export -f process_directory
find "$target_directory" -type d -exec bash -c 'process_directory "$0"' {} \;
