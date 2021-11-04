# Most Popular Commands
## Not relying on my memory

In an IT-related discussion forum I saw the question "Just curious ... what are
some of the most helpful commands you guys/girls have learned that you use
most frequently?"

Well I could rely on my memory like a normal person but because I'm not a
normal person I wrote a script to automate the task instead. First, I got rid
of the neither-ASCII nor-Unicode crud in my `.zsh_history` because I am using
`zsh` on a Raspberry Pi 400. (`fish` is better but required slightly more
effort to install.) The following site helped immensely:

[Check for non-ASCII characters](https://pages.cs.wisc.edu/~markm/ascii.html)

Without that crud gone the Python script would have choked.

Anyway, I then sifted through all the lines in my `.zsh_history` and extracted
the command names and sorted them in descending order of usage. The script is
for `zsh` specifically but I suspect it can easily be tailored to other shells
such as the default of `bash` or `fish`. Enjoy!

Oh and BTW as of 4 November 2021 here are my top 50:

```
ls 1801
cd 845
vim 478
git 371
sudo 286
xz 245
atril 241
ssh 226
trash-put 182
dosbox 146
mplayer 136
ebook-viewer 126
mv 125
ipython3 92
R 82
python3 79
gs 79
mkdir 77
du 76
for 75
fg 72
trash-empty 72
unzip 71
ristretto 71
ping 69
locate 69
make 68
file 67
cat 66
find 61
man 54
view 51
fortune 50
cp 49
less 49
racket 48
grep 48
dirs 44
xsol 44
gcloud 41
htop 36
ps 36
zipinfo 35
Rscript 34
popd 34
NODE_PATH=/usr/local/lib/node_modules 31
echo 31
zip 29
tail 29
leafpad 28
```
