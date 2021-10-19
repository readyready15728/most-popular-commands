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
