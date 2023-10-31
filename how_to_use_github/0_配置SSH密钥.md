# 配置SSH密钥

## **1. 检查SSH密钥是否存在** :

首先，你需要检查你的系统上是否已经有一个SSH密钥。打开终端，并运行以下命令：

```
ls -al ~/.ssh
```

这将列出你的 `.ssh`目录中的所有文件。你应该看到一对密钥文件，例如 `id_rsa`和 `id_rsa.pub`。如果没有，你需要创建一个新的SSH密钥。


## **2. 创建SSH密钥**

如果你还没有SSH密钥，运行以下命令来创建一个新的SSH密钥（使用你的电子邮件地址替换 `your-email@example.com`）：

```
ssh-keygen -t rsa -b 4096 -C "your-email@example.com"
```

当提示你输入文件以保存密钥时，只需按 `Enter`接受默认位置。

一直按`enter`就行。


## **3. 添加SSH密钥到ssh-agent** :

确保 `ssh-agent`在后台运行，并添加你的SSH密钥：

```
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_rsa
```


## **4. 将SSH密钥添加到你的GitHub账户** :

运行以下命令，将SSH公钥复制到剪贴板：

```
clip < ~/.ssh/id_rsa.pub
```

或者，你可以使用文本编辑器打开 `~/.ssh/id_rsa.pub`文件，并手动复制内容。

```
sudo gedit `~/.ssh/id_rsa.pub`
```

* 登录到你的GitHub账户。
* 在右上角的用户头像旁边，点击并进入“Settings”（设置）。

* 在左侧的侧边栏中，点击“SSH and GPG keys”（SSH和GPG密钥）。
* 点击“New SSH key”（新SSH密钥），粘贴你的公钥，为密钥命名，然后点击“Add SSH key”（添加SSH密钥）。

## **5. 再次尝试推送** :


现在你应该能够通过运行以下命令将你的代码推送到GitHub：

```
git push -u origin main
```
