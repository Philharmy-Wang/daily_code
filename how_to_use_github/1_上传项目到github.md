# 在 VSCode 中将代码同步到你的 GitHub 仓库

```
git init
git remote add origin https://github.com/your-username/your-repository.git
git config --global user.name "Philharmy_Wang"
git config --global user.email "1271578900@qq.com"

# 添加所有新的或已修改的文件到 Git 的暂存区
git add .

# 提交你的更改，确保替换 "Initial commit" 为描述你更改的信息
git commit -m "Initial commit"

# 把提交推送到 GitHub
git push -u origin main


```



在 Visual Studio Code (VSCode) 中将代码同步到 GitHub 需要以下几个步骤。确保你已经安装了 Git，并且在 GitHub 上有一个账户和仓库。

1. **安装 Git**:

   - 如果你还没有安装 Git，请先[下载并安装 Git](https://git-scm.com/downloads)。
2. **打开 VSCode**:

   - 打开你想要同步到 GitHub 的项目文件夹。
3. **初始化 Git 仓库**:

   - 打开终端（Terminal）并运行 `git init` 来初始化一个新的 Git 仓库。
4. **连接到 GitHub 仓库**:

   - 运行 `git remote add origin https://github.com/your-username/your-repository.git` 来连接你的本地仓库到 GitHub。将 `your-username` 和 `your-repository.git` 替换为你的 GitHub 用户名和仓库名。
5. **配置用户信息**:

   - 运行 `git config --global user.name "Your Name"` 和 `git config --global user.email "your-email@example.com"` 来配置你的用户信息。
6. **添加文件到仓库**:

   - 运行 `git add .` 来添加所有的文件到仓库。
7. **提交你的代码**:

   - 运行 `git commit -m "Initial commit"` 来提交你的代码。
8. **推送代码到 GitHub**:

   - 运行 `git push -u origin master` 来推送你的代码到 GitHub。

以上是通过命令行在 VSCode 中将代码同步到 GitHub 的基本步骤。此外，VSCode 也有集成的 Git 功能和插件，如 GitLens，可以通过图形用户界面(GUI)来完成以上步骤，使得过程更为简单和直观。
