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

# 删除远程分之
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