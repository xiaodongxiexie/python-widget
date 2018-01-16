```git
# .gitconfig配置用如下配置可以使用pycharm的diff和merge工具（已经安装pycharm）
[diff]
    tool = pycharm
[difftool "pycharm"]
    cmd = /usr/local/bin/charm diff "$LOCAL" "$REMOTE" && echo "Press enter to continue..." && read
[merge]
    tool = pycharm
    keepBackup = false
[mergetool "pycharm"]
    cmd = /usr/local/bin/charm merge "$LOCAL" "$REMOTE" "$BASE" "$MERGED"

# 用来review：
git log --since=1.days --committer=PegasusWang --author=PegasusWang
git diff commit1 commit2

# 冲突以后使用远端的版本：
git checkout --theirs templates/efmp/campaign.mako

# 防止http协议每次都要输入密码：
git config --global credential.helper 'cache --timeout=36000000'      #秒数

# 暂存和恢复
git stash
git stash apply
git stash apply stash@{1}
git stash pop # 重新应用储藏并且从堆栈中移走

# 删除远程分支
git push origin --delete {the_remote_branch}

# 手残 add 完以后输入错了 commit 信息
git commit --amend

# 撤销 add （暂存）
git reset -- file

# 撤销修改
git checkout -- file

# 手残pull错了分支就
git reset --hard HEAD~

# How to revert Git repository to a previous commit?, https://stackoverflow.com/questions/4114095/how-to-revert-git-repository-to-a-previous-commit
git reset --hard 0d1d7fc32

# 手残直接在master分之改了并且add了
git reset --soft HEAD^
git branch new_branch
git checkout new_branch
git commit -a -m "..."
    # 或者
git reset --soft HEAD^
    git stash
git checkout new_branch
    git stash pop
# 如果改了master但是没有add比较简单，三步走
git stash
git checkout -b new_branch
git stash pop

# rename branch
git branch -m <oldname> <newname>
git branch -m <newname> # rename the current branch

# 指定文件类型diff
git diff master -- '*.c' '*.h'
# 带有上下文的diff
git diff master --no-prefix -U999

# undo add
git reset <file>
git reset    # undo all

# 查看add后的diff
git diff --staged

# http://weizhifeng.net/git-rebase.html
# rebase改变历史, 永远不要用在master分之，别人有可能使用你的分之时也不要用
# only change history for commits that have not yet been pushed
# master has changed since I stared my feature branch, and I want bo bring my branch up to date with master. - Dont't merge. rebase
# rebase: finds the merge base; cherry-picks all commits; reassigns the branch pointer.
# then git push -f
# git rebase --abort

# 全局 ignore, 对于不同编辑器协作的人比较有用
git config --global core.excludesfile ~/.gitignore_global

# 拉取别人远程分支，在 .git/config 里配置好
git fetch somebody somebranch
git checkout -b somebranch origin/somebranch
```
## Git工作流

```git
git checkout master    # 切到master
git pull origin master     # 拉取更新
git checkout -b newbranch    # 新建分之，名称最好起个有意义的，比如jira号等

# 开发中。。。
git fetch origin master    # fetch master
git rebase origin/master    #

# 开发完成等待合并到master，推荐使用 rebase 保持线性的提交历史，但是记住不要在公众分之搞，如果有无意义的提交也可以用 rebase -i 压缩提交
git rebase -i origin/master
git checkout master
git merge newbranch
git push origin master

# 压缩提交
git rebase -i HEAD~~    # 最近两次提交
```

## Git hook

比如我们要在每次 commit 之前运行下单测，进入项目的 .git/hooks 目录， “cp pre-commit.sample pre-commit” 修改内容如下:

```
#!/bin/sh

if git rev-parse --verify HEAD >/dev/null 2>&1
then
    against=HEAD
else
    # Initial commit: diff against an empty tree object
    against=4b825dc642cb6eb9a060e54bf8d69288fbee4904
fi

# Redirect output to stderr.
exec 1>&2

if /your/path/bin/test:    # 这里添加需要运行的测试脚本
then
    exit 0
else
    exit 1
fi

# If there are whitespace errors, print the offending file names and fail.
exec git diff-index --check --cached $against --
```