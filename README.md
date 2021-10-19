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

Oh and BTW as of 19 October 2021 here are my top 50:

```
ls 1545
cd 715
vim 305
sudo 267
ssh 225
atril 216
xz 215
git 181
dosbox 146
trash-put 145
mplayer 136
ebook-viewer 117
mv 110
ipython3 83
R 78
gs 74
for 73
fg 70
unzip 70
ristretto 69
ping 68
du 66
mkdir 64
python3 61
file 61
locate 55
find 54
trash-empty 53
cat 50
man 50
fortune 49
grep 46
less 44
xsol 44
gcloud 41
dirs 40
make 39
view 37
zipinfo 34
popd 33
ps 32
NODE_PATH=/usr/local/lib/node_modules 31
Rscript 29
tail 29
zip 28
leafpad 27
echo 27
wget 25
jobs 24
./configure 23
```
